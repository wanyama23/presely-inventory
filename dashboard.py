import tkinter as tk
from tkinter import PhotoImage, LEFT
from datetime import datetime
from tkinter import messagebox  # For error messages
import pymysql
from employee import employee_form
from supplier import supplier_form
from category import category_form
from product import product_form
from sale import sale_form


def update_datetime(subtitle_label):
    """Update the date and time dynamically on the dashboard."""
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%H:%M:%S %p")
    subtitle_label.config(text=f"Welcome Admin\t\t Date: {current_date}\t\t Time: {current_time}")
    # Re-run this function after 1000ms (1 second)
    subtitle_label.after(1000, update_datetime, subtitle_label)


def connect_database():
    """Connect to MySQL database."""
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            database='inventory_system'
        )
        return connection
    except Exception as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return None


def fetch_total_suppliers():
    """Fetch the total number of suppliers from the database."""
    connection = connect_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM supplier_data")  # Ensure supplier_data table exists
            total_suppliers = cursor.fetchone()[0]
            connection.close()
            return total_suppliers
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching supplier data: {e}")
            return 0
    else:
        return 0


def update_supplier_count(label):
    """Update the supplier count label dynamically."""
    total_suppliers = fetch_total_suppliers()
    label.config(text=str(total_suppliers))



def fetch_total_employees():
    """Fetch the total number of employees from the database."""
    connection = connect_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM employee_data")  # Ensure employee_data table exists
            total_employees = cursor.fetchone()[0]
            connection.close()
            return total_employees
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching employee data: {e}")
            return 0
    else:
        return 0

def update_employee_count(label):
    """Update the employee count label dynamically."""
    total_employees = fetch_total_employees()
    label.config(text=str(total_employees))  # Update the label dynamically


def fetch_total_category():
    """Fetch the total number of category from the database."""
    connection = connect_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM category_data")  # Ensure employee_data table exists
            total_category = cursor.fetchone()[0]
            connection.close()
            return total_category
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching category data: {e}")
            return 0
    else:
        return 0

def update_category_count(label):
    """Update the category count label dynamically."""
    total_category = fetch_total_category()
    label.config(text=str(total_category))  # Update the label dynamically


def fetch_total_product():
    """Fetch the total number of product from the database."""
    connection = connect_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM product_data")  # Ensure product_data table exists
            total_product = cursor.fetchone()[0]
            connection.close()
            return total_product
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching product data: {e}")
            return 0
    else:
        return 0

def update_product_count(label):
    """Update the product count label dynamically."""
    total_product = fetch_total_product()
    label.config(text=str(total_product))  # Update the label dynamically

def fetch_total_sales():
    """Fetch the total number of sales from the database."""
    connection = connect_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM sales")  # Ensure sales_data table exists
            total_sales = cursor.fetchone()[0]
            connection.close()
            return total_sales
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching sales data: {e}")
            return 0
    else:
        return 0

def update_sales_count(label):
    """Update the sales count label dynamically."""
    total_sales = fetch_total_sales()
    label.config(text=str(total_sales))  # Update the label dynamically



