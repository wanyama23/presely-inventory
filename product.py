import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


def product_form(root):
    global back_image,logo
    product_frame = tk.Frame(root, width=1070,height=567, bg='white')
    product_frame.place(x=200, y=100)

    back_image = PhotoImage(file='back.png')

    back_button = tk.Button(product_frame, image=back_image, bd=0, cursor='hand2',bg='white', command=lambda: product_frame.place_forget())

    back_button.place(x=10, y=30)

    left_frame =tk.Frame(product_frame, bg='white')
    left_frame.place(x=20, y=60)
    

    heading_label=tk.Label(left_frame, text='Manage product Details',font=('times new roman', 16, 'bold'), bg='#0f4d7d',fg='white')
    heading_label.grid(row=0,columnspan=2)

    category_label=tk.Label(left_frame,text='Category',font=('times new roman',14,'bold'),bg='white')
    category_label.grid(row=1,column=0,padx=20,sticky='w')

    category_combobox=ttk.Combobox(left_frame,font=('times new roman',14,'bold'),width=10,state='readonly')
    category_combobox.grid(row=1,column=1,pady=20)
    category_combobox.set('select')


    supplier_label=tk.Label(left_frame,text='Supplier',font=('times new roman',14,'bold'),bg='white')
    supplier_label.grid(row=2,column=0,padx=20,sticky='w')

    supplier_combobox=ttk.Combobox(left_frame,font=('times new roman',14,'bold'),width=10,state='readonly')
    supplier_combobox.grid(row=2,column=1)
    supplier_combobox.set('select')


    name_label=tk.Label(left_frame,text='Name',font=('times new roman',14,'bold'),bg='white')
    name_label.grid(row=3,column=0,padx=20,sticky='w')
    name_entry=tk.Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    name_entry.grid(row=3,column=1,pady=20)

    price_label=tk.Label(left_frame,text='Price',font=('times new roman',14,'bold'),bg='white')
    price_label.grid(row=4,column=0,padx=20,sticky='w')
    price_entry=tk.Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    price_entry.grid(row=4,column=1)


    quantity_label=tk.Label(left_frame,text='Quantity',font=('times new roman',14,'bold'),bg='white')
    quantity_label.grid(row=5,column=0,padx=20,sticky='w')
    quantity_entry=tk.Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    quantity_entry.grid(row=5,column=1,pady=20)


    status_label=tk.Label(left_frame,text='Status',font=('times new roman',14,'bold'),bg='white')
    status_label.grid(row=6,column=0,padx=20,sticky='w')

    status_combobox=ttk.Combobox(left_frame,values=('Active','Inactive'),font=('times new roman',14,'bold'),width=10,state='readonly')
    status_combobox.grid(row=6,column=1)
    status_combobox.set('select status')


    button_frame=tk.Button(left_frame,bg='white')
    button_frame.grid(row=7,columnspan=2,pady=(30,10))

    add_button=tk.Button(button_frame, text='Add', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d')
    add_button.grid(row=0,column=0,padx=10)

    update_button=tk.Button(button_frame, text='Update', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d')
    update_button.grid(row=0,column=1,padx=10)

    clear_button = tk.Button(button_frame, text='Clear', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d')
    clear_button.grid(row=0, column=2, padx=10)

    delete_button = tk.Button(button_frame, text='Delete', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d')
    delete_button.grid(row=0, column=3, padx=10)

