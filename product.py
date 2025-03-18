# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from tkinter import PhotoImage, RIDGE, VERTICAL, HORIZONTAL, BOTTOM, RIGHT, BOTH, X, Y, END
# from employee import connect_database



# def treeview_data(treeview):
#     cursor,connection=connect_database()
#     if not cursor or not connection:
#         return
#     try:
#         cursor.execute('use inventory_system')
#         cursor.execute('select * from product_data')
#         records=cursor.fetchall()
#         treeview.delete(*treeview.get_children())
#         for record in records:
#             treeview.insert('',END,values=records)
#     except Exception as e:
#         messagebox.showerror('Error',f'Error due to{e}')

#     finally:
#         cursor.close()
#         connection.close            

# def fetch_supplier_category(category_combobox,supplier_combobox):
#     category_option=[]
#     supplier_option=[]
#     cursor,connection=connect_database()
#     if not cursor or not connection:
#         return
#     cursor.execute('USE inventory_system')
#     cursor.execute('SELECT name from category_data')
#     names=cursor.fetchall()
#     for name in names:
#         category_option.append(name[0])
#     category_combobox.config(values=category_option)

#     cursor.execute('SELECT name from supplier_data')
#     names = cursor.fetchall()
#     for name in names:
#         supplier_option.append(name[0])
#     supplier_combobox.config(values=supplier_option)



# def add_data(category, supplier, name, price, quantity, status):
#     if category=='Empty':
#         messagebox.showerror('Error','please add categories')
#     elif supplier=='Empty':
#         messagebox.showerror('Error','please add suppliers')
#     elif category=='Select' or supplier=='Select' or name=='' or price=='' or quantity=='' or status=='Select Status':
#         messagebox.showerror('Error','All fields are required')
#     else:
#         cursor,connection=connect_database()
#         if not cursor or not connection:
#             return
#         cursor.execute('USE inventory_system')
#         cursor.execute('CREATE TABLE IF NOT EXISTS product_data(id INT AUTO_INCREMENT PRIMARY KEY, category VARCHAR(100),supplier VARCHAR(100), name VARCHAR(100), price DECIMAL(10,2),quantity INT, status VARCHAR(50))')
#         cursor.execute(
#     'INSERT INTO product_data (id, category, supplier, name, price, quantity, status) VALUES (%s, %s, %s, %s, %s, %s, %s)',
#     (id, category, supplier, name, price, quantity, status)
# )

#         connection.commit()
#         messagebox.showinfo('success','Data is added successfully')
#         treeview_data(treeview)



# def product_form(root):
#     global back_image
#     # Removed 'logo' since it's unused and undefined
#     product_frame = tk.Frame(root, width=1070, height=567, bg='white')
#     product_frame.place(x=200, y=100)

#     back_image = PhotoImage(file='back.png')

#     back_button = tk.Button(product_frame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: product_frame.place_forget())
#     back_button.place(x=10, y=30)

#     left_frame = tk.Frame(product_frame, bg='white', bd=2, relief=RIDGE)
#     left_frame.place(x=20, y=60)

#     heading_label = tk.Label(left_frame, text='Manage product Details', font=('times new roman', 16, 'bold'), bg='#0f4d7d', fg='white')
#     heading_label.grid(row=0, columnspan=2, sticky='we')

#     category_label = tk.Label(left_frame, text='Category', font=('times new roman', 14, 'bold'), bg='white')
#     category_label.grid(row=1, column=0, padx=20, sticky='w')

#     category_combobox = ttk.Combobox(left_frame, font=('times new roman', 14, 'bold'), width=10, state='readonly')
#     category_combobox.grid(row=1, column=1, pady=20)
#     category_combobox.set('select')

#     supplier_label = tk.Label(left_frame, text='Supplier', font=('times new roman', 14, 'bold'), bg='white')
#     supplier_label.grid(row=2, column=0, padx=20, sticky='w')

#     supplier_combobox = ttk.Combobox(left_frame, font=('times new roman', 14, 'bold'), width=10, state='readonly')
#     supplier_combobox.grid(row=2, column=1)
#     supplier_combobox.set('select')

