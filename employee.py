import tkinter as tk
from tkinter import PhotoImage, LEFT, HORIZONTAL, VERTICAL, BOTTOM, RIGHT
from tkinter import ttk
from tkcalendar import DateEntry


def employee_form(root):
    global back_image
    employee_frame = tk.Frame(root, width=1070, height=567, bg='white')
    employee_frame.place(x=200, y=100)
    headingLabel = tk.Label(employee_frame, text='Manage Employee Details', font=('times new romans', 16, 'bold'), bg='#0f4d7d', fg='white')
    headingLabel.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file='back.png')
    back_button = tk.Button(employee_frame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: employee_frame.place_forget())
    back_button.place(x=10, y=30)

    top_frame = tk.Frame(employee_frame,bg='white')
    top_frame.place(x=0, y=60, relwidth=1, height=235)
    search_frame = tk.Frame(top_frame,bg='white')
    search_frame.pack()
    search_combobox = ttk.Combobox(search_frame, values=('Id', 'Name', 'Email'),font=('times new roman',20),state='readonly')
    search_combobox.set('Search By')
    search_combobox.grid(row=0, column=0,padx=20)
    search_entry=tk.Entry(search_frame,font=('times new roman',12),bg='lightyellow')
    search_entry.grid(row=0,column=1)
    search_button=tk.Button(search_frame,text='Search',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    search_button.grid(row=0,column=2,padx=20)
    show_button=tk.Button(search_frame,text='Show All',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    show_button.grid(row=0,column=3)


    horizontal_scrollbar=tk.Scrollbar(top_frame,orient=HORIZONTAL)
    verticall_scrollbar=tk.Scrollbar(top_frame,orient=VERTICAL)
    employee_treeview=ttk.Treeview(top_frame,columns=('empid','name','email','gender','contact','dob','employment_type','education','work_shift','address','doj','salary','usertype'),show='headings',yscrollcommand=verticall_scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.pack(side=BOTTOM,fill=tk.X)
    verticall_scrollbar.pack(side=RIGHT,fill=tk.Y)
    horizontal_scrollbar.config(command=employee_treeview.xview)
    employee_treeview.pack(pady=10)

    employee_treeview.heading('empid',text='Empid')
    employee_treeview.heading('name',text='Name')
    employee_treeview.heading('email',text='Email')
    employee_treeview.heading('gender',text='Gender')
    employee_treeview.heading('contact',text='Contact')
    employee_treeview.heading('dob',text='Dob')
    employee_treeview.heading('employment_type',text='Employment_type')
    employee_treeview.heading('education',text='Eductaion')
    employee_treeview.heading('work_shift',text='Work_shift')
    employee_treeview.heading('address',text='Address')
    employee_treeview.heading('doj',text='Doj')
    employee_treeview.heading('salary',text='Salary')
    employee_treeview.heading('usertype',text='Usertype')

    employee_treeview.column('empid',width=60)
    employee_treeview.column('name',width=140)
    employee_treeview.column('email',width=180)
    employee_treeview.column('gender',width=80)
    employee_treeview.column('contact',width=100)
    employee_treeview.column('dob',width=100)
    employee_treeview.column('employment_type',width=120)
    employee_treeview.column('education',width=120)
    employee_treeview.column('work_shift',width=100)
    employee_treeview.column('address',width=200)
    employee_treeview.column('doj',width=100)
    employee_treeview.column('salary',width=100)
    employee_treeview.column('usertype',width=120)

    detail_frame=tk.Frame(employee_frame,bg='white')
    detail_frame.place(x=20,y=300)

    empid_label=tk.Label(detail_frame,text='Empid',font=('times new roman',12))
    empid_label.grid(row=0,column=0,padx=20,pady=10, sticky='w')
    empid_entry=tk.Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    empid_entry.grid(row=0,column=1,padx=20,pady=10)

    name_label=tk.Label(detail_frame,text='Name',font=('times new roman',12))
    name_label.grid(row=0,column=2,padx=20,pady=10, sticky='w')
    name_entry=tk.Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    name_entry.grid(row=0,column=3,padx=20,pady=10)

    email_label=tk.Label(detail_frame,text='Email',font=('times new roman',12))
    email_label.grid(row=0,column=4,padx=20,pady=10, sticky='w')
    email_entry=tk.Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    email_entry.grid(row=0,column=5,padx=20,pady=10)

    gender_label=tk.Label(detail_frame,text='Gender',font=('times new roman',12))
    gender_label.grid(row=1,column=0,padx=20,pady=10, sticky='w')

    gender_combobox=ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
    gender_combobox.set('select Gender')
    gender_combobox.grid(row=1,column=1)


    dob_label=tk.Label(detail_frame,text='Date of Birth',font=('times new roman',12))
    dob_label.grid(row=1,column=2,padx=20,pady=10, sticky='w')

    dob_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
    dob_date_entry.grid(row=1,column=3)


    contact_label=tk.Label(detail_frame,text='Contact',font=('times new roman',12))
    contact_label.grid(row=1,column=4, padx=20, pady=10, sticky='w')
    contact_enrty=tk.Entry(detail_frame,font=('times new roman',12), bg='lightyellow')
    contact_enrty.grid(row=1,column=5, padx=20,pady=10)

    employment_type_label=tk.Label(detail_frame,text='Employment Type',font=('times new roman',12))
    employment_type_label.grid(row=2,column=0,padx=20,pady=10, sticky='w')

    employment_type_combobox=ttk.Combobox(detail_frame,values=('Full Time','Part Time','Cusual','Contract','Intern'),font=('times new roman',12),width=18,state='readonly')
    employment_type_combobox.set('select Type')
    employment_type_combobox.grid(row=2,column=1)

    education_label=tk.Label(detail_frame,text='Education',font=('times new roman',12))
    education_label.grid(row=2,column=2,padx=20,pady=10, sticky='w')

    education_option=["B.tech", "M.tech", "M.Cos", "M.SC", "BBA", "MBA"]

    education_combobox=ttk.Combobox(detail_frame,values=education_option,font=('times new roman',12),width=18,state='readonly')
    education_combobox.set('select Education')
    education_combobox.grid(row=2,column=3)

    work_shift_label=tk.Label(detail_frame,text='Work Shift',font=('times new roman',12))
    work_shift_label.grid(row=2,column=4,padx=20,pady=10, sticky='w')

    work_shift_combobox=ttk.Combobox(detail_frame,values=('Morning','Evening'),font=('times new roman',12),width=18,state='readonly')
    work_shift_combobox.set('select Shift')
    work_shift_combobox.grid(row=2,column=5)


    address_label=tk.Label(detail_frame, text='Address',font=('times new roman',12))
    address_label.grid(row=3,column=0,padx=20,pady=10, sticky='w')
    address_text=tk.Text(detail_frame,width=20,height=3, font=('times new roman',12),bg='lightyellow')
    address_text.grid(row=3,column=1, rowspan=2)


    doj_label=tk.Label(detail_frame,text='Date of Joining',font=('times new roman',12))
    doj_label.grid(row=3,column=2,padx=20,pady=10, sticky='w')

    doj_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
    doj_date_entry.grid(row=3,column=3)


    usertype_label=tk.Label(detail_frame,text='User Type',font=('times new roman',12))
    usertype_label.grid(row=4,column=2,padx=20,pady=10, sticky='w')

    usertype_combobox=ttk.Combobox(detail_frame,values=('Admin','Employee'),font=('times new roman',12),width=18,state='readonly')
    usertype_combobox.set('select Usertype')
    usertype_combobox.grid(row=4,column=3)

    salary_label=tk.Label(detail_frame,text='Salary',font=('times new roman',12))
    salary_label.grid(row=3,column=4, padx=20, pady=10, sticky='w')
    salary_enrty=tk.Entry(detail_frame,font=('times new roman',12), bg='lightyellow')
    salary_enrty.grid(row=3,column=5, padx=20,pady=10)

    password_label=tk.Label(detail_frame,text='Password',font=('times new roman',12))
    password_label.grid(row=4,column=4, padx=20, pady=10)
    password_enrty=tk.Entry(detail_frame,font=('times new roman',12), bg='lightyellow')
    password_enrty.grid(row=4,column=5, padx=20,pady=10)


    button_frame=tk.Frame(employee_frame,bg='white')
    button_frame.place(x=200,y=530)

    add_button=tk.Button(button_frame,text='Add',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    add_button.grid(row=0,column=0,padx=20)

    update_button=tk.Button(button_frame,text='Update',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    update_button.grid(row=0,column=1,padx=20)

    delete_button=tk.Button(button_frame,text='Delete',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    delete_button.grid(row=0,column=2,padx=20)

    clear_button=tk.Button(button_frame,text='clear',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    clear_button.grid(row=0,column=3,padx=20)



    