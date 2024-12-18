from foodItem import Food_Item
from menu import Menu
from user_class import Customer,Admin,Employee
from orders import Order
from restaurent import Restaurent

My_restourant=Restaurent("My_restourant")
def customer_menu():
    name=input("Enter Your Name: ")
    email=input("Enter Your Email: ")
    phone=input("Enter Your Phone Number: ")
    address=input("Enter Your Address: ")
    customer=Customer(name=name,email=email,phone=phone,address=address)
    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Paybill")
        print("5. Exit")

        choice=int(input("Enter Your Choice: "))
        if choice==1:
            customer.view_menu(My_restourant)
        elif choice==2:
            item_name=input("Enter Your item ")
            item_quantity=int(input("Enter item quantity: "))
            customer.add_to_cart(My_restourant,item_name,item_quantity)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print("Invalid")

def admin_menu():
    name=input("Enter Your Name: ")
    email=input("Enter Your Email: ")
    phone=input("Enter Your Phone Number: ")
    address=input("Enter Your Address: ")
    admin=Admin(name=name,email=email,phone=phone,address=address)
    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete")
        print("6. Exit")

        choice=int(input("Enter Your Choice: "))
        if choice==1:
            item_name=input("Enter New Item name: ")
            item_price=int(input("Enter Item Price: "))
            item_quantity=int(input("Enter Item Quantity: "))
            item=Food_Item(item_name,item_price,item_quantity)
            admin.add_new_item(My_restourant, item)
        elif choice==2:
            name=input("Enter Your name: ")
            phone=input("Enter Your phone: ")
            email=input("Enter Your email: ")
            designation=input("Enter Your Designation: ")
            age=input("Enter Your Age: ")
            salary=input("Enter Your Salary: ")
            address=input("Enter Your Address: ")
            employee=Employee(name, phone, email, address,age,designation,salary)
            admin.add_employee(My_restourant,employee)
        elif choice==3:
            admin.view_employee(My_restourant)
        elif choice==4:
            admin.view_item(My_restourant)
            print("Item deleted")
        elif choice==5:
            item_name=input("Enter Item Name: ")
            admin.remove_item(My_restourant,item_name)
        else:
            break
while True:
    print("--Welcome--")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print("Invalid Input!")