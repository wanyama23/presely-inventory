import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox
from datetime import datetime
import pymysql  # MySQL database connector
import os

# === Database Connection ===
def connect_database():
    """Connect to MySQL database."""
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="inventory_system"
        )
        return connection
    except Exception as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return None

# === Fetch Products from Database ===
def fetch_products():
    conn = connect_database()
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, quantity FROM product_data")  
        records = cursor.fetchall()
        conn.close()
        return records
    except Exception as e:
        messagebox.showerror("Database Error", f"Error fetching products: {e}")
        return []

# === Populate Product List in UI ===
def populate_product_list():
    product_table.delete(*product_table.get_children())  # Clear previous entries
    products = fetch_products()

    if not products:
        messagebox.showwarning("No Data", "No products found in the database!")
        return

    for product in products:
        product_table.insert("", "end", values=product)

# === Update Date and Time Dynamically ===
def update_datetime(subtitle_label):
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%H:%M:%S %p")
    subtitle_label.config(text=f"Welcome \t\t Date: {current_date}\t\t Time: {current_time}")
    subtitle_label.after(1000, update_datetime, subtitle_label)
    

# === Handle Product Selection ===
def on_product_select(event):
    """Updates entry fields with the selected product details."""
    selected_item = product_table.selection()  # Get selected row(s)

    if selected_item:
        product_data = product_table.item(selected_item[0], "values")  # Get first selected row's values

        product_id.set(product_data[0])  # Store Product ID
        name_entry.delete(0, tk.END)
        name_entry.insert(0, product_data[1])  # Product name
        
        price_entry.delete(0, tk.END)
        price_entry.insert(0, product_data[2])  # Base price

        stock_label.config(text=f"In Stock: {product_data[3]}")  # Update stock availability

        update_price(None)  # Ensure price updates when product is selected

# === Update Price Based on Quantity ===
def update_price(event):
    """Updates price dynamically based on the quantity entered."""
    global total_price_label  # Mark as global

    try:
        unit_price = float(price_entry.get())
        quantity = int(quantity_entry.get()) if quantity_entry.get() else 1
        total_price = unit_price * quantity
        total_price_label.set(f"Total Price: {total_price:.2f}")  # Use .set() instead of .config()
    except ValueError:
        total_price_label.set("Total Price: 0.00")


# === Add Product to Cart ===
def add_to_cart():
    """Adds selected product to the cart."""
    if not name_entry.get() or not price_entry.get() or not quantity_entry.get():
        messagebox.showwarning("Input Error", "Please select a product and enter quantity!")
        return
    
    total_price = float(price_entry.get()) * float(quantity_entry.get())  # Compute total price
    cart_table.insert("", "end", values=(product_id.get(), name_entry.get(), quantity_entry.get(), f"{total_price:.2f}"))
    messagebox.showinfo("Cart", "Product added to cart successfully!")

def generate_bill():
    """Generates and displays a billing receipt in the Customer Billing Area."""
    if not name_entry.get() or not phone_entry.get():
        messagebox.showwarning("Missing Details", "Please enter customer name and phone number!")
        return

    # Get cart items
    cart_items = cart_table.get_children()
    if not cart_items:
        messagebox.showwarning("Empty Cart", "No products in the cart!")
        return

    # ✅ Correctly format receipt with customer details
    customer_name = name_entry.get()
    phone_number = phone_entry.get()

    receipt_text = f"Customer Name: {customer_name}\n"
    receipt_text += f"Phone Number: {phone_number}\n"
    receipt_text += "-"*40 + "\n"
    receipt_text += f"{'Product':<15}{'Qty':<10}{'Price':<10}\n"
    receipt_text += "-"*40 + "\n"

    total_price = 0.0
    sales = []  # Prepare records for database insertion

    for item in cart_items:
        values = cart_table.item(item, "values")
        product_id, product_name, quantity, price = values  # Ensure correct mapping

        receipt_text += f"{product_name:<15}{quantity:<10}{price:<10}\n"
        total_price += float(price)

        # ✅ Save correct customer details to the database
        sales.append((customer_name, phone_number, product_name, quantity, quantity, price, total_price))  # ✅ Corrected this

    receipt_text += "-"*40 + "\n"
    receipt_text += f"Total Amount: Ksh {total_price:.2f}\n"
    receipt_text += "-"*40 + "\n"
    receipt_text += "Thank you for shopping with us!\n"

    # ✅ Display bill correctly in UI
    billing_label.config(text=receipt_text, justify="left", anchor="w")

    # ✅ Save to the database with correct structure
    save_to_sales(sales)

    # ✅ Clear the cart after generating the bill
    # for item in cart_items:
    #     cart_table.delete(item)

    return receipt_text  # Return for printing



 # Return for printing

