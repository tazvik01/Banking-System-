class User():
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    name = input("What is your name:")
    gender = input("What is your gender:")
    age = input("What is your age:")

    print("")
    print("Account Details")
    print("---------------")
    print("")
    print("Name:", name)
    print("Gender:", gender)
    print("Age:", age)
    print("")
    print("---------------")
    

    



class Bank(User):
    
    def __init__(self,name,gender,age):
        super().__init__(name,gender,age)
        
    

    def deposit(self,amount,balance):
        self.amount = amount
        self.balance = balance

    amount = int(input("How much money do you want to deposit: "))
    balance = 0
    balance += amount
    print("Your current balance is $", balance)

    






    

    