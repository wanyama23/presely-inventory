import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, HORIZONTAL, VERTICAL, BOTTOM, RIGHT, X, Y, BOTH, END
from tkinter import messagebox
from employee import connect_database


def treeview_data(treeview):
    cursor,connection=connect_database()
    if not cursor or not connection:
        return
    cursor.execute('use inventory_system')
    cursor.execute('select * from supplier_data')
    records=cursor.fetchall()
    treeview.delete(*treeview.get_children())
    for record in records:
        treeview.insert('',END,values=record)



def select_data(event, invoice_entry, name_entry, contact_entry, description_text, treeview):
    try:
        # Get the selected item in the Treeview
        selected_row = treeview.selection()[0]
        row = treeview.item(selected_row, 'values')  # Get the values from the selected row

        # Populate the fields in the supplier form
        invoice_entry.delete(0, END)
        invoice_entry.insert(0, row[0])  # Invoice number

        name_entry.delete(0, END)
        name_entry.insert(0, row[1])  # Supplier name

        contact_entry.delete(0, END)
        contact_entry.insert(0, row[2])  # Supplier contact

        description_text.delete(1.0, END)
        description_text.insert(1.0, row[3])  # Description
    except IndexError:
        messagebox.showerror('Error', 'No item selected')
    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')


# def add_supplier(invoice, name, contact, description,treeview):
#     if invoice=='' or name=='' or contact=='' or description.strip()=='':
#         messagebox.showerror('Error','All fields are requires')
#     else:
#         cursor,connection=connect_database()
#         if not cursor or not connection:
#             return
#         try:
#         cursor.execute('use inventory_system')
#         cursor.execute('SELECT * from supplier_data WHERE invoice=%s',invoice)
#         if cursor.fetchone():
#             messagebox.showerror('Error','Id already exists')
#         cursor.execute('CREATE TABLE IF NOT EXISTS supplier_data(invoice INT PRIMARY KEY,name VARCHAR(100), contact VARCHAR(15), description TEXT)') 

#         cursor.execute('INSERT INTO supplier_data VALUES(%s,%s,%s,%s)',(invoice,name,contact,description.strip()))   
#         connection.commit()
#         messagebox.showinfo('info','Data is inserted')
#         treeview_data(treeview)
#     except Exception as e:
# messagebox.showerror('Error',f'Error due to {e}')


def add_supplier(invoice, name, contact, description, treeview):
    if invoice == '' or name == '' or contact == '' or description.strip() == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        try:
            cursor.execute('use inventory_system')
            cursor.execute('SELECT * from supplier_data WHERE invoice=%s', (invoice,))
            if cursor.fetchone():
                messagebox.showerror('Error', 'Invoice ID already exists')
                return
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS supplier_data(invoice INT PRIMARY KEY, name VARCHAR(100), contact VARCHAR(15), description TEXT)'
            )
            cursor.execute(
                'INSERT INTO supplier_data VALUES(%s, %s, %s, %s)', (invoice, name, contact, description.strip())
            )
            connection.commit()
            messagebox.showinfo('Info', 'Data inserted successfully')
            treeview_data(treeview)
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()    


def update_supplier(invoice, name, contact, description, treeview):
    if invoice == '' or name == '' or contact == '' or description.strip() == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        try:
            cursor.execute('use inventory_system')
            cursor.execute('SELECT * FROM supplier_data WHERE invoice=%s', (invoice,))
            record = cursor.fetchone()
            if not record:
                messagebox.showerror('Error', 'Invoice ID does not exist')
                return

            # Perform the update
            cursor.execute(
                'UPDATE supplier_data SET name=%s, contact=%s, description=%s WHERE invoice=%s',
                (name, contact, description.strip(), invoice)
            )
            connection.commit()

            # Check if the update was successful
            if cursor.rowcount == 0:
                messagebox.showerror('Error', 'No updates made')
            else:
                messagebox.showinfo('Info', 'Data updated successfully')
                treeview_data(treeview)

        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()


def delete_supplier(invoice, treeview):
    if invoice == '':
        messagebox.showerror('Error', 'Invoice number is required')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        try:
            cursor.execute('use inventory_system')
            cursor.execute('SELECT * FROM supplier_data WHERE invoice=%s', (invoice,))
            if not cursor.fetchone():
                messagebox.showerror('Error', 'Invoice ID does not exist')
                return
            cursor.execute('DELETE FROM supplier_data WHERE invoice=%s', (invoice,))
            connection.commit()
            messagebox.showinfo('Info', 'Data deleted successfully')
            treeview_data(treeview)
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()

def search_supplier(invoice, treeview):
    if invoice == '':
        messagebox.showerror('Error', 'Invoice number is required for search')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        try:
            cursor.execute('use inventory_system')
            cursor.execute('SELECT * FROM supplier_data WHERE invoice=%s', (invoice,))
            record = cursor.fetchone()
            treeview.delete(*treeview.get_children())
            if record:
                treeview.insert('', END, values=record)
            else:
                messagebox.showinfo('Info', 'No record found')
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()
            
