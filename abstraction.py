from abc import ABC, abstractmethod

class Parent(ABC):
    
    @abstractmethod
    def abstract_method(self):
        pass
    
class Child(Parent):
    
    def abstract_method(self):
        print("This is a abstract method")
        
obj = Child()
obj.abstract_method()