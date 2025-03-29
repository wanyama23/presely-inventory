import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage, BOTH, END
import pymysql


# Database connection function
def connect_database():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",  # Replace with your database password
            database="inventory_system"  # Replace with your database name
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


# Function to populate the purchase list
def populate_purchases(listbox):
    connection = connect_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT purchase_id, item_name FROM purchases")  # Adjust query
            rows = cursor.fetchall()
            for row in rows:
                listbox.insert(tk.END, f"{row[0]} - {row[1]}")
        except pymysql.err.ProgrammingError as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            connection.close()



# Function to search for an invoice
def search_invoice(invoice_number, billing_area):
    connection = connect_database()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM invoices WHERE invoice_number = %s"  # Adjust query to match schema
            cursor.execute(query, (invoice_number,))
            invoice_data = cursor.fetchone()
            if invoice_data:
                billing_area.delete("1.0", tk.END)
                billing_area.insert(tk.END, f"Invoice Number: {invoice_data[1]}\n")
                billing_area.insert(tk.END, f"Customer Name: {invoice_data[2]}\n")
                billing_area.insert(tk.END, f"Date: {invoice_data[3]}\n")
                billing_area.insert(tk.END, f"Items: {invoice_data[4]}\n")
                billing_area.insert(tk.END, f"Total Amount: {invoice_data[5]}\n")
            else:
                messagebox.showinfo("Search Result", "Invoice not found.")
        except pymysql.err.ProgrammingError as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            connection.close()



# Function to populate the sales analysis table
def populate_sales_table(table):
    connection = connect_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT product_name, quantity_sold, total_amount FROM sales")  # Query
            rows = cursor.fetchall()
            for row in rows:
                table.insert("", tk.END, values=(row[0], row[1], row[2]))
        except pymysql.err.ProgrammingError as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            connection.close()



# Function to filter sales data
def filter_sales(date, sorting_option, table):
    connection = connect_database()
    if connection:
        cursor = connection.cursor()
        if sorting_option == "Highest Sales":
            query = "SELECT product_name, quantity_sold, total_amount FROM sales WHERE date = %s ORDER BY total_amount DESC"
        elif sorting_option == "Lowest Sales":
            query = "SELECT product_name, quantity_sold, total_amount FROM sales WHERE date = %s ORDER BY total_amount ASC"
        elif sorting_option == "By Product":
            query = "SELECT product_name, quantity_sold, total_amount FROM sales WHERE date = %s ORDER BY product_name"
        else:
            query = "SELECT product_name, quantity_sold, total_amount FROM sales WHERE date = %s"

        cursor.execute(query, (date,))
        rows = cursor.fetchall()
        table.delete(*table.get_children())  # Clear existing rows
        for row in rows:
            table.insert("", tk.END, values=(row[0], row[1], row[2]))
        connection.close()


