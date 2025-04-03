import tkinter as tk
from tkinter import PhotoImage, LEFT, HORIZONTAL, VERTICAL, BOTTOM, RIGHT, END
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime
import pymysql

        
def connect_database():
    try:
        connection = pymysql.connect(host='localhost', user='root', password='1234')
        cursor = connection.cursor()
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Database connectivity issue: {e}')
        return None, None
    

    return cursor, connection


def create_database_table():
    cursor,connection=connect_database()
    cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system')
    cursor.execute('USE inventory_system')
    cursor.execute('CREATE TABLE IF NOT EXISTS employee_data (empid INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), gender VARCHAR(50), contact VARCHAR(100), dob VARCHAR(30), employment_type VARCHAR(50), education VARCHAR(100), work_shift VARCHAR(50), address VARCHAR(100), doj VARCHAR(30), salary VARCHAR(50), usertype VARCHAR(50), password VARCHAR(50))')

def treeview_data():
    cursor,connection=connect_database()
    if not cursor or not connection:
        return
    cursor.execute('use inventory_system')
    try:
        cursor.execute('SELECT * from employee_data')
        employee_records=cursor.fetchall()
        employee_treeview.delete(*employee_treeview.get_children())
        # print(employee_records)
        for record in employee_records:
            employee_treeview.insert('',END,values=record)
    except Exception as e:
        messagebox.showerror('Error',f'error due to {e}')
    finally:
        cursor.close()
        connection.close         
        

def select_data(event, empid_entry, name_entry, email_entry, gender_combobox, dob_date_entry, contact_entry, employment_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry):
    index = employee_treeview.selection()
    if not index:
        messagebox.showerror("Error", "No row selected")
        return
    
    content = employee_treeview.item(index)
    row = content['values']

    try:
        # Clear existing entries
        empid_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        gender_combobox.set("")
        dob_date_entry.set_date(datetime.date.today())  # Reset to today by default
        contact_entry.delete(0, tk.END)
        employment_type_combobox.set("")
        education_combobox.set("")
        work_shift_combobox.set("")
        address_text.delete("1.0", tk.END)
        doj_date_entry.set_date(datetime.date.today())
        salary_entry.delete(0, tk.END)
        usertype_combobox.set("")
        password_entry.delete(0, tk.END)

        # Populate fields with data from the selected row
        empid_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        email_entry.insert(0, row[2])
        gender_combobox.set(row[3])
        
        # Validate the DOB value before setting it in dob_date_entry
        try:
            dob = datetime.datetime.strptime(row[4], '%d/%m/%Y')  # Convert to datetime object
            dob_date_entry.set_date(dob)
        except (ValueError, TypeError):
            messagebox.showwarning("Warning", f"Invalid date for DOB: {row[4]}")
            dob_date_entry.set_date(datetime.date.today())  # Default to today if invalid
        
        contact_entry.insert(0, row[5])
        employment_type_combobox.set(row[6])
        education_combobox.set(row[7])
        work_shift_combobox.set(row[8])
        address_text.insert("1.0", row[9])

        # Validate the DOJ value before setting it in doj_date_entry
        try:
            doj = datetime.datetime.strptime(row[10], '%d/%m/%Y')
            doj_date_entry.set_date(doj)
        except (ValueError, TypeError):
            messagebox.showwarning("Warning", f"Invalid date for DOJ: {row[10]}")
            doj_date_entry.set_date(datetime.date.today())

        salary_entry.insert(0, row[11])
        usertype_combobox.set(row[12])
        password_entry.insert(0, row[13])
    
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")