def show_dashboard():
    """Function to show the admin dashboard after successful login."""
    root = tk.Tk()
    root.title("Dashboard")
    root.geometry("1270x668+0+0")
    root.config(bg='white')

    # Store global references to prevent garbage collection of images
    global bg_image, employee_icon, supplier_icon, category_icon, product_icon, sales_icon, exit_icon

    # Load background image
    try:
        bg_image = PhotoImage(file='inventory(1).png')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load background image. Ensure the file exists. {e}")
        return

    # Load all icon images with debugging for each file path
    try:
        employee_icon = PhotoImage(file='man.png')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load employee icon. Ensure the file exists. {e}")
        return

    try:
        supplier_icon = PhotoImage(file='tracking.png')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load supplier icon. Ensure the file exists. {e}")
        return

    try:
        category_icon = PhotoImage(file='categorization.png')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load category icon. Ensure the file exists. {e}")
        return

    try:
        product_icon = PhotoImage(file='cubes.png')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load product icon. Ensure the file exists. {e}")
        return

    try:
        sales_icon = PhotoImage(file='trend.png')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load sales icon. Ensure the file exists. {e}")
        return

    try:
        exit_icon = PhotoImage(file='logout.png')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load exit icon. Ensure the file exists. {e}")
        return

    # Create label with image and text
    titleLabel = tk.Label(root, image=bg_image, compound=LEFT, text='  Presely Management System',
                          font=('times new roman', 40, 'bold'), bg='#010048', fg='white', anchor='w', padx=20)
    titleLabel.place(x=0, y=0, relwidth=1)

    # Create Logout button
    logoutButton = tk.Button(root, text='Logout', font=('times new roman', 20, 'bold'), fg='#010048',
                              command=root.destroy)  # Close the dashboard
    logoutButton.place(x=1100, y=10)

    # Create subtitle label
    subtitleLabel = tk.Label(root, font=('times new roman', 15), bg='#4d636d', fg='white')
    subtitleLabel.place(x=0, y=70, relwidth=1)
    update_datetime(subtitleLabel)  # Call the function to update the time

    # Create left frame
    leftFrame = tk.Frame(root)
    leftFrame.place(x=0, y=102, width=200, height=555)

    # Load and display logo image
    logoImage = PhotoImage(file='checklist.png')
    root.logoImage = logoImage  # Prevent garbage collection
    imageLabel = tk.Label(leftFrame, image=logoImage)
    imageLabel.pack()

    # Create menu label
    menuLabel = tk.Label(leftFrame, text='Menu', font=('times new roman', 20), bg='#009688')
    menuLabel.pack(fill=tk.X)

    # Create buttons for various modules with images
    employee_button = tk.Button(leftFrame, image=employee_icon, compound=LEFT, text='Employees',
                                 font=('times new roman', 20, 'bold'), anchor='w', padx=10,
                                 command=lambda: employee_form(root))
    employee_button.pack(fill=tk.X)

    supplier_button = tk.Button(leftFrame, image=supplier_icon, compound=LEFT, text='Suppliers',
                                 font=('times new roman', 20, 'bold'), anchor='w', padx=10,
                                 command=lambda: supplier_form(root))
    supplier_button.pack(fill=tk.X)

    category_button = tk.Button(leftFrame, image=category_icon, compound=LEFT, text='Categories',
                                 font=('times new roman', 20, 'bold'), anchor='w', padx=10,
                                 command=lambda: category_form(root))
    category_button.pack(fill=tk.X)

    product_button = tk.Button(leftFrame, image=product_icon, compound=LEFT, text='Products',
                                font=('times new roman', 20, 'bold'), anchor='w', padx=10,
                                command=lambda: product_form(root))
    product_button.pack(fill=tk.X)

    sales_button = tk.Button(leftFrame, image=sales_icon, compound=LEFT, text='Sales',
                              font=('times new roman', 20, 'bold'), anchor='w', padx=10,
                              command=lambda: sale_form(root))
    sales_button.pack(fill=tk.X)

    exit_button = tk.Button(leftFrame, image=exit_icon, compound=LEFT, text='Exit',
                             font=('times new roman', 20, 'bold'), anchor='w', command=root.destroy)
    exit_button.pack(fill=tk.X)

    # Frames and widgets from the original code
    emp_frame = tk.Frame(root, bg='#2c3e50', bd=3, relief='ridge')
    emp_frame.place(x=400, y=125, height=170, width=280)
    total_emp_icon = PhotoImage(file='division(1).png')
    total_emp_icon_label = tk.Label(emp_frame, image=total_emp_icon, bg='#2c3e50')
    total_emp_icon_label.pack(pady=10)

    total_emp_label = tk.Label(emp_frame, text='Total Employees', bg='#2c3e50', fg='white',
                               font=('times new roman', 15, 'bold'))
    total_emp_label.pack()

    total_emp_count_label = tk.Label(emp_frame, text="Loading...", bg='#2c3e50', fg='white', font=('times new roman', 30, 'bold'))
    total_emp_count_label.pack()
    update_employee_count(total_emp_count_label)  # 🔹 Call the function after placing the label


    # total_emp_count_label = tk.Label(emp_frame, text='0', bg='#2c3e50', fg='white',
    #                                  font=('times new roman', 30, 'bold'))
    # total_emp_count_label.pack()


    sup_frame = tk.Frame(root, bg='#8e44ad', bd=3, relief='ridge')
    sup_frame.place(x=800, y=125, height=170, width=280)
    total_sup_icon = PhotoImage(file='supplier(1).png')
    total_sup_icon_label = tk.Label(sup_frame, image=total_sup_icon, bg='#8e44ad')
    total_sup_icon_label.pack(pady=10)

    total_sup_label = tk.Label(sup_frame, text='Total Suppliers', bg='#8e44ad', fg='white', font=('times new roman', 15, 'bold'))
    total_sup_label.pack()

    total_sup_count_label = tk.Label(sup_frame, text="Loading...", bg='#8e44ad', fg='white', font=('times new roman', 30, 'bold'))
    total_sup_count_label.pack()
    update_supplier_count(total_sup_count_label)  # 🔹 Call the function after placing the label



    cat_frame = tk.Frame(root, bg='#27ae60', bd=3, relief='ridge')
    cat_frame.place(x=400, y=310, height=170, width=280)
    total_cat_icon = PhotoImage(file='market-segment.png')
    total_cat_icon_label = tk.Label(cat_frame, image=total_cat_icon, bg='#27ae60')
    total_cat_icon_label.pack(pady=10)

    total_cat_label = tk.Label(cat_frame, text='Category', bg='#27ae60', fg='white', font=('times new roman', 15, 'bold'))
    total_cat_label.pack()

    total_cat_count_label = tk.Label(cat_frame, text="Loading...", bg='#8e44ad', fg='white', font=('times new roman', 30, 'bold'))
    total_cat_count_label.pack()
    update_category_count(total_cat_count_label)  # 🔹 Call the function after placing the label

    prod_frame = tk.Frame(root, bg='#2c3e50', bd=3, relief='ridge')
    prod_frame.place(x=800, y=310, height=170, width=280)
    total_prod_icon = PhotoImage(file='products.png')
    total_prod_icon_label = tk.Label(prod_frame, image=total_prod_icon, bg='#2c3e50')
    total_prod_icon_label.pack(pady=10)

    total_prod_label = tk.Label(prod_frame, text='Total Products', bg='#2c3e50', fg='white', font=('times new roman', 15, 'bold'))
    total_prod_label.pack()

    total_prod_count_label = tk.Label(prod_frame, text="Loading...", bg='#8e44ad', fg='white', font=('times new roman', 30, 'bold'))
    total_prod_count_label.pack()
    update_product_count(total_prod_count_label)

    sales_frame = tk.Frame(root, bg='#2c3e50', bd=3, relief='ridge')
    sales_frame.place(x=600, y=495, height=170, width=280)
    total_sales_icon = PhotoImage(file='graph.png')
    total_sales_icon_label = tk.Label(sales_frame, image=total_sales_icon, bg='#2c3e50')
    total_sales_icon_label.pack(pady=10)

    total_sales_label = tk.Label(sales_frame, text='Total Sales', bg='#2c3e50', fg='white', font=('times new roman', 15, 'bold'))
    total_sales_label.pack()

    total_sales_count_label = tk.Label(sales_frame, text="Loading...", bg='#8e44ad', fg='white', font=('times new roman', 30, 'bold'))
    total_sales_count_label.pack()
    update_sales_count(total_sales_count_label)

    root.mainloop()