# Main sale form function
def sale_form(root):
    sale_frame = tk.Frame(root, width=1070, height=567, bg='white')
    sale_frame.place(x=200, y=100)

    # Heading label
    heading_label = tk.Label(sale_frame, text='Customer Bill And Sales Analysis',
                             font=('times new roman', 16, 'bold'), bg='#0f4d7d', fg='white')
    heading_label.place(x=0, y=0, relwidth=1)

    # Back button
    back_image = PhotoImage(file='back.png')
    back_button = tk.Button(sale_frame, image=back_image, bd=0, cursor='hand2', bg='white',
                            command=lambda: sale_frame.place_forget())
    back_button.image = back_image
    back_button.place(x=10, y=30)

    # Left frame (Purchases)
    left_frame = tk.Frame(sale_frame, bg='#d1d8e0', bd=2, relief='ridge')
    left_frame.place(x=0, y=50, width=200, height=500)
    purchase_label = tk.Label(left_frame, text="Purchases", font=('times new roman', 16), bg='#009688', fg='white')
    purchase_label.pack(fill=tk.X)
    purchase_list = tk.Listbox(left_frame, font=('times new roman', 14))
    purchase_list.pack(fill=tk.BOTH, expand=True)
    populate_purchases(purchase_list)  # Populate purchase data

    # Center frame (Invoice Details & Billing)
    center_frame = tk.Frame(sale_frame, bg='#f7f1e3', bd=2, relief='ridge')
    center_frame.place(x=200, y=50, width=470, height=500)

    invoice_label = tk.Label(center_frame, text="Invoice Number:", font=('times new roman', 16, 'bold'),
                             bg='#f7f1e3', fg='black')
    invoice_label.pack(anchor='nw', padx=10, pady=10)
    invoice_entry = tk.Entry(center_frame, font=('times new roman', 14), width=30)
    invoice_entry.pack(anchor='nw', padx=10, pady=5)

    search_button = tk.Button(center_frame, text="Search Bill", font=('times new roman', 14), bg='#16a085', fg='white',
                               command=lambda: search_invoice(invoice_entry.get(), billing_area))
    search_button.pack(anchor='nw', padx=10, pady=5)

    billing_label = tk.Label(center_frame, text="Customer Billing Area", font=('times new roman', 16, 'bold'),
                             bg='#f7f1e3', fg='black')
    billing_label.pack(anchor='nw', padx=10, pady=20)
    billing_area = tk.Text(center_frame, font=('times new roman', 14), height=15, width=50)
    billing_area.pack(padx=10, pady=5)

    # Right frame (Sales Analysis)
    right_frame = tk.Frame(sale_frame, bg='#d1d8e0', bd=2, relief='ridge')
    right_frame.place(x=670, y=50, width=400, height=500)

    analysis_label = tk.Label(right_frame, text="Sales Analysis", font=('times new roman', 16), bg='#9b59b6', fg='white')
    analysis_label.pack(fill=tk.X)

    date_label = tk.Label(right_frame, text="Select Date:", font=('times new roman', 14), bg='#d1d8e0', fg='black')
    date_label.pack(anchor='nw', padx=10, pady=10)
    date_entry = tk.Entry(right_frame, font=('times new roman', 14), width=20)
    date_entry.pack(anchor='nw', padx=10, pady=5)

    sort_label = tk.Label(right_frame, text="Sorting Option:", font=('times new roman', 14), bg='#d1d8e0', fg='black')
    sort_label.pack(anchor='nw', padx=10, pady=10)
    sort_combobox = ttk.Combobox(right_frame, font=('times new roman', 14),
                                  values=["Highest Sales", "Lowest Sales", "By Product"])
    sort_combobox.pack(anchor='nw', padx=10, pady=5)

    total_sales_label = tk.Label(right_frame, text="Total Sales: 138060.00", font=('times new roman', 14, 'bold'),
                                 bg='#d1d8e0', fg='black')
    total_sales_label.pack(anchor='nw', padx=10, pady=10)

    product_table = ttk.Treeview(right_frame, columns=("Product", "Quantity", "Amount"), show='headings', height=10)
    product_table.heading("Product", text="Product Name")
    product_table.heading("Quantity", text="Quantity Sold")
    product_table.heading("Amount", text="Amount")
    product_table.pack(fill=tk.BOTH, padx=10, pady=10)
    populate_sales_table(product_table)  # Populate sales data

    # Bind filter sales functionality
    date_entry.bind("<Return>", lambda event: filter_sales(date_entry.get(), sort_combobox.get(), product_table))











# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from tkinter import PhotoImage, RIDGE, VERTICAL, HORIZONTAL, BOTTOM, RIGHT, BOTH, X, Y, END
# from employee import connect_database




# def sale_form(root):
#     sale_frame = tk.Frame(root, width=1070, height=567, bg='white')
#     sale_frame.place(x=200, y=100)


#     heading_label=tk.Label(sale_frame, text='Customer Bill And Sales Analysis',font=('times new roman', 16, 'bold'), bg='#0f4d7d',fg='white')
#     heading_label.place(x=0, y=0, relwidth=1)

#     # Back button setup
#     back_image = PhotoImage(file='back.png')
#     back_button = tk.Button(sale_frame, image=back_image, bd=0, cursor='hand2', bg='white',
#                             command=lambda: sale_frame.place_forget())
#     back_button.image = back_image
#     back_button.place(x=10, y=30)

