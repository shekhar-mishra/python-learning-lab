class Atm:
  
    def __init__(self):
        self.pin=""
        self.balance=0
    
    def atmMenu(self):
        user_input=input("""
        Hi, Welcome to ATM How can i help you?
        1. Pressn 1 to create Pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)
        if user_input=="1":
           self.createPin()
        if user_input=="2":
             self.change_pin()
        if user_input=="3":
           print("hello option3")
        if user_input=="4":
           print("hello option4")
        if user_input=="5":  
            exit()  
    def createPin(self):
        user_pin=input("""
        Enter your pin in 4 digit only numaric value
        """)  
        self.pin=user_pin
        self.atmMenu() 
    def change_pin(self):
        old_pin=input("""
        Please enter your existing pin
        """)  
        if (old_pin==self.pin):
           new_pin= input("""
           Enter your new pin
           """)  
           self.pin=new_pin
           print("your pin get changes sucessfully")
           self.atmMenu() 
        else:
            print("you have entered wrong pin")
            self.atmMenu()   

atm1=Atm()
atm1.atmMenu()
print("atm1 datattaa",atm1.pin)         
print("atm1 datattaa",atm1.pin)    