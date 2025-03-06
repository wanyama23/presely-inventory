import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, VERTICAL, HORIZONTAL, RIGHT, BOTTOM, X, Y, BOTH, END
from tkinter import messagebox
from employee import connect_database


def delete_category(treeview):
        index = treeview.selection()
        content=treeview.item(index)
        row=content['values']
        id=row[0]
        if not index:
            messagebox.showerror('Error','No row is selected')
            return
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
    # if id == '':
    #     messagebox.showerror('Error', 'Id number is required')
    # else:
    #     cursor, connection = connect_database()
    #     if not cursor or not connection:
    #         return
        try:
            cursor.execute('use inventory_system')
            # cursor.execute('SELECT * FROM category_data WHERE id=%s', (id,))
            # if not cursor.fetchone():
            #     messagebox.showerror('Error', 'ID does not exist')
            #     return
            cursor.execute('DELETE FROM category_data WHERE id=%s', (id,))
            connection.commit()
            messagebox.showinfo('Info', 'Data deleted successfully')
            treeview_data(treeview)
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()


def clear(id_entry,category_name_entry,description_text):
    id_entry.delete(0,END)
    category_name_entry.delete(0,END)
    description_text.delete(1.0,END)

def treeview_data(treeview):
    cursor,connection=connect_database()
    if not cursor or not connection:
        return
    cursor.execute('use inventory_system')
    cursor.execute('select * from category_data')
    records=cursor.fetchall()
    treeview.delete(*treeview.get_children())
    for record in records:
        treeview.insert('',END,values=record)


def add_category(id, name, description, treeview):
    if id == '' or name == '' or description == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        try:
            cursor.execute('use inventory_system')
            cursor.execute('CREATE TABLE IF NOT EXISTS category_data(id INT PRIMARY KEY, name VARCHAR(100), description TEXT)')

            cursor.execute('SELECT * FROM category_data WHERE id=%s', (id,))
            if cursor.fetchone():
                messagebox.showerror('Error', 'Id already exists')
                return

            cursor.execute(
                'INSERT INTO category_data VALUES(%s, %s, %s)', (id, name, description.strip())
            )
            connection.commit()
            messagebox.showinfo('Info', 'Data inserted successfully')
            treeview_data(treeview)
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()






def category_form(root):
    global back_image,logo
    category_frame = tk.Frame(root, width=1070,height=567, bg='white')
    category_frame.place(x=200, y=100)

    heading_label=tk.Label(category_frame, text='Manage Category Details',font=('times new roman', 16, 'bold'), bg='#0f4d7d',fg='white')
    heading_label.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file='back.png')

    back_button = tk.Button(category_frame, image=back_image, bd=0, cursor='hand2',bg='white', command=lambda: category_frame.place_forget())

    back_button.place(x=10, y=30)

    logo=PhotoImage(file='best-seller(3).png')
    label=tk.Label(category_frame,image=logo,bg='white')
    label.place(x=30,y=100)

    details_frame=tk.Label(category_frame,bg='white')
    details_frame.place(x=500,y=60)

    id_label=tk.Label(details_frame,text='Id',font=('times new roman',14,'bold'),bg='white')
    id_label.grid(row=0,column=0,padx=20,sticky='w')
    id_entry=tk.Entry(details_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    id_entry.grid(row=0,column=1)

    category_name_label=tk.Label(details_frame,text='Category Name',font=('times new roman',14,'bold'),bg='white')
    category_name_label.grid(row=1,column=0,padx=20,sticky='w')
    category_name_entry=tk.Entry(details_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    category_name_entry.grid(row=1,column=1,pady=20)

    description_label=tk.Label(details_frame,text='Description',font=('times new roman',14,'bold'),bg='white')
    description_label.grid(row=2,column=0,padx=20,sticky='nw')

    description_text=tk.Text(details_frame,width=25,height=6,bd=2)
    description_text.grid(row=2,column=1)

    button_frame=tk.Label(category_frame,bg='white')
    button_frame.place(x=650,y=280)

    add_button=tk.Button(button_frame, text='Add', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :add_category(id_entry.get(),category_name_entry.get(),description_text.get(1.0,END).strip(),treeview))
    add_button.grid(row=0,column=0,padx=20)

    delete_button=tk.Button(button_frame, text='Delete', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :delete_category(treeview))
    delete_button.grid(row=0,column=1,padx=20)

    clear_button=tk.Button(button_frame, text='Clear', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :clear(id_entry,category_name_entry,description_text))
    clear_button.grid(row=0,column=2,padx=20)

    treeview_frame=tk.Label(category_frame,bg='white')
    treeview_frame.place(x=530,y=340,height=200,width=500)


    scrolly=tk.Scrollbar(treeview_frame,orient=VERTICAL)
    scrollx=tk.Scrollbar(treeview_frame,orient=HORIZONTAL) 
    treeview=ttk.Treeview(treeview_frame,columns=('id','name','description'),show='headings',yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.pack(side=BOTTOM,fill=X)
    scrollx.config(command=treeview.xview)
    scrolly.config(command=treeview.yview)
    treeview.pack(fill=BOTH, expand=1)

    treeview.heading('id',text='Id')
    treeview.heading('name',text='Category Name')
    treeview.heading('description',text='Description')

    treeview.column('id',width=80)
    treeview.column('name',width=140)
    treeview.column('description',width=300)
    treeview_data(treeview)

