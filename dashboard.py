import tkinter as tk
from tkinter import PhotoImage, LEFT

root = tk.Tk()
root.title("Dashboard")
root.geometry("1270x668+0+0")
# root.resizable(0,0)
root.config(bg='white')

# Load background image
bg_image = PhotoImage(file='inventory(1).png')

# Create label with image and text
titleLabel = tk.Label(root, image=bg_image, compound=LEFT, text='  Presely Management System', font=('times new roman', 40, 'bold'), bg='#010048', fg='white', anchor='w', padx=20)
titleLabel.place(x=0, y=0, relwidth=1)

# Create Logout button
logoutButton = tk.Button(root, text='Logout', font=('times new roman', 20, 'bold'), fg='#010048')
logoutButton.place(x=1100, y=10)

# Create subtitle label
subtitleLabel = tk.Label(root, text='Welcome Admin\t\t Date: 18-02-2025\t\t Time: 15:33:01 pm', font=('times new roman', 15), bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

# Create left frame
leftFrame = tk.Frame(root)
leftFrame.place(x=0, y=102, width=200, height=555)

# Load and display logo image
logoImage = PhotoImage(file='checklist.png')
imageLabel = tk.Label(leftFrame, image=logoImage)
imageLabel.pack()

# Create menu label
menuLabel = tk.Label(leftFrame, text='Menu', font=('times new roman', 20), bg='#009688')
menuLabel.pack(fill=tk.X)

# Create employee button
employee_icon = PhotoImage(file='man.png')
employee_button = tk.Button(leftFrame, image=employee_icon, compound=LEFT, text='Employees', font=('times new roman', 20, 'bold'),anchor='w')
employee_button.pack(fill=tk.X)

# Create supplier button
supplier_icon = PhotoImage(file='tracking.png')
supplier_button = tk.Button(leftFrame, image=supplier_icon, compound=LEFT, text='Suppliers', font=('times new roman', 20, 'bold'),anchor='w')
supplier_button.pack(fill=tk.X)

# Create category button
category_icon = PhotoImage(file='categorization.png')
category_button = tk.Button(leftFrame, image=category_icon, compound=LEFT, text='Categories', font=('times new roman', 20, 'bold'),anchor='w')
category_button.pack(fill=tk.X)

# Create product button
product_icon = PhotoImage(file='cubes.png')
product_button = tk.Button(leftFrame, image=product_icon, compound=LEFT, text='Products', font=('times new roman', 20, 'bold'),anchor='w')
product_button.pack(fill=tk.X)

# Create sales button
sales_icon = PhotoImage(file='trend.png')
sales_button = tk.Button(leftFrame, image=sales_icon, compound=LEFT, text='Sales', font=('times new roman', 20, 'bold'),anchor='w')
sales_button.pack(fill=tk.X)

# Create exit button
exit_icon = PhotoImage(file='logout.png')
exit_button = tk.Button(leftFrame,  image=exit_icon, compound=LEFT, text='Exit', font=('times new roman', 20, 'bold'),anchor='w')
exit_button.pack(fill=tk.X)

emp_frame=tk.Frame(root,bg='#2c3e50',bd=3,relief='ridge')
emp_frame.place(x=400,y=125,height=170,width=280)
total_emp_icon=PhotoImage(file='division(1).png')
total_emp_icon_label=tk.Label(emp_frame,image=total_emp_icon,bg='#2c3e50')
total_emp_icon_label.pack(pady=10)

total_emp_label=tk.Label(emp_frame,text='Total Employees',bg='#2c3e50',fg='white', font=('times new roman',15,'bold'))
total_emp_label.pack()

total_emp_count_label=tk.Label(emp_frame,text='0',bg='#2c3e50',fg='white', font=('times new roman',30,'bold'))
total_emp_count_label.pack()


sup_frame=tk.Frame(root,bg='#8e44ad',bd=3,relief='ridge')
sup_frame.place(x=800,y=125,height=170,width=280)
total_sup_icon=PhotoImage(file='supplier(1).png')
total_sup_icon_label=tk.Label(sup_frame,image=total_sup_icon,bg='#8e44ad')
total_sup_icon_label.pack(pady=10)

total_sup_label=tk.Label(sup_frame,text='Total Suppliers',bg='#8e44ad',fg='white', font=('times new roman',15,'bold'))
total_sup_label.pack()

total_sup_count_label=tk.Label(sup_frame,text='0',bg='#8e44ad',fg='white', font=('times new roman',30,'bold'))
total_sup_count_label.pack()


cat_frame=tk.Frame(root,bg='#27ae60',bd=3,relief='ridge')
cat_frame.place(x=400,y=310,height=170,width=280)
total_cat_icon=PhotoImage(file='market-segment.png')
total_cat_icon_label=tk.Label(cat_frame,image=total_cat_icon,bg='#27ae60')
total_cat_icon_label.pack(pady=10)

total_cat_label=tk.Label(cat_frame,text='Category',bg='#27ae60',fg='white', font=('times new roman',15,'bold'))
total_cat_label.pack()

total_cat_count_label=tk.Label(cat_frame,text='0',bg='#27ae60',fg='white', font=('times new roman',30,'bold'))
total_cat_count_label.pack()


prod_frame=tk.Frame(root,bg='#2c3e50',bd=3,relief='ridge')
prod_frame.place(x=800,y=310,height=170,width=280)
total_prod_icon=PhotoImage(file='products.png')
total_prod_icon_label=tk.Label(prod_frame,image=total_prod_icon,bg='#2c3e50')
total_prod_icon_label.pack(pady=10)

total_prod_label=tk.Label(prod_frame,text='Total Products',bg='#2c3e50',fg='white', font=('times new roman',15,'bold'))
total_prod_label.pack()

total_prod_count_label=tk.Label(prod_frame,text='0',bg='#2c3e50',fg='white', font=('times new roman',30,'bold'))
total_prod_count_label.pack()


sales_frame=tk.Frame(root,bg='#2c3e50',bd=3,relief='ridge')
sales_frame.place(x=600,y=495,height=170,width=280)
total_sales_icon=PhotoImage(file='graph.png')
total_sales_icon_label=tk.Label(sales_frame,image=total_sales_icon,bg='#2c3e50')
total_sales_icon_label.pack(pady=10)

total_sales_label=tk.Label(sales_frame,text='Total Sales',bg='#2c3e50',fg='white', font=('times new roman',15,'bold'))
total_sales_label.pack()

total_sales_count_label=tk.Label(sales_frame,text='0',bg='#2c3e50',fg='white', font=('times new roman',30,'bold'))
total_sales_count_label.pack()

root.mainloop()