def login():
    """Login function to validate Admin credentials."""
    admin_id = admin_id_entry.get()
    password = password_entry.get()

    # Replace these values with your actual database authentication logic
    valid_admin_id = "admin"  # Example Admin ID
    valid_password = "1234"  # Example password

    if admin_id == valid_admin_id and password == valid_password:
        login_window.destroy()  # Close the login window
        show_dashboard()  # Show the dashboard
    else:
        messagebox.showerror("Login Failed", "Invalid Admin ID or Password")


# Create the Login Window
login_window = tk.Tk()
login_window.title("Admin Login")
login_window.geometry("400x300+500+200")
login_window.config(bg='white')

# Create login form
login_label = tk.Label(login_window, text="Admin Login", font=('times new roman', 20, 'bold'), bg='white', fg='#010048')
login_label.pack(pady=20)

admin_id_label = tk.Label(login_window, text="Admin ID", font=('times new roman', 15), bg='white')
admin_id_label.pack(pady=5)
admin_id_entry = tk.Entry(login_window, font=('times new roman', 15), width=25)
admin_id_entry.pack(pady=5)

password_label = tk.Label(login_window, text="Password", font=('times new roman', 15), bg='white')
password_label.pack(pady=5)
password_entry = tk.Entry(login_window, font=('times new roman', 15), width=25, show="*")  # Password input with masking
password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="Login", font=('times new roman', 15, 'bold'), bg='#010048', fg='white',
                         command=login)