#     left_frame = tk.Frame(sale_frame, bg='#d1d8e0', bd=2, relief='ridge')
#     left_frame.place(x=0, y=50, width=200, height=500)
#     purchase_label = tk.Label(left_frame, text="Purchases", font=('times new roman', 16), bg='#009688', fg='white')
#     purchase_label.pack(fill=tk.X)
#     purchase_list = tk.Listbox(left_frame, font=('times new roman', 14))
#     purchase_list.pack(fill=tk.BOTH, expand=True)
#     # Populate this Listbox with your purchase data (e.g., from a database).

#     # Center Frame (Invoice Details & Customer Billing Area)
#     center_frame = tk.Frame(sale_frame, bg='#f7f1e3', bd=2, relief='ridge')
#     center_frame.place(x=200, y=50, width=470, height=500)

#     # Invoice Number and Search
#     invoice_label = tk.Label(center_frame, text="Invoice Number:", font=('times new roman', 16, 'bold'), bg='#f7f1e3', fg='black')
#     invoice_label.pack(anchor='nw', padx=10, pady=10)
#     invoice_entry = tk.Entry(center_frame, font=('times new roman', 14), width=30)
#     invoice_entry.pack(anchor='nw', padx=10, pady=5)

#     search_button = tk.Button(center_frame, text="Search Bill", font=('times new roman', 14), bg='#16a085', fg='white')
#     search_button.pack(anchor='nw', padx=10, pady=5)

#     # Customer Billing Area
#     billing_label = tk.Label(center_frame, text="Customer Billing Area", font=('times new roman', 16, 'bold'), bg='#f7f1e3', fg='black')
#     billing_label.pack(anchor='nw', padx=10, pady=20)
#     billing_area = tk.Text(center_frame, font=('times new roman', 14), height=15, width=50)
#     billing_area.pack(padx=10, pady=5)
#     # Populate this Text widget with invoice details when an invoice is clicked in the Listbox.

#     # Right Frame (Sales Analysis)
#     right_frame = tk.Frame(sale_frame, bg='#d1d8e0', bd=2, relief='ridge')
#     right_frame.place(x=670, y=50, width=400, height=500)

#     analysis_label = tk.Label(right_frame, text="Sales Analysis", font=('times new roman', 16), bg='#9b59b6', fg='white')
#     analysis_label.pack(fill=tk.X)

#     # Filtering Options
#     date_label = tk.Label(right_frame, text="Select Date:", font=('times new roman', 14), bg='#d1d8e0', fg='black')
#     date_label.pack(anchor='nw', padx=10, pady=10)
#     date_entry = tk.Entry(right_frame, font=('times new roman', 14), width=20)
#     date_entry.pack(anchor='nw', padx=10, pady=5)

#     sort_label = tk.Label(right_frame, text="Sorting Option:", font=('times new roman', 14), bg='#d1d8e0', fg='black')
#     sort_label.pack(anchor='nw', padx=10, pady=10)
#     sort_combobox = ttk.Combobox(right_frame, font=('times new roman', 14), values=["Highest Sales", "Lowest Sales", "By Product"])
#     sort_combobox.pack(anchor='nw', padx=10, pady=5)

#     # Total Sales Display
#     total_sales_label = tk.Label(right_frame, text="Total Sales: 138060.00", font=('times new roman', 14, 'bold'), bg='#d1d8e0', fg='black')
#     total_sales_label.pack(anchor='nw', padx=10, pady=10)

#     # Product Breakdown Table (optional)
#     product_table = ttk.Treeview(right_frame, columns=("Product", "Quantity", "Amount"), show='headings', height=10)
#     product_table.heading("Product", text="Product Name")
#     product_table.heading("Quantity", text="Quantity Sold")
#     product_table.heading("Amount", text="Amount")
#     product_table.pack(fill=tk.BOTH, padx=10, pady=10)
    # Populate this Treeview with your sales data.

# Additional logic to connect to database and populate widgets is required.






    # the left_frame shows list all the purchase, the centre_frame has the text area for invoice no. and a search button for the searching the bill 
    # down the search button there is customer billing area whereby when one clicks on the invoice on the left_frame, appears onnthe customer bill area and on the right 