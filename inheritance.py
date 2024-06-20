# #Single inheritance
# class Parent:
    
#     def parent_method(self):
#         print("This is a parent method")
        
        
# class Child(Parent):
    
#     def child_method(self):
#         print("This is a child method")
        
        
#     def parent_method(self):
#         print("Parent method is overrided by child class")



# child = Child()
# child.child_method()
# child.parent_method()

#Multiple inheritance

# class Parent1:
    
#     def parent_method(self):
#         print("This is a parent1 method")
        
# class Parent2:
    
#     def parent_method(self):
#         print("This is a parent2 method")
        
# class Child(Parent1, Parent2):
    
#     def child_method(self):
#         print("This is a child method")
        
        
# child = Child()
# child.parent_method()

#Multilevel inheritance

# class GrandFather:
    
#     def __init__(self, grandfather_name):
#         self.grandfather_name = grandfather_name
        
# class Father(GrandFather):
    
#     def __init__(self, father_name, grandfather_name):
#         super().__init__(grandfather_name)
#         self.father_name = father_name
        
# class Son(Father):
    
#     def __init__(self, name, father_name, grandfather_name):
#         super().__init__(father_name, grandfather_name)
#         self.name = name
        
#     def family_heritage(self):
#         return '{} is the father {} is the father {}'.format(self.grandfather_name, self.father_name, self.name)
    
    
# son = Son('Subin Sundar Kv', 'Sundaran Kv', 'Kitta Kv')
# print(son.family_heritage())

# class Parent:
    
#     def __init__(self, name):
#         self.name = name
        
        
# class Child1(Parent):
    
#     def __init__(self, childname, name):
#         super().__init__(name)
#         self.childname = childname
        
#     def child_detail(self):
#         return '{} is the child of {}'.format(self.childname, self.name)
    
    
# class Child2(Parent):
    
#     def __init__(self, child2name, name):
#         super().__init__(name)
#         self.child2name = child2name
        
#     def child_detail(self):
#         return '{} is also the child of {}'.format(self.child2name, self.name)
    
# child = Child1('Subin', 'Bijali')
# child2 = Child2('Sreeraj', 'Bijali')
# print(child.child_detail())
# print(child2.child_detail())
