#classes for the program

class Employee:
    def __init__(self, employee_id, position, salary, name):
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.name = name

class Customer:
    def __init__(self, customer_id, email, phone, name):
        self.customer_id = customer_id
        self.email = email
        self.phone = phone
        self.name = name

class Inventory:
    def __init__(self, product_id, category, price, name) -> None:
        self.product_id = product_id
        self.category = category
        self.price = price
        self.name = name

class Transaction:
    def __init__(self, transaction_id, employee_id, customer_id, product_id, quantity, total_amount, date):
        self.transaction_id = transaction_id
        self.employee_id = employee_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_amount = total_amount
        self.date = date