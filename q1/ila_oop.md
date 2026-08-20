**Name:** Dona Capillano
**Section:** Magnesium
**School Year:** 2026-2027
**Date:** August 20, 2026

# ILA 3-1: Applying the Four Pillers of OOP
## Sari-Sari Store Inventory System
### 1. Encapsulation
In the sari-sari store inventory system, Enscapsulation is used to keep product data like price and stock safe inside the product object.

'''python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock
    def sell (self, amount):
        if amount <= self._stock:
            self._stock -= amount
            print("Item sold!")

### 2. Abstraction 
Abstraction hides complicated backend steps and only shows simple actions to the user. A cashier may click "Process Sale", without needing to see the internal math or database calculations happening behind the scenes. This makes the system easier to use and maintain.

'''python
class StoreSystem:
    def process_sale(self, product, amount):
    # Cashier only sees this simple function cell
    product.sell(amount)

### 3. Inheritance
Inheritance lets specific products inherit common attributes from a general main product. a basic product has a name and a price, while a PerishableProduct inherits those same traits and adds an expiration_date. This keeps code clean and avoids repeating the same code.

'''python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class PerishableProduct(Product):
def __init__(self, name, pricem exp_date):
    super().__init__(name, price)
    selp.exp_date = exp_date 

### 4. Polymorphism
Polymorphism allows different items to perform the same action in their own way. for example, both standard and perishable products can have a get_discount() method, but perishable items can automatically give a larger discount when close to expiring.

'''python
class RegularItem:
    def get_discount(self):
        return 0.05
class PeroshableItem:
    def get_discount(self):
        return 0.20

### REFLECTION
Encapsulation is the most useful pillar for a sari-sari store system. As stock levels change always change during sales, protecting variables like price and item quantities stops bat data or human error from messing up inventory counts. using strict methods to handle stock changes ensures the store records remain accurate
