from abc import ABC
from orders import Order
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=Order()
    
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self,restaurent,item_name,quantity):
        item=restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print("Item added")
        else:
            print("Item not found")
    def view_cart(self):
        print("--View cart--")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{item.quantity}")
        print(f"Total price: {self.cart.total_price}")
    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary
# emp=Employee('Rahim','rahim@gmail.com',12334,'Dhaka','chef',1200)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)

    def view_employee(self,restuatent):
        restuatent.view_employee()

    def add_new_item(self,restuatent,item):
        restuatent.menu.add_menu_item(item)

    def remove_item(self,restuatent,item):
        restuatent.menu.remove_item(item)

    def view_item(self,resturent):
        resturent.menu.show_menu()