login_button.pack(pady=20)

login_window.mainloop()





















# Functionality
# def employee_form():
#     global back_image
#     employee_frame = tk.Frame(root, width=1070, height=567, bg='white')
#     employee_frame.place(x=200, y=100)
#     headingLabel = tk.Label(employee_frame, text='Manage Employee Details', font=('times new romans', 16, 'bold'), bg='#0f4d7d', fg='white')
#     headingLabel.place(x=0, y=0, relwidth=1)

#     back_image = PhotoImage(file='back.png')
#     back_button = tk.Button(employee_frame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: employee_frame.place_forget())
#     back_button.place(x=10, y=30)

#     top_frame = tk.Frame(employee_frame,bg='white')
#     top_frame.place(x=0, y=60, relwidth=1, height=235)
#     search_frame = tk.Frame(top_frame,bg='white')
#     search_frame.pack()
#     search_combobox = ttk.Combobox(search_frame, values=('Id', 'Name', 'Email'),font=('times new roman',20),state='readonly')
#     search_combobox.set('Search By')
#     search_combobox.grid(row=0, column=0,padx=20)
#     search_entry=tk.Entry(search_frame,font=('times new roman',12),bg='lightyellow')
#     search_entry.grid(row=0,column=1)
#     search_button=tk.Button(search_frame,text='Search',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     search_button.grid(row=0,column=2,padx=20)
#     show_button=tk.Button(search_frame,text='Show All',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     show_button.grid(row=0,column=3)


#     horizontal_scrollbar=tk.Scrollbar(top_frame,orient=HORIZONTAL)
#     verticall_scrollbar=tk.Scrollbar(top_frame,orient=VERTICAL)
#     employee_treeview=ttk.Treeview(top_frame,columns=('empid','name','email','gender','contact','dob','employment_type','education','work_shift','address','doj','salary','usertype'),show='headings',yscrollcommand=verticall_scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
#     horizontal_scrollbar.pack(side=BOTTOM,fill=tk.X)
#     verticall_scrollbar.pack(side=RIGHT,fill=tk.Y)
#     horizontal_scrollbar.config(command=employee_treeview.xview)
#     employee_treeview.pack(pady=10)