def print_bill():
    """Handles printing the bill by exporting it to a text file and resets cart & customer details after printing."""
    receipt_content = generate_bill()
    if receipt_content:
        try:
            file_name = f"Receipt_{name_entry.get().replace(' ', '_')}.txt"
            file_path = os.path.join(os.getcwd(), file_name)
            
            with open(file_path, "w") as file:
                file.write(receipt_content)
            
            messagebox.showinfo("Print Successful", f"Receipt saved as {file_name}")

            # ✅ Clear customer details only if printing was successful
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)

            # ✅ Clear the cart only if printing was successful
            for item in cart_table.get_children():
                cart_table.delete(item)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save receipt: {e}")




def save_to_sales(sales):
    """Saves the billing record to the sales database and updates total sales count."""
    conn = connect_database()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        for record in sales:
            cursor.execute("""
    INSERT INTO sales (customer_name, phone_number, product_name, quantity_sold, quantity, price, total_amount, sale_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
""", record)

            # cursor.execute("""
            #     INSERT INTO sales (customer_name, phone_number, product_name, quantity_sold, quantity, price, total_amount)
            #     VALUES (%s, %s, %s, %s, %s, %s, %s)
            # """, record)  # ✅ Ensure correct value count
        
        conn.commit()
        conn.close()
        
        # ✅ Update total sales dynamically after saving transaction
        update_sales_count(total_sales_count_label)
    
    except Exception as e:
        messagebox.showerror("Database Error", f"Error saving sales record: {e}")



def update_sales_count(label):
    """Fetch the total number of sales from the database and update the label."""
    conn = connect_database()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM sales")  # Ensure correct query
        total_sales = cursor.fetchone()[0]
        label.config(text=f"Total Sales: {total_sales}")  # ✅ Update label dynamically
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Error updating total sales: {e}")





