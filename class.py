#classes for the program

class Employee:
    def __init__(self, employee_id, position, salary, name):
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.name = name
    #get information from employee
    def getID(self):
        return self.employee_id
    def getPos(self):
        return self.position
    def getSalary(self):
        return self.salary
    def getName(self):
        return self.name
    #change values
    def changeID(self, newID):
        self.employee_id = newID
    def changePos(self, newPos):
        self.position = newPos
    def changeSal(self, newSal):
        self.salary = newSal
    def changeName(self, newName):
        self.name = newName
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
class Customer:
    def __init__(self, customer_id, email, phone, name):
        self.customer_id = customer_id
        self.email = email
        self.phone = phone
        self.name = name
    #get information from customer
    def getID(self):
        return self.customer_id
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone
    def getName(self):
        return self.name
    #change values
    def changeID(self, newID):
        self.customer_id = newID
    def changeEmail(self, newEmail):
        self.email = newEmail
    def changePhone(self, newPhone):
        self.phone = newPhone
    def changeName(self, newName):
        self.name = newName
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
class Inventory:
    def __init__(self, product_id, category, price, name):
        self.product_id = product_id
        self.category = category
        self.price = price
        self.name = name
    #get information from inventory
    def getID(self):
        return self.product_id
    def getCat(self):
        return self.category
    def getPrice(self):
        return self.price
    def getName(self):
        return self.name
    #change values
    def changeID(self, newID):
        self.product_id = newID
    def changeCategory(self, newCat):
        self.category = newCat
    def changePrice(self, newPrice):
        self.price = newPrice
    def changeName(self, newName):
        self.name = newName
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
class Transaction:
    def __init__(self, transaction_id, employee_id, customer_id, product_id, quantity, total_amount, date):
        self.transaction_id = transaction_id
        self.employee_id = employee_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_amount = total_amount
        self.date = date
    #get information from transaction
    def getTransID(self):
        return self.transaction_id
    def getEmpID(self):
        return self.employee_id
    def getCustID(self):
        return self.customer_id
    def getProdID(self):
        return self.product_id
    def getQuan(self):
        return self.quantity
    def getTotal(self):
        return self.total_amount
    def getDate(self):
        return self.date