#     employee_treeview.heading('empid',text='Empid')
#     employee_treeview.heading('name',text='Name')
#     employee_treeview.heading('email',text='Email')
#     employee_treeview.heading('gender',text='Gender')
#     employee_treeview.heading('contact',text='Contact')
#     employee_treeview.heading('dob',text='Dob')
#     employee_treeview.heading('employment_type',text='Employment_type')
#     employee_treeview.heading('education',text='Eductaion')
#     employee_treeview.heading('work_shift',text='Work_shift')
#     employee_treeview.heading('address',text='Address')
#     employee_treeview.heading('doj',text='Doj')
#     employee_treeview.heading('salary',text='Salary')
#     employee_treeview.heading('usertype',text='Usertype')

#     employee_treeview.column('empid',width=60)
#     employee_treeview.column('name',width=140)
#     employee_treeview.column('email',width=180)
#     employee_treeview.column('gender',width=80)
#     employee_treeview.column('contact',width=100)
#     employee_treeview.column('dob',width=100)
#     employee_treeview.column('employment_type',width=120)
#     employee_treeview.column('education',width=120)
#     employee_treeview.column('work_shift',width=100)
#     employee_treeview.column('address',width=200)
#     employee_treeview.column('doj',width=100)
#     employee_treeview.column('salary',width=100)
#     employee_treeview.column('usertype',width=120)

#     detail_frame=tk.Frame(employee_frame,bg='white')
#     detail_frame.place(x=20,y=300)

#     empid_label=tk.Label(detail_frame,text='Empid',font=('times new roman',12))
#     empid_label.grid(row=0,column=0,padx=20,pady=10, sticky='w')
#     empid_entry=tk.Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
#     empid_entry.grid(row=0,column=1,padx=20,pady=10)

#     name_label=tk.Label(detail_frame,text='Name',font=('times new roman',12))
#     name_label.grid(row=0,column=2,padx=20,pady=10, sticky='w')
#     name_entry=tk.Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
#     name_entry.grid(row=0,column=3,padx=20,pady=10)

#     email_label=tk.Label(detail_frame,text='Email',font=('times new roman',12))
#     email_label.grid(row=0,column=4,padx=20,pady=10, sticky='w')
#     email_entry=tk.Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
#     email_entry.grid(row=0,column=5,padx=20,pady=10)

#     gender_label=tk.Label(detail_frame,text='Gender',font=('times new roman',12))
#     gender_label.grid(row=1,column=0,padx=20,pady=10, sticky='w')

#     gender_combobox=ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
#     gender_combobox.set('select Gender')
#     gender_combobox.grid(row=1,column=1)


#     dob_label=tk.Label(detail_frame,text='Date of Birth',font=('times new roman',12))
#     dob_label.grid(row=1,column=2,padx=20,pady=10, sticky='w')

#     dob_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
#     dob_date_entry.grid(row=1,column=3)


#     contact_label=tk.Label(detail_frame,text='Contact',font=('times new roman',12))
#     contact_label.grid(row=1,column=4, padx=20, pady=10, sticky='w')
#     contact_enrty=tk.Entry(detail_frame,font=('times new roman',12), bg='lightyellow')
#     contact_enrty.grid(row=1,column=5, padx=20,pady=10)

#     employment_type_label=tk.Label(detail_frame,text='Employment Type',font=('times new roman',12))
#     employment_type_label.grid(row=2,column=0,padx=20,pady=10, sticky='w')

#     employment_type_combobox=ttk.Combobox(detail_frame,values=('Full Time','Part Time','Cusual','Contract','Intern'),font=('times new roman',12),width=18,state='readonly')
#     employment_type_combobox.set('select Type')
#     employment_type_combobox.grid(row=2,column=1)

#     education_label=tk.Label(detail_frame,text='Education',font=('times new roman',12))
#     education_label.grid(row=2,column=2,padx=20,pady=10, sticky='w')

#     education_option=["B.tech", "M.tech", "M.Cos", "M.SC", "BBA", "MBA"]

#     education_combobox=ttk.Combobox(detail_frame,values=education_option,font=('times new roman',12),width=18,state='readonly')
#     education_combobox.set('select Education')
#     education_combobox.grid(row=2,column=3)

