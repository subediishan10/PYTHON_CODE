import csv
class Item:
    def __init__(self,name,age): #constructor method
        
        #Run validations to the received arguments
        assert age>=0, f"Age {age} is not in negative"
 
        #Assign to self object
        self.name=name
        self.age=age
    def calculate(self,x,y):
        return x*y
    def __rep__(self):
        return f"Item('{self.name}',{self.age})"

item=Item("Ishan",2)
print(item)



    
    
                  


            
        
            
        