#     name_label = tk.Label(left_frame, text='Name', font=('times new roman', 14, 'bold'), bg='white')
#     name_label.grid(row=3, column=0, padx=20, sticky='w')
#     name_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     name_entry.grid(row=3, column=1, pady=20)

#     price_label = tk.Label(left_frame, text='Price', font=('times new roman', 14, 'bold'), bg='white')
#     price_label.grid(row=4, column=0, padx=20, sticky='w')
#     price_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     price_entry.grid(row=4, column=1)

#     quantity_label = tk.Label(left_frame, text='Quantity', font=('times new roman', 14, 'bold'), bg='white')
#     quantity_label.grid(row=5, column=0, padx=20, sticky='w')
#     quantity_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     quantity_entry.grid(row=5, column=1, pady=20)

#     status_label = tk.Label(left_frame, text='Status', font=('times new roman', 14, 'bold'), bg='white')
#     status_label.grid(row=6, column=0, padx=20, sticky='w')

#     status_combobox = ttk.Combobox(left_frame, values=('Active', 'Inactive'), font=('times new roman', 14, 'bold'), width=10, state='readonly')
#     status_combobox.grid(row=6, column=1)
#     status_combobox.set('select status')

#     # Corrected button_frame as a Frame
#     button_frame = tk.Frame(left_frame, bg='white')
#     button_frame.grid(row=7, columnspan=2, pady=(30, 10))

#     add_button = tk.Button(button_frame, text='Add', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',command=lambda :add_data(category_combobox.get(),supplier_combobox.get(),name_entry.get(),price_entry.get(),quantity_entry.get(),status_combobox.get()))
#     add_button.grid(row=0, column=0, padx=10)

#     update_button = tk.Button(button_frame, text='Update', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d')
#     update_button.grid(row=0, column=1, padx=10)

#     clear_button = tk.Button(button_frame, text='Clear', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d')
#     clear_button.grid(row=0, column=2, padx=10)

#     delete_button = tk.Button(button_frame, text='Delete', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d')
#     delete_button.grid(row=0, column=3, padx=10)

#     search_frame = tk.LabelFrame(product_frame, text='Search Product', font=('times new roman', 14))
#     search_frame.place(x=500, y=10)

#     search_combobox = ttk.Combobox(search_frame, values=('category', 'supplier', 'Name', 'Status'), state='readonly', width=16, font=('times new roman', 14))
#     search_combobox.grid(row=0, column=0,padx=10)
#     search_combobox.set('Search By')

#     search_entry = tk.Entry(search_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     search_entry.grid(row=0, column=1)

#     search_button = tk.Button(search_frame, text='search', font=('times new roman', 14),width=8, cursor='hand2',fg='white', bg='#0f4d7d')
#     search_button.grid(row=0,column=2,padx=(10,0),pady=10)

#     show_button = tk.Button(search_frame, text='Show All', font=('times new roman',14), width=8,cursor='hand2',fg='white',bg='#0f4d7d')
#     show_button.grid(row=0, column=3, padx=10)

#     treeview_frame = tk.Frame(product_frame)
#     treeview_frame.place(x=480,y=125,width=570,height=430)

#     scrolly=tk.Scrollbar(treeview_frame,orient=VERTICAL)
#     scrollx=tk.Scrollbar(treeview_frame,orient=HORIZONTAL) 
#     treeview=ttk.Treeview(treeview_frame,columns=('id','category','supplier','name','price','quantity','status'),show='headings',yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
#     scrolly.pack(side=RIGHT,fill=Y)
#     scrollx.pack(side=BOTTOM,fill=X)
#     scrollx.config(command=treeview.xview)
#     scrolly.config(command=treeview.yview)
#     treeview.pack(fill=BOTH, expand=1)

#     treeview.heading('id',text='Id')
#     treeview.heading('category',text='Category')
#     treeview.heading('supplier',text='Supplier')
#     treeview.heading('name',text='Product Name')
#     treeview.heading('price',text='Price')
#     treeview.heading('quantity',text='Quantity')
#     treeview.heading('status',text='Status')
#     fetch_supplier_category(category_combobox,supplier_combobox)




