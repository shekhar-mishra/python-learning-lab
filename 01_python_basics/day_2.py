class Student:

    def __init__(self,name,age):
       self.name
       self.age
    def displayStudentdetails(self):
        print("Name",self.name)   
        print("Age",self.age)   
student1=Student("Shekhar",25)   
student1.displayStudentdetails()     

# print(help())
# print(dir("shekhar"))
# print(dir(list))
# print(help(list))

items=[]
while True:
    item=input("Enter your item:")
    items.append(item)
    print("Item are:",items)
