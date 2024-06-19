
class Employee:
    
    rise_amount = 1000
    
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        
     
    def employee_detail(self):
        return '{} have {} salary per month will have a bonus {}'.format(self.name, self.pay, self.rise_amount)
    
    def __private_method(self):
        print("This is a private method")
        
    def _protected_method(self):
        print("This is a protected method")
        

    @classmethod
    def calculate_rise_amount(cls, rise_amount):
        cls.rise_amount = rise_amount
        return 'rise amount for the employee is {}'.format(cls.rise_amount)
    
    @staticmethod
    def static_method(a, b):
        print(f'sum = {a + b}')
        print("This is a static method")
        
        
class Developer(Employee):
    
    def __init__(self, name, pay, domain):
        super().__init__(name, pay)
        self.domain = domain
        
    
    def employee_detail(self):
        return '{} is the new developer in the company as {}'.format(self.name, self.domain)
    
    def AddOperation(self, *args):
        return sum(args)
   
     
emp1 = Employee('Subin', 50000)
emp1._Employee__private_method()

emp1._protected_method()
print(emp1.calculate_rise_amount(2000))
print(emp1.employee_detail())
emp1.static_method(5, 6)

dev1 = Developer('Subin', 60000, 'Python Developer')
dev1._Employee__private_method()
print(dev1.employee_detail())
print(dev1.AddOperation(1, 2, 3, 4))
print(dev1.AddOperation(1, 2))