import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage, RIDGE, VERTICAL, HORIZONTAL, BOTTOM, RIGHT, BOTH, X, Y, END
from employee import connect_database  # Ensure this module provides a valid database connection


# Function to populate the TreeView
def treeview_data(treeview):
    cursor, connection = connect_database()
    if not cursor or not connection:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return
    try:
        cursor.execute('USE inventory_system')
        cursor.execute('SELECT * FROM product_data')
        records = cursor.fetchall()

        # Clear existing TreeView data
        treeview.delete(*treeview.get_children())
        
        # Add records to the TreeView
        for record in records:
            treeview.insert('', END, values=record)  # Populate each record

    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        connection.close()



# Function to fetch options for category and supplier
def fetch_supplier_category(category_combobox, supplier_combobox):
    category_options = []
    supplier_options = []
    cursor, connection = connect_database()
    if not cursor or not connection:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    try:
        cursor.execute('USE inventory_system')
        
        # Fetch categories
        cursor.execute('SELECT name FROM category_data')
        category_options = [name[0] for name in cursor.fetchall()]
        category_combobox.config(values=category_options)
        
        # Fetch suppliers
        cursor.execute('SELECT name FROM supplier_data')
        supplier_options = [name[0] for name in cursor.fetchall()]
        supplier_combobox.config(values=supplier_options)

    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        connection.close()


