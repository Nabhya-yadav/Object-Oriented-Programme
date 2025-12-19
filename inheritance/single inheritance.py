class Animal:
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print(self.name)

class Dog(Animal):
    def sound(self):
        print(self.name ,"barks")

a=Dog("Tommy")
a.sound()