#     work_shift_label=tk.Label(detail_frame,text='Work Shift',font=('times new roman',12))
#     work_shift_label.grid(row=2,column=4,padx=20,pady=10, sticky='w')

#     work_shift_combobox=ttk.Combobox(detail_frame,values=('Morning','Evening'),font=('times new roman',12),width=18,state='readonly')
#     work_shift_combobox.set('select Shift')
#     work_shift_combobox.grid(row=2,column=5)


#     address_label=tk.Label(detail_frame, text='Address',font=('times new roman',12))
#     address_label.grid(row=3,column=0,padx=20,pady=10, sticky='w')
#     address_text=tk.Text(detail_frame,width=20,height=3, font=('times new roman',12),bg='lightyellow')
#     address_text.grid(row=3,column=1, rowspan=2)


#     doj_label=tk.Label(detail_frame,text='Date of Joining',font=('times new roman',12))
#     doj_label.grid(row=3,column=2,padx=20,pady=10, sticky='w')

#     doj_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
#     doj_date_entry.grid(row=3,column=3)


#     usertype_label=tk.Label(detail_frame,text='User Type',font=('times new roman',12))
#     usertype_label.grid(row=4,column=2,padx=20,pady=10, sticky='w')

#     usertype_combobox=ttk.Combobox(detail_frame,values=('Admin','Employee'),font=('times new roman',12),width=18,state='readonly')
#     usertype_combobox.set('select Usertype')
#     usertype_combobox.grid(row=4,column=3)

#     salary_label=tk.Label(detail_frame,text='Salary',font=('times new roman',12))
#     salary_label.grid(row=3,column=4, padx=20, pady=10, sticky='w')
#     salary_enrty=tk.Entry(detail_frame,font=('times new roman',12), bg='lightyellow')
#     salary_enrty.grid(row=3,column=5, padx=20,pady=10)

#     password_label=tk.Label(detail_frame,text='Password',font=('times new roman',12))
#     password_label.grid(row=4,column=4, padx=20, pady=10)
#     password_enrty=tk.Entry(detail_frame,font=('times new roman',12), bg='lightyellow')
#     password_enrty.grid(row=4,column=5, padx=20,pady=10)


#     button_frame=tk.Frame(employee_frame,bg='white')
#     button_frame.place(x=200,y=530)

#     add_button=tk.Button(button_frame,text='Add',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     add_button.grid(row=0,column=0,padx=20)

#     update_button=tk.Button(button_frame,text='Update',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     update_button.grid(row=0,column=1,padx=20)

#     delete_button=tk.Button(button_frame,text='Delete',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     delete_button.grid(row=0,column=2,padx=20)

#     clear_button=tk.Button(button_frame,text='clear',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     clear_button.grid(row=0,column=3,padx=20)





















# Functionality
# def employee_form():
#     global back_image
#     employee_frame = tk.Frame(root, width=1070, height=567, bg='white')
#     employee_frame.place(x=200, y=100)
#     headingLabel = tk.Label(employee_frame, text='Manage Employee Details', font=('times new romans', 16, 'bold'), bg='#0f4d7d', fg='white')
#     headingLabel.place(x=0, y=0, relwidth=1)

#     back_image = PhotoImage(file='back.png')
#     back_button = tk.Button(employee_frame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: employee_frame.place_forget())
#     back_button.place(x=10, y=30)

#     top_frame = tk.Frame(employee_frame,bg='white')
#     top_frame.place(x=0, y=60, relwidth=1, height=235)
#     search_frame = tk.Frame(top_frame,bg='white')
#     search_frame.pack()
#     search_combobox = ttk.Combobox(search_frame, values=('Id', 'Name', 'Email'),font=('times new roman',20),state='readonly')
#     search_combobox.set('Search By')
#     search_combobox.grid(row=0, column=0,padx=20)
#     search_entry=tk.Entry(search_frame,font=('times new roman',12),bg='lightyellow')
#     search_entry.grid(row=0,column=1)
#     search_button=tk.Button(search_frame,text='Search',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     search_button.grid(row=0,column=2,padx=20)
#     show_button=tk.Button(search_frame,text='Show All',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     show_button.grid(row=0,column=3)


