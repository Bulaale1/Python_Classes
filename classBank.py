import math
from datetime import date
print('--- Welcome To Python Classes ---')
print('1:Bank acount class: ')
print('2:Circle class: ')
print('3:Rectangle class: ')

#   1.  Class Bank account
class Bank_account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        
        try:
            amount = float(amount)
            if amount <= 0:
                print(f"❌ Error: Cannot deposit {amount}. Amount must be positive.")
                return
            
            self.balance += amount
            # now = datetime.datetime.now()
            self.transaction_history.append(f"+{amount}")
            print(f"✅ Deposited ${amount}. New balance: ${self.balance} ")
        except ValueError:
            print("❌ Error: Please enter a valid numerical amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Error: Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"❌ Error: Insufficient funds! You tried to withdraw ${amount} but only have ${self.balance}.")
        else:
            self.balance -= amount
            # now = datetime.datetime.now()
            self.transaction_history.append(f"-{amount}")
            print(f"💸 Withdrew ${amount} . Remaining: ${self.balance}")

    def details(self):
        print(f"\n👤 Holder: {self.account_holder} | 💰 Balance: ${self.balance}")

    def statement(self):
        print(f'\n--- 📜 Transaction History for {self.account_holder} ---')
        if not self.transaction_history:
            print("No transactions yet.")
        for entry in self.transaction_history:
            status = 'Deposit' if entry.startswith('+') else 'Withdrawal'
            print(f' {status:12}: {entry}')
# --- Execution ---
#   Class BankAccount instance
account_1 = Bank_account('Bulaale116',580)
account_1.deposit(250)
account_1.deposit(350)
account_1.deposit(-250)
account_1.deposit('million')
account_1.withdraw(57)
account_1.withdraw(0)
account_1.details()
account_1.statement()

print('---End of bank account class---')
print("-" * 20)

# 2. Circle class.
# Declare a circle class
class Circle:
    # pi = 3.141
    #The class circle accepts one parameter , radius
    def __init__(self,radius):
        self.radius = radius
    # calculate the circle area and return to it
    def area(self):
        return math.pi*(self.radius**2)
    
    # calculate the circle circumference and return to it
    def circumference(self):
        return math.pi*(2*self.radius)
    
    # assign the radius to a new value
    def resize(self,new_radius):
        self.radius = new_radius
    def __str__(self):
        return f"Circle class with :{self.radius} radius"
    
# --- Execution ---
#   Circle class intance.
circle = Circle(25)
print('Before resizing the radius')
print(circle)
# Display the result
print(f"The area of circle : {circle.area():.2f}")
print(f"The circumference of circle is :{circle.circumference():.2f}")

print("-" * 20)

print('After resizing the radius') 
circle.resize(50)
print(circle)
# Display the result
print(f"The area of circle : {circle.area():.2f}")
print(f"The circumference of circle is :{circle.circumference():.2f}")

print('---End of Circle class---')
print("-" * 20)


#   3. Rectangle class .
#   Declare a Rectangle class
class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width
    # calculate the area of the rectangle  and return to it
    def area (self):
        return self.width * self.length
    # calculate the perimeter of rectangle and return to it
    def perimeter (self):
        return 2*(self.length+self.width)
    def __str__(self):
        return f"Class Rectangle with length and width of :{self.length,self.width}"
# --- Execution ---
#   Rectangle class instance
rectangle = Rectangle(10,5)
print(rectangle)
print(f"The area of rectangle with {rectangle.length} and width of {rectangle.width} is: {rectangle.area()}")
print(f"The Perimeter of rectangle with {rectangle.length} and width of {rectangle.width} is: {rectangle.perimeter()}")
print('---End of Rectangle class---')
print("-" * 20)



# 4.    Inheritance 
class Vehicle:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
    def get_resale_value(self):
        value = 20000 - (date.today().year - self.year) * 1500
        return max(0,value)
    def get_age(self):
        return date.today().year  - self.year
    def describe(self):
        return f"This vehicle is {self.make}, {self.model}, {self.year}"
    def __str__(self):
        return f"This is Vehicle class with make:{self.make},model:{self.model},and manufactured on :{self.year}"
class Car(Vehicle):
    def __init__(self, make, model, year,number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
    def describe(self):
        return f"{super().describe()} with {self.number_of_doors} doors"
    
# Child Class 2: Motorcycle, which adds an attribute for has_sidecar.

class Motorcycle(Vehicle):
    def __init__(self, make, model, year,has_sidecar = False):
        super().__init__(make,model, year)
        self.has_sidecar = has_sidecar
    def describe (self):
        suffix = 'with sidecar' if self.has_sidecar else 'without sidecar'
        return f"{super().describe()} {suffix}"
    

# --- Execution ---
car = Car('Tesla', 'Model 3', 2023, 4)
motorcycle = Motorcycle('Yamaha', 'MT-07', 2011, False)
motorcycle1 = Motorcycle('Toyota', 'MT-09', 2014, True)
motorcycle2 = Motorcycle('Yamaha', 'MT-05', 2009)

print(car.describe())
print(f"Resale Value: $CAD {car.get_resale_value()}")
print(f"Age: {car.get_age()} years")

print("-" * 20)

print(motorcycle.describe())
print(f"Resale Value: $CAD {motorcycle.get_resale_value()}")
print(f"Age: {motorcycle.get_age()} years") 
print("-" * 20)

print(motorcycle1.describe())
print(f"Resale Value: $CAD {motorcycle1.get_resale_value()}")
print(f"Age: {motorcycle1.get_age()} years") 

print("-" * 20)

print(motorcycle2.describe())
print(f"Resale Value: $CAD {motorcycle2.get_resale_value()}")
print(f"Age: {motorcycle2.get_age()} years") 