# === Show Admin Dashboard ===
def show_dashboard():
    global product_table, bg_image,product_table, cart_table, stock_label, name_entry, price_entry, quantity_entry, product_id, phone_entry, total_price_label, billing_label, sales_label, total_sales_count_label, sales_frame

    root = tk.Tk()
    root.title("Presely Management System")
    root.geometry("1400x668+0+0")
    root.config(bg="white")


    sales_frame = tk.Frame(root, bg='#2c3e50', bd=3, relief='ridge')
    sales_frame.pack()
    # sales_frame.pack(x=600, y=495, height=170, width=280)


    total_sales_count_label = tk.Label(sales_frame, text="Loading...", bg='#8e44ad', fg='white', font=('times new roman', 30, 'bold'))
    total_sales_count_label.pack()

    # update_total_sales()

    # === Load Background Image ===
    try:
        bg_image = PhotoImage(file="inventory(1).png")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load background image. Ensure the file exists. {e}")
        return

    # === Header Section ===
    titleLabel = tk.Label(root, image=bg_image, compound="left", text="  Presely Management System",
                          font=("Times New Roman", 40, "bold"), bg="#010048", fg="white", anchor="w", padx=20)
    titleLabel.place(x=0, y=0, relwidth=1)

    logoutButton = tk.Button(root, text="Logout", font=("Times New Roman", 20, "bold"), fg="#010048",
                             command=root.destroy)
    logoutButton.place(x=1100, y=10)

    subtitleLabel = tk.Label(root, font=("Times New Roman", 15), bg="#4d636d", fg="white")
    subtitleLabel.place(x=0, y=70, relwidth=1)
    update_datetime(subtitleLabel)



    product_id = tk.StringVar()  # Define product_id properly
    total_price_label = tk.StringVar(value="Total Price: 0.00")

    # === Product List Section (Left Side) ===
    productFrame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    productFrame.place(x=10, y=110, width=450, height=500)

    tk.Label(productFrame, text="All Products", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(fill="x", pady=5)

    searchFrame = tk.Frame(productFrame, bg="white")
    searchFrame.pack(fill="x", pady=10)

    tk.Label(searchFrame, text="Product Name:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=10, pady=10)
    search_entry = tk.Entry(searchFrame, font=("Arial", 12))
    search_entry.grid(row=0, column=1, padx=10)

    tk.Button(searchFrame, text="Search", font=("Arial", 12), bg="#3498DB", fg="white").grid(row=0, column=2, padx=10)
    tk.Button(searchFrame, text="Show All", font=("Arial", 12), bg="#2ECC71", fg="white", command=populate_product_list).grid(row=0, column=3, padx=10)

    columns = ("ID", "Name", "Price", "Quantity")
    product_table = ttk.Treeview(productFrame, columns=columns, show="headings")
    for col in columns:
        product_table.heading(col, text=col)
        product_table.column(col, width=100)
    product_table.pack(fill="both", expand=True, padx=10, pady=10)

    populate_product_list()
    product_table.bind("<<TreeviewSelect>>", on_product_select) 

    # === Customer Details Section (Middle) ===
    customerFrame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    customerFrame.place(x=480, y=110, width=450, height=500)

    tk.Label(customerFrame, text="Customer's Details", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(fill="x", pady=5)

    nameFrame = tk.Frame(customerFrame, bg="white")
    nameFrame.pack(pady=5, padx=10, fill="x")

    tk.Label(nameFrame, text="Name:", font=("Arial", 12), bg="white").pack(side="left")
    name_entry = tk.Entry(nameFrame, font=("Arial", 12), width=25)
    name_entry.pack(side="left", padx=10)

    phoneFrame = tk.Frame(customerFrame, bg="white")
    phoneFrame.pack(pady=5, padx=10, fill="x")

    tk.Label(phoneFrame, text="Phone Number:", font=("Arial", 12), bg="white").pack(side="left")
    phone_entry = tk.Entry(phoneFrame, font=("Arial", 12), width=25)
    phone_entry.pack(side="left", padx=10)

    # === My Cart Total Product Section ===
    cartFrame = tk.Frame(customerFrame, bg="white", bd=2, relief="ridge")
    cartFrame.pack(fill="x", padx=10, pady=10)

    tk.Label(cartFrame, text="My Cart", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(fill="x")

    cart_columns = ("ID", "Name", "Quantity", "Price")
    cart_table = ttk.Treeview(cartFrame, columns=cart_columns, show="headings")
    for col in cart_columns:
        cart_table.heading(col, text=col)
        cart_table.column(col, width=100)
    cart_table.pack(fill="both", expand=True, padx=10, pady=10)

    # === Product Selection Entry Area ===
    # === Product Entry Section ===
    entryFrame = tk.Frame(customerFrame, bg="white", bd=2, relief="ridge")
    entryFrame.pack(fill="x", padx=5, pady=10)  # Apply fill="x" for width consistency

    tk.Label(entryFrame, text="Product Name:", font=("Arial", 12), bg="white").pack(side="left", padx=5)
    name_entry = tk.Entry(entryFrame, font=("Arial", 12), width=5)  # Maintain a reduced width
    name_entry.pack(side="left", padx=5)

    tk.Label(entryFrame, text="Price:", font=("Arial", 12), bg="white").pack(side="left", padx=5)
    price_entry = tk.Entry(entryFrame, font=("Arial", 12), width=5)
    price_entry.pack(side="left", padx=5)

    tk.Label(entryFrame, text="Quantity:", font=("Arial", 12), bg="white").pack(side="left", padx=5)
    quantity_entry = tk.Entry(entryFrame, font=("Arial", 12), width=5)
    quantity_entry.pack(side="left", padx=5)
    quantity_entry.bind("<KeyRelease>", update_price)

    # === In-Stock Display & Buttons Section ===
    stockFrame = tk.Frame(customerFrame, bg="white", bd=2, relief="ridge")
    stockFrame.pack(fill="x", padx=10, pady=10)

    # tk.Label(stockFrame, text="In Stock:", font=("Arial", 12), bg="white").pack(side="left", padx=10)

    stock_label = tk.Label(stockFrame, text="0", font=("Arial", 12, "bold"), bg="white", fg="#E74C3C")
    stock_label.pack(side="left", padx=10)

    total_price_display = tk.Label(stockFrame, textvariable=total_price_label, font=("Arial", 12, "bold"), bg="white", fg="green")
    total_price_display.pack(side="left", padx=10)


# Buttons for Clearing Cart and Adding Product
    tk.Button(stockFrame, text="Clear", font=("Arial", 12), bg="#E74C3C", command=lambda: quantity_entry.delete(0, tk.END)).pack(side="left", padx=10)
    tk.Button(stockFrame, text="Add to Cart", font=("Arial", 12), bg="#2ECC71", command=add_to_cart).pack(side="left", padx=10)

    # === Customer Billing Area Section (Right Side) ===
    customerBillingFrame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    customerBillingFrame.place(x=940, y=110, width=450, height=500)

    tk.Label(customerBillingFrame, text="Customer Billing Area", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(fill="x", pady=5)

    billing_label = tk.Label(customerBillingFrame, font=("Arial", 12), bg="white", fg="black", justify="left", anchor="w")
    billing_label.pack(fill="x", padx=10, pady=5)

   
    tk.Button(customerBillingFrame, text="Generate Bill", font=("Arial", 12), bg="#2ECC71", command=generate_bill).pack(pady=5)
    tk.Button(customerBillingFrame, text="Print Bill", font=("Arial", 12), bg="#3498DB", command=print_bill).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    show_dashboard()



 # billing_text = tk.Text(customerBillingFrame, font=("Arial", 12), width=50, height=20)
    # billing_text.pack(padx=10, pady=10)


















































# # Function to handle calculator button clicks
# def calculator_click(value):
#     calc_entry.insert(tk.END, value)

# def clear_calc():
#     calc_entry.delete(0, tk.END)

# # Function to add selected product to cart
# def add_to_cart():
#     product_id = selected_product_id.get()
#     product_name = selected_product_name.get()
#     product_price = selected_product_price.get()
#     product_quantity = selected_product_quantity.get()

#     if product_id and product_name and product_price and product_quantity:
#         cart_table.insert("", tk.END, values=(product_id, product_name, product_price, product_quantity))
#         clear_selection()
#     else:
#         messagebox.showerror("Error", "Please select a product before adding to cart.")

# def clear_selection():
#     selected_product_id.set("")
#     selected_product_name.set("")
#     selected_product_price.set("")
#     selected_product_quantity.set("")

# # Function to generate bill
# def generate_bill():
#     customer_name = name_entry.get()
#     contact_number = contact_entry.get()

#     if not customer_name or not contact_number:
#         messagebox.showerror("Error", "Please enter customer details before generating a bill.")
#         return

#     bill_content = f"Customer Name: {customer_name}\nContact: {contact_number}\nPurchased Items:\n"

#     for item in cart_table.get_children():
#         values = cart_table.item(item, 'values')
#         bill_content += f"{values[1]} - ${values[2]} x {values[3]}\n"

#     messagebox.showinfo("Bill Generated", bill_content)


    # # === Customer Details Section ===
    # customerFrame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    # customerFrame.place(x=480, y=110, width=300, height=150)

    # tk.Label(customerFrame, text="Customer Details", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(fill="x", pady=5)

    # name_entry = tk.Entry(customerFrame, font=("Arial", 12), width=30)
    # name_entry.pack(padx=10, pady=5)

    # contact_entry = tk.Entry(customerFrame, font=("Arial", 12), width=30)
    # contact_entry.pack(padx=10, pady=5)

    # # === Selected Product Section ===
    # selectedFrame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    # selectedFrame.place(x=10, y=620, width=450, height=150)

    # tk.Label(selectedFrame, text="Selected Product", font=("Arial", 14, "bold"), bg="#2C3E50", fg="white").pack(fill="x", pady=5)

    # selected_product_id = tk.StringVar()
    # selected_product_name = tk.StringVar()
    # selected_product_price = tk.StringVar()
    # selected_product_quantity = tk.StringVar()

    # tk.Entry(selectedFrame, textvariable=selected_product_id, font=("Arial", 12), width=30).pack(padx=10, pady=5)
    # tk.Entry(selectedFrame, textvariable=selected_product_name, font=("Arial", 12), width=30).pack(padx=10, pady=5)
    # tk.Entry(selectedFrame, textvariable=selected_product_price, font=("Arial", 12), width=30).pack(padx=10, pady=5)
    # tk.Entry(selectedFrame, textvariable=selected_product_quantity, font=("Arial", 12), width=30).pack(padx=10, pady=5)

    # tk.Button(selectedFrame, text="Add to Cart", font=("Arial", 12), bg="#2ECC71", fg="white", command=add_to_cart).pack(pady=5)
    # tk.Button(selectedFrame, text="Clear", font=("Arial", 12), bg="#FF5733", fg="white", command=clear_selection).pack(pady=5)

    # # === Cart Section ===
    # cartFrame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    # cartFrame.place(x=480, y=280, width=300, height=200)

    # tk.Label(cartFrame, text="My Cart", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(fill="x", pady=5)

    # cart_columns = ("ID", "Name", "Price", "Quantity")
    # cart_table = ttk.Treeview(cartFrame, columns=cart_columns, show="headings")
    # for col in cart_columns:
    #     cart_table.heading(col, text=col)
    #     cart_table.column(col, width=100)
    # cart_table.pack(fill="both", expand=True, padx=10, pady=10)

    # # === Calculator Section ===
    # calcFrame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    # calcFrame.place(x=800, y=110, width=200, height=200)

    # calc_entry = tk.Entry(calcFrame, font=("Arial", 16), justify="right")
    # calc_entry.pack(fill="x", padx=10, pady=5)

    # tk.Button(calcFrame, text="Clear", font=("Arial", 12), bg="#FF5733", command=clear_calc).pack(pady=5)

    # # === Billing Section ===
    # billingFrame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    # billingFrame.place(x=800, y=420, width=400, height=200)

    # tk.Label(billingFrame, text="Generate Bill", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(fill="x", pady=5)
    # tk.Button(billingFrame, text="Generate Bill", font=("Arial", 12), bg="#2ECC71", fg="white", command=generate_bill).pack(pady=5)









     # customerFrame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    # customerFrame.place(x=480, y=110, width=450, height=500)

    # tk.Label(customerFrame, text="Customer's Details", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(fill="x", pady=5)

    # tk.Label(customerFrame, text="Name:", font=("Arial", 12), bg="white").pack(anchor="w", padx=10, pady=5)
    # name_entry = tk.Entry(customerFrame, font=("Arial", 12), width=30)
    # name_entry.pack(padx=10)

    # tk.Label(customerFrame, text="Phone Number:", font=("Arial", 12), bg="white").pack(anchor="w", padx=10, pady=5)
    # phone_entry = tk.Entry(customerFrame, font=("Arial", 12), width=30)
    # phone_entry.pack(padx=10)