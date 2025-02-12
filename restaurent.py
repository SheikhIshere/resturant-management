class Restaurant:
    def __init__(self, name, rent, menu = []):
        self.name = name
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0
    
    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee

    def add_order(self, order):
        self.orders.append(order)

    def receive_payment(self, order, amount, customer):
        # print(amount, order.bill)
        if amount >= order.bill :
            self.revenue += order.bill
            self.balance += order.bill            
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('############Not enough money. pay more############')
    def pay_expense(self, amount, discription):
        if amount <= self.balance:            
            self.expense += amount
            self.balance -= amount
            
            print(f' Expense {amount} for {discription}')
        else:
            print(f'Not enougn money to pay {amount}')    
    
    def pay_salary(self, employee):
        if employee.salary < self.balance:
            self.balance -= employee.salary  # Deduct salary from balance
            self.expense += employee.salary  # Add salary to expense
            employee.receive_salary()  # Notify the employee of the salary payment            
        else:
            print(f"Not enough balance to pay {employee.name}'s salary.")

    def show_employees(self):
        print("********showing employees name*********")
        if self.chef is not None:
            print(f'Chef: {self.chef.name} with salary: {self.chef.salary}' )
        else:
            print("no chef employed.")
        
        if self.server is not None:
            print(f'Server: {self.server.name} with salary: {self.server.salary}' )
        else:
            print("no server employed.")
        
        if self.manager is not None:
            print(f'Manager: {self.manager.name} with salary: {self.manager.salary}' )
        else:
            print("no manager employed.")