#     horizontal_scrollbar=tk.Scrollbar(top_frame,orient=HORIZONTAL)
#     verticall_scrollbar=tk.Scrollbar(top_frame,orient=VERTICAL)
#     employee_treeview=ttk.Treeview(top_frame,columns=('empid','name','email','gender','contact','dob','employment_type','education','work_shift','address','doj','salary','usertype'),show='headings',yscrollcommand=verticall_scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
#     horizontal_scrollbar.pack(side=BOTTOM,fill=tk.X)
#     verticall_scrollbar.pack(side=RIGHT,fill=tk.Y)
#     horizontal_scrollbar.config(command=employee_treeview.xview)
#     employee_treeview.pack(pady=10)

#     employee_treeview.heading('empid',text='Empid')
#     employee_treeview.heading('name',text='Name')
#     employee_treeview.heading('email',text='Email')
#     employee_treeview.heading('gender',text='Gender')
#     employee_treeview.heading('contact',text='Contact')
#     employee_treeview.heading('dob',text='Dob')
#     employee_treeview.heading('employment_type',text='Employment_type')
#     employee_treeview.heading('education',text='Eductaion')
#     employee_treeview.heading('work_shift',text='Work_shift')
#     employee_treeview.heading('address',text='Address')
#     employee_treeview.heading('doj',text='Doj')
#     employee_treeview.heading('salary',text='Salary')
#     employee_treeview.heading('usertype',text='Usertype')

#     employee_treeview.column('empid',width=60)
#     employee_treeview.column('name',width=140)
#     employee_treeview.column('email',width=180)
#     employee_treeview.column('gender',width=80)
#     employee_treeview.column('contact',width=100)
#     employee_treeview.column('dob',width=100)
#     employee_treeview.column('employment_type',width=120)
#     employee_treeview.column('education',width=120)
#     employee_treeview.column('work_shift',width=100)
#     employee_treeview.column('address',width=200)
#     employee_treeview.column('doj',width=100)
#     employee_treeview.column('salary',width=100)
#     employee_treeview.column('usertype',width=120)

#     detail_frame=tk.Frame(employee_frame,bg='white')
#     detail_frame.place(x=20,y=300)

#     empid_label=tk.Label(detail_frame,text='Empid',font=('times new roman',12))
#     empid_label.grid(row=0,column=0,padx=20,pady=10, sticky='w')
#     empid_entry=tk.Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
#     empid_entry.grid(row=0,column=1,padx=20,pady=10)

#     name_label=tk.Label(detail_frame,text='Name',font=('times new roman',12))
#     name_label.grid(row=0,column=2,padx=20,pady=10, sticky='w')
#     name_entry=tk.Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
#     name_entry.grid(row=0,column=3,padx=20,pady=10)

#     email_label=tk.Label(detail_frame,text='Email',font=('times new roman',12))
#     email_label.grid(row=0,column=4,padx=20,pady=10, sticky='w')
#     email_entry=tk.Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
#     email_entry.grid(row=0,column=5,padx=20,pady=10)

#     gender_label=tk.Label(detail_frame,text='Gender',font=('times new roman',12))
#     gender_label.grid(row=1,column=0,padx=20,pady=10, sticky='w')

#     gender_combobox=ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
#     gender_combobox.set('select Gender')
#     gender_combobox.grid(row=1,column=1)


#     dob_label=tk.Label(detail_frame,text='Date of Birth',font=('times new roman',12))
#     dob_label.grid(row=1,column=2,padx=20,pady=10, sticky='w')

#     dob_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
#     dob_date_entry.grid(row=1,column=3)


