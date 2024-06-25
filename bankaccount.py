# Design a BankAccount class that allows users to deposit, withdraw, and check their account balance. The class should also have a method to calculate the interest on the account balance. Additionally, create a SavingsAccount class that inherits from BankAccount and has a higher interest rate.

# Constraints:

# The base interest rate for BankAccount is 2% per annum.
# The interest rate for SavingsAccount is 3% per annum.
# The account balance should not go below 0.



class BankAccount:
       
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance 
    
    def deposit(self, money):
        self.balance += money
        return self.balance
    
    def withdraw(self, money):
        self.balance -= money
        return self.balance
    
    def calculate_interest(self):
        interest = self.balance * 0.02
        return interest
        
        
class SavingsAccount(BankAccount):
    
    def __init__(self, name, balance):
        super().__init__(name, balance)
    
    def calculate_interest(self):
        interest = self.balance * 0.03
        return interest
    
    def __private_method(self):
        print("This is a private method")
    
        
obj1 = BankAccount('Subin', 5000)  
print(obj1.deposit(5000))
print(obj1.withdraw(20000))
print(obj1.calculate_interest())
obj2 = SavingsAccount('Ajin', 6000)
print(obj2.deposit(5000))
print(obj2.withdraw(2000))
print(obj2.calculate_interest())
obj2._SavingsAccount__private_method()
        
        
        
ORDER_TABLE                 CUSTOMER_TABLE


ORDER_ID                    CUSTOMER_ID
                            CUSTOMER_NAME
                            EMAIL
CUSTOMER_ID
TOTAL AMOUNT
REGION
        
        
        
 SELECT CUSTOMER_NAME FROM CUSTOMER_TABLE
 JOIN ORDER_TABLE ON ORDER_TABLE.CUSTOMER_ID = CUSTOMER_TABLE.CUSTOMER_ID
 WHERE TOTAL AMOUNT > 100;  
 
 SELECT REGION, AVG(TOTAL AMOUNT) FROM ORDER_TABLE GROUP_BY REGION;