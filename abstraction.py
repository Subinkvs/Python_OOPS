from abc import ABC, abstractmethod

class Parent(ABC):
    
    @abstractmethod
    def abstract_class(self):
        pass
    
class Child(Parent):
    
    
    def child_method(self):
        print("This is a parent method")
        
    def abstract_class(self):
        print("This is an abstract method")
        
        
obj = Child()
obj.abstract_class()
