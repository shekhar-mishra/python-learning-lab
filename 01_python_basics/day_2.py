class Student:
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def displayStudentdetails(self):
        print("Name",self.name)   
        print("Age",self.age)   
student1=Student("Shekhar",25)   
student1.displayStudentdetails()     