#     contact_label=tk.Label(detail_frame,text='Contact',font=('times new roman',12))
#     contact_label.grid(row=1,column=4, padx=20, pady=10, sticky='w')
#     contact_enrty=tk.Entry(detail_frame,font=('times new roman',12), bg='lightyellow')
#     contact_enrty.grid(row=1,column=5, padx=20,pady=10)

#     employment_type_label=tk.Label(detail_frame,text='Employment Type',font=('times new roman',12))
#     employment_type_label.grid(row=2,column=0,padx=20,pady=10, sticky='w')

#     employment_type_combobox=ttk.Combobox(detail_frame,values=('Full Time','Part Time','Cusual','Contract','Intern'),font=('times new roman',12),width=18,state='readonly')
#     employment_type_combobox.set('select Type')
#     employment_type_combobox.grid(row=2,column=1)

#     education_label=tk.Label(detail_frame,text='Education',font=('times new roman',12))
#     education_label.grid(row=2,column=2,padx=20,pady=10, sticky='w')

#     education_option=["B.tech", "M.tech", "M.Cos", "M.SC", "BBA", "MBA"]

#     education_combobox=ttk.Combobox(detail_frame,values=education_option,font=('times new roman',12),width=18,state='readonly')
#     education_combobox.set('select Education')
#     education_combobox.grid(row=2,column=3)

#     work_shift_label=tk.Label(detail_frame,text='Work Shift',font=('times new roman',12))
#     work_shift_label.grid(row=2,column=4,padx=20,pady=10, sticky='w')

#     work_shift_combobox=ttk.Combobox(detail_frame,values=('Morning','Evening'),font=('times new roman',12),width=18,state='readonly')
#     work_shift_combobox.set('select Shift')
#     work_shift_combobox.grid(row=2,column=5)


#     address_label=tk.Label(detail_frame, text='Address',font=('times new roman',12))
#     address_label.grid(row=3,column=0,padx=20,pady=10, sticky='w')
#     address_text=tk.Text(detail_frame,width=20,height=3, font=('times new roman',12),bg='lightyellow')
#     address_text.grid(row=3,column=1, rowspan=2)


#     doj_label=tk.Label(detail_frame,text='Date of Joining',font=('times new roman',12))
#     doj_label.grid(row=3,column=2,padx=20,pady=10, sticky='w')

#     doj_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
#     doj_date_entry.grid(row=3,column=3)


#     usertype_label=tk.Label(detail_frame,text='User Type',font=('times new roman',12))
#     usertype_label.grid(row=4,column=2,padx=20,pady=10, sticky='w')

#     usertype_combobox=ttk.Combobox(detail_frame,values=('Admin','Employee'),font=('times new roman',12),width=18,state='readonly')
#     usertype_combobox.set('select Usertype')
#     usertype_combobox.grid(row=4,column=3)

#     salary_label=tk.Label(detail_frame,text='Salary',font=('times new roman',12))
#     salary_label.grid(row=3,column=4, padx=20, pady=10, sticky='w')
#     salary_enrty=tk.Entry(detail_frame,font=('times new roman',12), bg='lightyellow')
#     salary_enrty.grid(row=3,column=5, padx=20,pady=10)

#     password_label=tk.Label(detail_frame,text='Password',font=('times new roman',12))
#     password_label.grid(row=4,column=4, padx=20, pady=10)
#     password_enrty=tk.Entry(detail_frame,font=('times new roman',12), bg='lightyellow')
#     password_enrty.grid(row=4,column=5, padx=20,pady=10)


#     button_frame=tk.Frame(employee_frame,bg='white')
#     button_frame.place(x=200,y=530)

#     add_button=tk.Button(button_frame,text='Add',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     add_button.grid(row=0,column=0,padx=20)

#     update_button=tk.Button(button_frame,text='Update',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     update_button.grid(row=0,column=1,padx=20)

#     delete_button=tk.Button(button_frame,text='Delete',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     delete_button.grid(row=0,column=2,padx=20)

#     clear_button=tk.Button(button_frame,text='clear',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
#     clear_button.grid(row=0,column=3,padx=20)