# Function to add data
def add_data(category, supplier, name, price, quantity, status, treeview):
    if category == 'Select':
        messagebox.showerror('Error', 'Please select a valid category.')
    elif supplier == 'Select':
        messagebox.showerror('Error', 'Please select a valid supplier.')
    elif not name or not price or not quantity or status == 'Select Status':
        messagebox.showerror('Error', 'All fields are required.')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            messagebox.showerror("Error", "Failed to connect to the database.")
            return

        try:
            cursor.execute('USE inventory_system')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS product_data(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    category VARCHAR(100),
                    supplier VARCHAR(100),
                    name VARCHAR(100),
                    price DECIMAL(10,2),
                    quantity INT,
                    status VARCHAR(50)
                )
            ''')
            cursor.execute(
                'INSERT INTO product_data (category, supplier, name, price, quantity, status) VALUES (%s, %s, %s, %s, %s, %s)',
                (category, supplier, name, float(price), int(quantity), status)
            )
            connection.commit()
            messagebox.showinfo('Success', 'Data is added successfully.')
            treeview_data(treeview)

        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()


# Function to update data in the TreeView and database
def update_data(category, supplier, name, price, quantity, status, treeview):
    # Check if a record is selected
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror('Error', 'No record selected for update.')
        return

    # Validate price and quantity inputs
    if not price or not quantity:
        messagebox.showerror('Error', 'Price and Quantity cannot be empty.')
        return

    try:
        price = float(price)  # Ensure price is a valid float
    except ValueError:
        messagebox.showerror('Error', 'Price must be a valid number.')
        return

    try:
        quantity = int(quantity)  # Ensure quantity is a valid integer
    except ValueError:
        messagebox.showerror('Error', 'Quantity must be a valid whole number.')
        return

    # Validate all other fields
    if category == 'Select':
        messagebox.showerror('Error', 'Please select a valid category.')
        return
    if supplier == 'Select':
        messagebox.showerror('Error', 'Please select a valid supplier.')
        return
    if not name or status == 'Select Status':
        messagebox.showerror('Error', 'All fields are required.')
        return

    # Proceed with database update
    new_values = (category, supplier, name, price, quantity, status)
    item_id = treeview.item(selected_item[0], 'values')[0]  # Fetch the ID of the selected row

    cursor, connection = connect_database()
    if not cursor or not connection:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    try:
        cursor.execute('USE inventory_system')
        cursor.execute(
            'UPDATE product_data SET category=%s, supplier=%s, name=%s, price=%s, quantity=%s, status=%s WHERE id=%s',
            (*new_values, item_id)
        )
        connection.commit()
        messagebox.showinfo('Success', 'Data updated successfully.')
        treeview_data(treeview)
    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        connection.close()



# Function to delete selected record
def delete_data(treeview):
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror('Error', 'No record selected for deletion.')
        return

    item_id = treeview.item(selected_item[0], 'values')[0]  # Fetch the ID of the selected row

    cursor, connection = connect_database()
    if not cursor or not connection:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    try:
        cursor.execute('USE inventory_system')
        cursor.execute('DELETE FROM product_data WHERE id=%s', (item_id,))
        connection.commit()
        messagebox.showinfo('Success', 'Record deleted successfully.')
        treeview_data(treeview)
    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        connection.close()


# Function to clear all input fields
def clear_fields(category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox):
    category_combobox.set('Select')
    supplier_combobox.set('Select')
    name_entry.delete(0, END)
    price_entry.delete(0, END)
    quantity_entry.delete(0, END)
    status_combobox.set('Select Status')


# Function to search for records
def search_data(search_by, search_value, treeview):
    if search_by == 'Search By' or not search_value.strip():
        messagebox.showerror('Error', 'Please select a valid search field and enter a value.')
        return

    cursor, connection = connect_database()
    if not cursor or not connection:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    try:
        cursor.execute('USE inventory_system')
        query = f"SELECT * FROM product_data WHERE {search_by.lower()} LIKE %s"
        cursor.execute(query, (f"%{search_value.strip()}%",))
        records = cursor.fetchall()

        treeview.delete(*treeview.get_children())
        for record in records:
            treeview.insert('', END, values=record)
    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        connection.close()


# Button Integration
# def product_form(root):
#     product_frame = tk.Frame(root, width=1070, height=567, bg='white')
#     product_frame.place(x=200, y=100)

#     # Back button setup
#     back_image = PhotoImage(file='back.png')
#     back_button = tk.Button(product_frame, image=back_image, bd=0, cursor='hand2', bg='white', 
#                             command=lambda: product_frame.place_forget())
#     back_button.image = back_image
#     back_button.place(x=10, y=30)

#     # Left frame setup
#     left_frame = tk.Frame(product_frame, bg='white', bd=2, relief=RIDGE)
#     left_frame.place(x=20, y=60)

#     # Form Labels and Entry Widgets
#     tk.Label(left_frame, text='Manage Product Details', font=('times new roman', 16, 'bold'), bg='#0f4d7d', fg='white').grid(row=0, columnspan=2, sticky='we')

#     category_combobox = ttk.Combobox(left_frame, font=('times new roman', 14, 'bold'), width=15, state='readonly')
#     category_combobox.grid(row=1, column=1, pady=10)
#     category_combobox.set('Select')

#     supplier_combobox = ttk.Combobox(left_frame, font=('times new roman', 14, 'bold'), width=15, state='readonly')
#     supplier_combobox.grid(row=2, column=1, pady=10)
#     supplier_combobox.set('Select')

#     name_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     name_entry.grid(row=3, column=1, pady=10)

#     price_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     price_entry.grid(row=4, column=1, pady=10)

#     quantity_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     quantity_entry.grid(row=5, column=1, pady=10)

#     status_combobox = ttk.Combobox(left_frame, values=['Active', 'Inactive'], font=('times new roman', 14, 'bold'), width=15, state='readonly')
#     status_combobox.grid(row=6, column=1, pady=10)
#     status_combobox.set('Select Status')
def product_form(root):
    product_frame = tk.Frame(root, width=1070, height=567, bg='white')
    product_frame.place(x=200, y=100)

    # Back button setup
    back_image = PhotoImage(file='back.png')
    back_button = tk.Button(product_frame, image=back_image, bd=0, cursor='hand2', bg='white',
                            command=lambda: product_frame.place_forget())
    back_button.image = back_image
    back_button.place(x=10, y=30)

    # Left frame setup
    left_frame = tk.Frame(product_frame, bg='white', bd=2, relief=RIDGE)
    left_frame.place(x=20, y=60)

    # Title Label
    tk.Label(left_frame, text='Manage Product Details', font=('times new roman', 16, 'bold'), bg='#0f4d7d', fg='white').grid(row=0, columnspan=2, sticky='we')

    # CATEGORY
    tk.Label(left_frame, text='Category:', font=('times new roman', 14, 'bold'), bg='white').grid(row=1, column=0, padx=20, sticky='w')
    category_combobox = ttk.Combobox(left_frame, font=('times new roman', 14, 'bold'), width=15, state='readonly')
    category_combobox.grid(row=1, column=1, pady=10)
    category_combobox.set('Select')

    # SUPPLIER
    tk.Label(left_frame, text='Supplier:', font=('times new roman', 14, 'bold'), bg='white').grid(row=2, column=0, padx=20, sticky='w')
    supplier_combobox = ttk.Combobox(left_frame, font=('times new roman', 14, 'bold'), width=15, state='readonly')
    supplier_combobox.grid(row=2, column=1, pady=10)
    supplier_combobox.set('Select')

    # NAME
    tk.Label(left_frame, text='Product Name:', font=('times new roman', 14, 'bold'), bg='white').grid(row=3, column=0, padx=20, sticky='w')
    name_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    name_entry.grid(row=3, column=1, pady=10)

    # PRICE
    tk.Label(left_frame, text='Price:', font=('times new roman', 14, 'bold'), bg='white').grid(row=4, column=0, padx=20, sticky='w')
    price_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    price_entry.grid(row=4, column=1, pady=10)

    # QUANTITY
    tk.Label(left_frame, text='Quantity:', font=('times new roman', 14, 'bold'), bg='white').grid(row=5, column=0, padx=20, sticky='w')
    quantity_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    quantity_entry.grid(row=5, column=1, pady=10)

    # STATUS
    tk.Label(left_frame, text='Status:', font=('times new roman', 14, 'bold'), bg='white').grid(row=6, column=0, padx=20, sticky='w')
    status_combobox = ttk.Combobox(left_frame, values=['Active', 'Inactive'], font=('times new roman', 14, 'bold'), width=15, state='readonly')
    status_combobox.grid(row=6, column=1, pady=10)
    status_combobox.set('Select Status')


    # Buttons for actions
    button_frame = tk.Frame(left_frame, bg='white')
    button_frame.grid(row=7, columnspan=2, pady=20)

    add_button = tk.Button(button_frame, text='Add', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                           command=lambda: add_data(
                               category_combobox.get(), supplier_combobox.get(),
                               name_entry.get(), price_entry.get(),
                               quantity_entry.get(), status_combobox.get(), treeview))
    add_button.grid(row=0, column=0, padx=10)

    update_button = tk.Button(button_frame, text='Update', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                              command=lambda: update_data(
                                  category_combobox.get(), supplier_combobox.get(),
                                  name_entry.get(), price_entry.get(),
                                  quantity_entry.get(), status_combobox.get(), treeview))
    update_button.grid(row=0, column=1, padx=10)

    clear_button = tk.Button(button_frame, text='Clear', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                             command=lambda: clear_fields(
                                 category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox))
    clear_button.grid(row=0, column=2, padx=10)

    delete_button = tk.Button(button_frame, text='Delete', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                              command=lambda: delete_data(treeview))
    delete_button.grid(row=0, column=3, padx=10)

    # Search Frame and Buttons
    search_frame = tk.LabelFrame(product_frame, text='Search Product', font=('times new roman', 14))
    search_frame.place(x=500, y=10)

    search_combobox = ttk.Combobox(search_frame, values=('category', 'supplier', 'name', 'status'), state='readonly', width=16, font=('times new roman', 14))
    search_combobox.grid(row=0, column=0, padx=10)
    search_combobox.set('Search By')

    search_entry = tk.Entry(search_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    search_entry.grid(row=0, column=1)

    search_button = tk.Button(search_frame, text='Search', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                              command=lambda: search_data(search_combobox.get(), search_entry.get(), treeview))
    search_button.grid(row=0, column=2, padx=(10, 0), pady=10)

    show_button = tk.Button(search_frame, text='Show All', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                            command=lambda: treeview_data(treeview))
    show_button.grid(row=0, column=3, padx=10)

    # Treeview Setup (unchanged)
    treeview_frame = tk.Frame(product_frame)
    treeview_frame

# Function to display the product form
# def product_form(root):
#     product_frame = tk.Frame(root, width=1070, height=567, bg='white')
#     product_frame.place(x=200, y=100)

#     # Back button setup
#     back_image = PhotoImage(file='back.png')
#     back_button = tk.Button(product_frame, image=back_image, bd=0, cursor='hand2', bg='white', 
#                             command=lambda: product_frame.place_forget())
#     back_button.image = back_image
#     back_button.place(x=10, y=30)

#     # Left frame setup
#     left_frame = tk.Frame(product_frame, bg='white', bd=2, relief=RIDGE)
#     left_frame.place(x=20, y=60)

#     # Form Labels and Entry Widgets
#     tk.Label(left_frame, text='Manage Product Details', font=('times new roman', 16, 'bold'), bg='#0f4d7d', fg='white').grid(row=0, columnspan=2, sticky='we')

#     labels = ['Category', 'Supplier', 'Name', 'Price', 'Quantity', 'Status']
#     entries = []

#     for idx, label in enumerate(labels):
#         tk.Label(left_frame, text=label, font=('times new roman', 14, 'bold'), bg='white').grid(row=idx + 1, column=0, padx=20, sticky='w')

#     category_combobox = ttk.Combobox(left_frame, font=('times new roman', 14, 'bold'), width=15, state='readonly')
#     category_combobox.grid(row=1, column=1, pady=10)
#     category_combobox.set('Select')

#     supplier_combobox = ttk.Combobox(left_frame, font=('times new roman', 14, 'bold'), width=15, state='readonly')
#     supplier_combobox.grid(row=2, column=1, pady=10)
#     supplier_combobox.set('Select')

#     name_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     name_entry.grid(row=3, column=1, pady=10)

#     price_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     price_entry.grid(row=4, column=1, pady=10)

#     quantity_entry = tk.Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     quantity_entry.grid(row=5, column=1, pady=10)

#     status_combobox = ttk.Combobox(left_frame, values=['Active', 'Inactive'], font=('times new roman', 14, 'bold'), width=15, state='readonly')
#     status_combobox.grid(row=6, column=1, pady=10)
#     status_combobox.set('Select Status')

#     # Add Buttons
#     button_frame = tk.Frame(left_frame, bg='white')
#     button_frame.grid(row=7, columnspan=2, pady=20)

#     add_button = tk.Button(button_frame, text='Add', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
#                            command=lambda: add_data(
#                                category_combobox.get(), supplier_combobox.get(),
#                                name_entry.get(), price_entry.get(),
#                                quantity_entry.get(), status_combobox.get(), treeview))
#     add_button.grid(row=0, column=0, padx=10)

#     # Search Frame
#     search_frame = tk.LabelFrame(product_frame, text='Search Product', font=('times new roman', 14))
#     search_frame.place(x=500, y=10)

    treeview_frame = tk.Frame(product_frame)
    treeview_frame.place(x=480, y=125, width=570, height=430)

    scrolly = tk.Scrollbar(treeview_frame, orient=VERTICAL)
    scrollx = tk.Scrollbar(treeview_frame, orient=HORIZONTAL)

    treeview = ttk.Treeview(
        treeview_frame,
        columns=('id', 'category', 'supplier', 'name', 'price', 'quantity', 'status'),
        show='headings',
        yscrollcommand=scrolly.set,
        xscrollcommand=scrollx.set
    )

    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.pack(side=BOTTOM, fill=X)
    scrolly.config(command=treeview.yview)
    scrollx.config(command=treeview.xview)
    treeview.pack(fill=BOTH, expand=True)

    # Configure column headings
    treeview.heading('id', text='ID')
    treeview.heading('category', text='Category')
    treeview.heading('supplier', text='Supplier')
    treeview.heading('name', text='Product Name')
    treeview.heading('price', text='Price')
    treeview.heading('quantity', text='Quantity')
    treeview.heading('status', text='Status')

    for col in ('id', 'category', 'supplier', 'name', 'price', 'quantity', 'status'):
        treeview.column(col, width=100)

    # Load TreeView data when the product_form is initialized
    treeview_data(treeview)

    # Populate Comboboxes with Data
    fetch_supplier_category(category_combobox, supplier_combobox)








# import tkinter as tk
# from tkinter import ttk
# from tkinter import PhotoImage,RIDGE


# def product_form(root):
#     global back_image,logo
#     product_frame = tk.Frame(root, width=1070,height=567, bg='white')
#     product_frame.place(x=200, y=100)

#     back_image = PhotoImage(file='back.png')

#     back_button = tk.Button(product_frame, image=back_image, bd=0, cursor='hand2',bg='white', command=lambda: product_frame.place_forget())

#     back_button.place(x=10, y=30)

#     left_frame =tk.Frame(product_frame, bg='white',bd=2,relief=RIDGE)
#     left_frame.place(x=20, y=60)
    

#     heading_label=tk.Label(left_frame, text='Manage product Details',font=('times new roman', 16, 'bold'), bg='#0f4d7d',fg='white')
#     heading_label.grid(row=0,columnspan=2,sticky='we')

#     category_label=tk.Label(left_frame,text='Category',font=('times new roman',14,'bold'),bg='white')
#     category_label.grid(row=1,column=0,padx=20,sticky='w')

#     category_combobox=ttk.Combobox(left_frame,font=('times new roman',14,'bold'),width=10,state='readonly')
#     category_combobox.grid(row=1,column=1,pady=20)
#     category_combobox.set('select')


#     supplier_label=tk.Label(left_frame,text='Supplier',font=('times new roman',14,'bold'),bg='white')
#     supplier_label.grid(row=2,column=0,padx=20,sticky='w')

#     supplier_combobox=ttk.Combobox(left_frame,font=('times new roman',14,'bold'),width=10,state='readonly')
#     supplier_combobox.grid(row=2,column=1)
#     supplier_combobox.set('select')


#     name_label=tk.Label(left_frame,text='Name',font=('times new roman',14,'bold'),bg='white')
#     name_label.grid(row=3,column=0,padx=20,sticky='w')
#     name_entry=tk.Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
#     name_entry.grid(row=3,column=1,pady=20)

#     price_label=tk.Label(left_frame,text='Price',font=('times new roman',14,'bold'),bg='white')
#     price_label.grid(row=4,column=0,padx=20,sticky='w')
#     price_entry=tk.Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
#     price_entry.grid(row=4,column=1)


#     quantity_label=tk.Label(left_frame,text='Quantity',font=('times new roman',14,'bold'),bg='white')
#     quantity_label.grid(row=5,column=0,padx=20,sticky='w')
#     quantity_entry=tk.Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
#     quantity_entry.grid(row=5,column=1,pady=20)


#     status_label=tk.Label(left_frame,text='Status',font=('times new roman',14,'bold'),bg='white')
#     status_label.grid(row=6,column=0,padx=20,sticky='w')

#     status_combobox=ttk.Combobox(left_frame,values=('Active','Inactive'),font=('times new roman',14,'bold'),width=10,state='readonly')
#     status_combobox.grid(row=6,column=1)
#     status_combobox.set('select status')


#     button_frame=tk.Button(left_frame,bg='white')
#     button_frame.grid(row=7,columnspan=2,pady=(30,10))

#     add_button=tk.Button(button_frame, text='Add', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d')
#     add_button.grid(row=0,column=0,padx=10)

#     update_button=tk.Button(button_frame, text='Update', font=('times new roman',14), width=8, cursor='hand2',fg='white',bg='#0f4d7d')
#     update_button.grid(row=0,column=1,padx=10)

#     clear_button = tk.Button(button_frame, text='Clear', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d')
#     clear_button.grid(row=0, column=2, padx=10)

#     delete_button = tk.Button(button_frame, text='Delete', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d')
#     delete_button.grid(row=0, column=3, padx=10)


#     search_frame = tk.LabelFrame(product_frame, text='Search Product', font=('times new roman', 14))
#     search_frame.place(x=480, y=40)

#     search_combobox = ttk.Combobox(search_frame,values=('category', 'supplier', 'Name', 'Status'),state='readonly',width=16,font=('times new roman', 14))
#     search_combobox.grid(row=0, column=0)

#     search_entry = tk.Entry(search_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
#     search_entry.grid(row=0, column=1)