def add_employee(empid, name, email, gender, dob, contact, employment_type, education, work_shift, address, doj, salary, usertype, password):
    if (empid == '' or name == '' or email == '' or gender == '' or dob == '' or contact == '' or employment_type == '' or
        education == '' or work_shift == '' or address.strip() == '' or doj == '' or salary == '' or usertype == '' or password == ''):
        messagebox.showerror('Error', 'All fields are required')
        return
    
    cursor, connection = connect_database()
    if not cursor or not connection:
        return
    try:
        cursor.execute('USE inventory_system')
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS employee_data (
                empid INT PRIMARY KEY, 
                name VARCHAR(100), 
                email VARCHAR(100), 
                gender VARCHAR(50), 
                contact VARCHAR(100), 
                dob VARCHAR(30), 
                employment_type VARCHAR(50), 
                education VARCHAR(100), 
                work_shift VARCHAR(50), 
                address VARCHAR(100), 
                doj VARCHAR(30), 
                salary VARCHAR(50), 
                usertype VARCHAR(50), 
                password VARCHAR(50))'''
        )
        cursor.execute('SELECT * FROM employee_data WHERE empid=%s', (empid,))
        if cursor.fetchone():
            messagebox.showerror('Error', 'Employee ID already exists')
            return
        
        cursor.execute(
            'INSERT INTO employee_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (empid, name, email, gender, contact, dob, employment_type, education, work_shift, address, doj, salary, usertype, password)
        )
        connection.commit()
        messagebox.showinfo('Success', 'Employee added successfully')
        treeview_data()
    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        connection.close()




def clear_fields(empid_entry, name_entry, email_entry, gender_combobox,
                 dob_date_entry, contact_entry, employment_type_combobox,
                 education_combobox, work_shift_combobox, address_text,
                 doj_date_entry, salary_entry, usertype_combobox, password_entry):
    # Clear each field
    empid_entry.delete(0, END)
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    gender_combobox.set('')  # Reset ComboBox
    dob_date_entry.set_date(None)  # Reset DateEntry
    contact_entry.delete(0, END)
    employment_type_combobox.set('')
    education_combobox.set('')
    work_shift_combobox.set('')
    address_text.delete(1.0, END)
    doj_date_entry.set_date(None)  # Reset DateEntry
    salary_entry.delete(0, END)
    usertype_combobox.set('')
    password_entry.delete(0, END)






def update_employee(empid, name, email, gender, dob, contact, employment_type, education, work_shift, address, doj, salary, usertype, password, treeview):
    if (empid == '' or name == '' or email == '' or gender == '' or dob == '' or contact == '' or employment_type == '' or
        education == '' or work_shift == '' or address.strip() == '' or doj == '' or salary == '' or usertype == '' or password == ''):
        messagebox.showerror('Error', 'All fields are required')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        try:
            cursor.execute('USE inventory_system')
            cursor.execute('SELECT * FROM employee_data WHERE empid=%s', (empid,))
            record = cursor.fetchone()
            if not record:
                messagebox.showerror('Error', 'Employee ID does not exist')
                return

            # Prepare the new data for comparison
            new_data = (name, email, gender, dob, contact, employment_type, education, work_shift, address.strip(), doj, salary, usertype, password)

            # Check if the new data is the same as the existing data
            current_data = record[1:]  # Exclude empid for comparison
            if current_data == new_data:
                messagebox.showerror('Error', 'No changes made')
                return

            # Perform the update
            cursor.execute(
                '''UPDATE employee_data 
                SET name=%s, email=%s, gender=%s, dob=%s, contact=%s, employment_type=%s, education=%s, work_shift=%s,
                    address=%s, doj=%s, salary=%s, usertype=%s, password=%s 
                WHERE empid=%s''',
                (name, email, gender, dob, contact, employment_type, education, work_shift, address.strip(), doj, salary, usertype, password, empid)
            )
            connection.commit()

            # Check if the update was successful
            if cursor.rowcount == 0:
                messagebox.showerror('Error', 'No updates made')
            else:
                messagebox.showinfo('Info', 'Employee details updated successfully')
                treeview_data(treeview)

        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()
   


def delete_employee(empid, treeview):
    if empid == '':
        messagebox.showerror('Error', 'Employee ID is required')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        try:
            cursor.execute('USE inventory_system')
            cursor.execute('SELECT * FROM employee_data WHERE empid=%s', (empid,))
            record = cursor.fetchone()
            if not record:
                messagebox.showerror('Error', 'Employee ID does not exist')
                return
            cursor.execute('DELETE FROM employee_data WHERE empid=%s', (empid,))
            connection.commit()

            # Check if the deletion was successful
            if cursor.rowcount == 0:
                messagebox.showerror('Error', 'Error deleting the employee')
            else:
                messagebox.showinfo('Info', 'Employee deleted successfully')
                treeview_data(treeview)

        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()

def search_employee(treeview, search_combobox, search_entry):
    """Search employee data based on the criteria in the Combobox and Entry."""
    search_by = search_combobox.get()
    search_value = search_entry.get()

    if search_by == 'Search By':
        messagebox.showerror('Error', 'Please select a search criteria')
        return

    if search_value.strip() == '':
        messagebox.showerror('Error', 'Please enter a value to search')
        return

    column_map = {'Id': 'empid', 'Name': 'name', 'Email': 'email'}
    column_name = column_map.get(search_by)

    cursor, connection = connect_database()
    if not cursor or not connection:
        return
    try:
        cursor.execute('USE inventory_system')
        query = f'SELECT * FROM employee_data WHERE {column_name} LIKE %s'
        cursor.execute(query, (f'%{search_value}%',))
        records = cursor.fetchall()

        # Clear the Treeview before showing search results
        treeview.delete(*treeview.get_children())

        # Populate the Treeview with fetched records
        if records:
            for record in records:
                treeview.insert('', tk.END, values=record)
        else:
            messagebox.showinfo('Info', 'No matching records found')
    except Exception as e:
        messagebox.showerror('Error', f'Error searching data: {e}')
    finally:
        cursor.close()
        connection.close()


def employee_form(root):
    global back_image,employee_treeview
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

    treeview_data()
    
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
    password_enrty.grid(row=4,column=5, padx=20,pady=10)\
    


    button_frame=tk.Frame(employee_frame,bg='white')
    button_frame.place(x=200,y=530)

    add_button=tk.Button(button_frame,text='Add',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :add_employee(empid_entry.get(),name_entry.get(),email_entry.get(),gender_combobox.get(),
                                                                                                                                                  dob_date_entry.get(),contact_enrty.get(),employment_type_combobox.get(),
                                                                                                                                                  education_combobox.get(),work_shift_combobox.get(),address_text.get(1.0,END),
                                                                                                                                                  doj_date_entry.get(),salary_enrty.get(),usertype_combobox.get(),password_enrty.get()))
    add_button.grid(row=0,column=0,padx=20)


    update_button = tk.Button(
    button_frame,
    text='Update',
    font=('times new roman', 12),
    width=10,
    cursor='hand2',
    fg='white',
    bg='#0f4d7d',
    command=lambda: update_employee(
        empid_entry.get(),
        name_entry.get(),
        email_entry.get(),
        gender_combobox.get(),
        treeview  # Pass the treeview argument here
    )
)
    update_button.grid(row=0,column=1,padx=20)


    # update_button=tk.Button(button_frame,text='Update',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :update_employee(empid_entry.get(),name_entry.get(),email_entry.get(),gender_combobox.get(),
    #                                                                                                                                               dob_date_entry.get(),contact_enrty.get(),employment_type_combobox.get(),
    #                                                                                                                                               education_combobox.get(),work_shift_combobox.get(),address_text.get(1.0,END),
    #                                                                                                                                               doj_date_entry.get(),salary_enrty.get(),usertype_combobox.get(),password_enrty.get()))
    # update_button.grid(row=0,column=1,padx=20)

    delete_button=tk.Button(button_frame,text='Delete',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    delete_button.grid(row=0,column=2,padx=20)

    # clear_button=tk.Button(button_frame,text='clear',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :clear_fields(empid_entry,name_entry,email_entry,gender_combobox,
    #                                                                                                                                               dob_date_entry,contact_enrty,employment_type_combobox,
    #                                                                                                                                               education_combobox,work_shift_combobox,address_text,
    #                                                                                                                                               doj_date_entry,salary_enrty,usertype_combobox,password_enrty,True))
    # clear_button.grid(row=0,column=3,padx=20)

    clear_button = tk.Button(button_frame, text='Clear', font=('times new roman', 12), width=10,
                         cursor='hand2', fg='white', bg='#0f4d7d',
                         command=lambda: clear_fields(empid_entry, name_entry, email_entry, gender_combobox,
                                                      dob_date_entry, contact_enrty, employment_type_combobox,
                                                      education_combobox, work_shift_combobox, address_text,
                                                      doj_date_entry, salary_enrty, usertype_combobox, password_enrty))
    clear_button.grid(row=0, column=3, padx=20)


    employee_treeview.bind('<ButtonRelease-1>', 
                       lambda event: select_data(event, empid_entry, name_entry, email_entry, gender_combobox,
                                                 dob_date_entry, contact_enrty, employment_type_combobox,
                                                 education_combobox, work_shift_combobox, address_text,
                                                 doj_date_entry, salary_enrty, usertype_combobox, password_enrty))





#     employee_treeview.bind(
#     '<ButtonRelease-1>',
#     lambda event: select_data(
#         event, empid_entry, name_entry, email_entry, gender_combobox, dob_date_entry,
#         contact_enrty, employment_type_combobox, education_combobox, work_shift_combobox,
#         address_text, doj_date_entry, salary_enrty, usertype_combobox, password_enrty, employee_treeview
#     )
# )

    

    # employee_treeview.bind('<ButtonRelease-1>',lambda event:select_data(empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,contact_enrty,employment_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_enrty,usertype_combobox,password_enrty))

    create_database_table



    



























    # def connect_database():
#     try:
#         # Connect to MySQL database
#         connection = pymysql.connect(host='localhost', user='root', password='1234', database='inventory_system')
#         cursor = connection.cursor()
#     except pymysql.MySQLError as e:
#         # Show error message if connection fails
#         messagebox.showerror('Error', f'Database connectivity issue: {str(e)}')
#         return None, None
    
#     # Create database if it doesn't exist
#     cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system')
#     cursor.execute('USE inventory_system')

#     # Create table if it doesn't exist
#     cursor.execute('''CREATE TABLE IF NOT EXISTS employee_data (
#                         empid INT PRIMARY KEY, 
#                         name VARCHAR(100), 
#                         email VARCHAR(100), 
#                         gender VARCHAR(50), 
#                         contact VARCHAR(100), 
#                         dob VARCHAR(30), 
#                         employment_type VARCHAR(50), 
#                         education VARCHAR(100), 
#                         work_shift VARCHAR(50), 
#                         address VARCHAR(100), 
#                         doj VARCHAR(30), 
#                         salary VARCHAR(50), 
#                         usertype VARCHAR(50), 
#                         password VARCHAR(50)
#                       )''')

#     return cursor, connection
    # connection.commit()
    # connection.close()


















    # def connect_database():
#     try:
#         connection = pymysql.connect(host='localhost', user='root', password='1234')
#         cursor = connection.cursor()
#         cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system')
#         cursor.execute('USE inventory_system')
#         cursor.execute('''CREATE TABLE IF NOT EXISTS employee_data (
#                             empid INT PRIMARY KEY, 
#                             name VARCHAR(100), 
#                             email VARCHAR(100), 
#                             gender VARCHAR(50), 
#                             contact VARCHAR(100), 
#                             dob VARCHAR(30), 
#                             employment_type VARCHAR(50), 
#                             education VARCHAR(100), 
#                             work_shift VARCHAR(50), 
#                             address VARCHAR(100), 
#                             doj VARCHAR(30), 
#                             salary VARCHAR(50), 
#                             usertype VARCHAR(50), 
#                             password VARCHAR(50)
#                           )''')
#         return cursor, connection
#     except pymysql.MySQLError as e:
#         # Create a Tkinter root window
#         root = tk()
#         root.withdraw()  # Hide the root window
#         messagebox.showerror('Error', f'Database connectivity issue: {str(e)}')
#         root.destroy()  # Destroy the root window
#         return None, None

# def treeview_data():
#     cursor, connection = connect_database()
#     if not cursor or not connection:
#         return
#     cursor.execute('SELECT * FROM employee_data')
#     employee_records = cursor.fetchall()
#     print(employee_records)

# def add_employee(empid, name, email, gender, dob, contact, employment_type, education, work_shift, address, doj, salary, user_type, password):
#     if (empid == '' or name == '' or email == '' or gender == 'Select Gender' or contact == '' or employment_type == 'select type' or education == 'Select Education' or work_shift == 'select Shift' or address == '\n' or salary == '' or user_type == 'select User Type' or password == ''):
#         messagebox.showerror("Error", "All fields are required")
#     else:
#         cursor, connection = connect_database()
#         if not cursor or not connection:
#             return
#         cursor.execute('INSERT INTO employee_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (empid, name, email, gender, dob, contact, employment_type, education, work_shift, address, doj, salary, user_type, password))
#         connection.commit()
#         treeview_data()
#         messagebox.showinfo('Success', 'Data is inserted successfully')