def clear_fields(invoice_entry, name_entry, contact_entry, description_text):
    invoice_entry.delete(0, END)
    name_entry.delete(0, END)
    contact_entry.delete(0, END)
    description_text.delete(1.0, END)


def supplier_form(root):
    global back_image
    supplier_frame = tk.Frame(root, width=1070,height=567, bg='white')
    supplier_frame.place(x=200, y=100)

    heading_label=tk.Label(supplier_frame, text='Manage Supplier Details',font=('times new roman', 16, 'bold'), bg='#0f4d7d',fg='white')
    heading_label.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file='back.png')

    back_button = tk.Button(supplier_frame, image=back_image, bd=0, cursor='hand2',bg='white', command=lambda: supplier_frame.place_forget())

    back_button.place(x=10, y=30)

    left_frame=tk.Frame(supplier_frame,bg='white')
    left_frame.place(x=10,y=100)

    invoice_label=tk.Label(left_frame,text='Invoice No.',font=('times new roman',14,'bold'),bg='white')
    invoice_label.grid(row=0,column=0,padx=20,sticky='w')
    invoice_entry=tk.Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    invoice_entry.grid(row=0,column=1)

    contact_label=tk.Label(left_frame,text='Supplier Contact',font=('times new roman',14,'bold'),bg='white')
    contact_label.grid(row=2,column=0,padx=20,sticky='w')
    contact_entry=tk.Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    contact_entry.grid(row=2,column=1)


    name_label=tk.Label(left_frame,text='Supplier Name',font=('times new roman',14,'bold'),bg='white')
    name_label.grid(row=1,column=0, padx=20,pady=20,sticky='w')
    name_entry=tk.Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    name_entry.grid(row=1,column=1)


    description_label=tk.Label(left_frame,text='Description',font=('times new roman',14,'bold'),bg='white')
    description_label.grid(row=3,column=0, padx=20,sticky='w')
    description_text=tk.Text(left_frame,width=25,height=6,bd=2)
    description_text.grid(row=3,column=1,pady=25)


    button_Frame=tk.Frame(left_frame,bg='white')
    button_Frame.grid(row=4,columnspan=2,pady=20)

    add_button=tk.Button(button_Frame, text='Add', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :add_supplier(invoice_entry.get(),name_entry.get(),contact_entry.get(),description_text.get(1.0,END),treeview))
    add_button.grid(row=0,column=0,padx=20)

    update_button=tk.Button(button_Frame, text='Update', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d',command=lambda: update_supplier(invoice_entry.get(), name_entry.get(), contact_entry.get(), description_text.get(1.0, END), treeview))
    update_button.grid(row=0,column=1)

    delete_button=tk.Button(button_Frame, text='Delete', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d',command=lambda: delete_supplier(invoice_entry.get(), treeview))
    delete_button.grid(row=0,column=2, padx=20)

    clear_button=tk.Button(button_Frame, text='Clear', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d',command=lambda: clear_fields(invoice_entry, name_entry, contact_entry, description_text)) 
    clear_button.grid(row=0,column=3)


    right_frame=tk.Frame(supplier_frame,bg='white')
    right_frame.place(x=520,y=95,width=500,height=350)


    search_frame=tk.Frame(right_frame,bg='white')
    search_frame.pack(pady=(0,20))

    num_label=tk.Label(search_frame,text='Invoice No.',font=('times new roman',14,'bold'),bg='white')
    num_label.grid(row=0,column=0,padx=(0,15),sticky='w')
    search_entry=tk.Entry(search_frame,font=('times new roman',14,'bold'),bg='lightyellow',width=12)
    search_entry.grid(row=0,column=1)

    search_button=tk.Button(search_frame, text='Search', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d',command=lambda: search_supplier(search_entry.get(), treeview))
    search_button.grid(row=0,column=2,padx=15)

    show_button=tk.Button(search_frame, text='Show All', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d',command=lambda: treeview_data(treeview))
    show_button.grid(row=0,column=3)
     

    scrolly=tk.Scrollbar(right_frame,orient=VERTICAL)
    scrollx=tk.Scrollbar(right_frame,orient=HORIZONTAL) 
    treeview=ttk.Treeview(right_frame,columns=('invoice','name','contact','description'),show='headings',yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.pack(side=BOTTOM,fill=X)
    scrollx.config(command=treeview.xview)
    scrolly.config(command=treeview.yview)
    treeview.pack(fill=BOTH,expand=1)
    treeview.heading('invoice',text='invoice Id')
    treeview.heading('name',text='Supplier Name')
    treeview.heading('contact',text='Supplier Contact')
    treeview.heading('description',text='Description')


    treeview.column('invoice',width=80)
    treeview.column('name',width=160)
    treeview.column('contact',width=120)
    treeview.column('description',width=300)
    # Bind Treeview selection to the select_data function
    treeview.bind('<ButtonRelease-1>', lambda event: select_data(event, invoice_entry, name_entry, contact_entry, description_text, treeview))

    treeview_data(treeview)




