import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage, RIDGE, VERTICAL, HORIZONTAL, BOTTOM, RIGHT, BOTH, X, Y, END
from employee import connect_database




def sale_form(root):
    sale_frame = tk.Frame(root, width=1070, height=567, bg='white')
    sale_frame.place(x=200, y=100)


    heading_label=tk.Label(sale_frame, text='Customer Bill And Sales Analysis',font=('times new roman', 16, 'bold'), bg='#0f4d7d',fg='white')
    heading_label.place(x=0, y=0, relwidth=1)

    # Back button setup
    back_image = PhotoImage(file='back.png')
    back_button = tk.Button(sale_frame, image=back_image, bd=0, cursor='hand2', bg='white',
                            command=lambda: sale_frame.place_forget())
    back_button.image = back_image
    back_button.place(x=10, y=30)

    left_frame = tk.Frame(sale_frame, bg='#d1d8e0', bd=2, relief='ridge')
    left_frame.place(x=0, y=50, width=200, height=500)
    purchase_label = tk.Label(left_frame, text="Purchases", font=('times new roman', 16), bg='#009688', fg='white')
    purchase_label.pack(fill=tk.X)
    purchase_list = tk.Listbox(left_frame, font=('times new roman', 14))
    purchase_list.pack(fill=tk.BOTH, expand=True)
    # Populate this Listbox with your purchase data (e.g., from a database).

    # Center Frame (Invoice Details & Customer Billing Area)
    center_frame = tk.Frame(sale_frame, bg='#f7f1e3', bd=2, relief='ridge')
    center_frame.place(x=200, y=50, width=470, height=500)

    # Invoice Number and Search
    invoice_label = tk.Label(center_frame, text="Invoice Number:", font=('times new roman', 16, 'bold'), bg='#f7f1e3', fg='black')
    invoice_label.pack(anchor='nw', padx=10, pady=10)
    invoice_entry = tk.Entry(center_frame, font=('times new roman', 14), width=30)
    invoice_entry.pack(anchor='nw', padx=10, pady=5)

    search_button = tk.Button(center_frame, text="Search Bill", font=('times new roman', 14), bg='#16a085', fg='white')
    search_button.pack(anchor='nw', padx=10, pady=5)

    # Customer Billing Area
    billing_label = tk.Label(center_frame, text="Customer Billing Area", font=('times new roman', 16, 'bold'), bg='#f7f1e3', fg='black')
    billing_label.pack(anchor='nw', padx=10, pady=20)
    billing_area = tk.Text(center_frame, font=('times new roman', 14), height=15, width=50)
    billing_area.pack(padx=10, pady=5)
    # Populate this Text widget with invoice details when an invoice is clicked in the Listbox.

    # Right Frame (Sales Analysis)
    right_frame = tk.Frame(sale_frame, bg='#d1d8e0', bd=2, relief='ridge')
    right_frame.place(x=670, y=50, width=400, height=500)

    analysis_label = tk.Label(right_frame, text="Sales Analysis", font=('times new roman', 16), bg='#9b59b6', fg='white')
    analysis_label.pack(fill=tk.X)

    # Filtering Options
    date_label = tk.Label(right_frame, text="Select Date:", font=('times new roman', 14), bg='#d1d8e0', fg='black')
    date_label.pack(anchor='nw', padx=10, pady=10)
    date_entry = tk.Entry(right_frame, font=('times new roman', 14), width=20)
    date_entry.pack(anchor='nw', padx=10, pady=5)

    sort_label = tk.Label(right_frame, text="Sorting Option:", font=('times new roman', 14), bg='#d1d8e0', fg='black')
    sort_label.pack(anchor='nw', padx=10, pady=10)
    sort_combobox = ttk.Combobox(right_frame, font=('times new roman', 14), values=["Highest Sales", "Lowest Sales", "By Product"])
    sort_combobox.pack(anchor='nw', padx=10, pady=5)

    # Total Sales Display
    total_sales_label = tk.Label(right_frame, text="Total Sales: 138060.00", font=('times new roman', 14, 'bold'), bg='#d1d8e0', fg='black')
    total_sales_label.pack(anchor='nw', padx=10, pady=10)

    # Product Breakdown Table (optional)
    product_table = ttk.Treeview(right_frame, columns=("Product", "Quantity", "Amount"), show='headings', height=10)
    product_table.heading("Product", text="Product Name")
    product_table.heading("Quantity", text="Quantity Sold")
    product_table.heading("Amount", text="Amount")
    product_table.pack(fill=tk.BOTH, padx=10, pady=10)
    # Populate this Treeview with your sales data.

# Additional logic to connect to database and populate widgets is required.






    # the left_frame shows list all the purchase, the centre_frame has the text area for invoice no. and a search button for the searching the bill 
    # down the search button there is customer billing area whereby when one clicks on the invoice on the left_frame, appears onnthe customer bill area and on the right 