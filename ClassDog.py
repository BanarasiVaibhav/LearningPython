# classes in python 
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name +" is sitting")
    def roll(self):
        print(self.name+" is rolling")
    def happy_Birthday(self):
        print("Happy Birthday "+self.name.title())
        self.age=self.age+1
        print("New age of "+self.name.title()+" is "+str(self.age))
dog1=Dog('tom',22)
print('Age of tom is '+str(dog1.age))
print(dog1.happy_Birthday())
