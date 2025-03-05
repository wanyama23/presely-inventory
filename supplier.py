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

    update_button=tk.Button(button_Frame, text='Update', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d')
    update_button.grid(row=0,column=1)

    delete_button=tk.Button(button_Frame, text='Delete', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d')
    delete_button.grid(row=0,column=2, padx=20)

    clear_button=tk.Button(button_Frame, text='Clear', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d')
    clear_button.grid(row=0,column=3)


    right_frame=tk.Frame(supplier_frame,bg='white')
    right_frame.place(x=520,y=95,width=500,height=350)


    search_frame=tk.Frame(right_frame,bg='white')
    search_frame.pack(pady=(0,20))

    num_label=tk.Label(search_frame,text='Invoice No.',font=('times new roman',14,'bold'),bg='white')
    num_label.grid(row=0,column=0,padx=(0,15),sticky='w')
    search_entry=tk.Entry(search_frame,font=('times new roman',14,'bold'),bg='lightyellow',width=12)
    search_entry.grid(row=0,column=1)

    search_button=tk.Button(search_frame, text='Search', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d')
    search_button.grid(row=0,column=2,padx=15)

    show_button=tk.Button(search_frame, text='Show All', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d')
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

    treeview_data(treeview)



