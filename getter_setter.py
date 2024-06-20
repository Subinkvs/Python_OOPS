# class Employee:
    
#     def __init__(self, name, company_name, salary):
#         self.name = name 
#         self.company_name = company_name
#         self.salary = salary
        
#     @property
#     def employee_details(self):
#         return '{}'.format(self.company_name)
    
#     @employee_details.setter
#     def employee_details(self, company_name):
#         self.company_name = company_name
        
#     def update_employee_details(self):
#         return '{} is the new company'.format(self.company_name)
        
    
# emp1 = Employee('Subin', 'Amazon', 100000)
# print(emp1.employee_details)
# emp1.employee_details = 'Google'
# print(emp1.employee_details)
# print(emp1.update_employee_details())


class Employee:
    
    def __init__(self, name, company):
        self.name = name 
        self.__company = company
        
    @property
    def employee_email(self):
        return '{}@gmail.com'.format(self.name)
    
    @employee_email.setter
    def employee_email(self, name):
        self.name = name
        
emp1 = Employee('Subin', 'ABC')
print(emp1.employee_email)
emp1.employee_email  = 'Ajin'
print(emp1.employee_email)
print(emp1.name)
print(emp1._Employee__company)
        
    