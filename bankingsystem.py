
class User():
    def __init__(self):
        self.name = input("What is your name:")
        self.gender = input("What is your gender:")
        self.age = input("What is your age:")

    def print_info(self):
        print("")
        print("Account Details")
        print("---------------")
        print("")
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Age:", self.age)
        print("")
        print("---------------")

           
class Bank(User):
    
    def __init__(self):
        
        self.balance = 0
        

    def deposit(self):
        self.amount = int(input("How much money do you want to deposit: "))
        self.balance = 0
        self.balance += self.amount
        print("Your current balance is $", self.balance)    
    
    def withdraw(self):
        self.w_amount =int(input("How much do money do you want to withdraw: "))

        if (self.w_amount<= self.balance):
            self.balance -= self.w_amount
        else:
            print("Sorry you don't have enough money to withdraw!!")

        print("your current balance is $", self.balance)
    
user1 = User()
user1.print_info()
user1 = Bank()
user1.deposit()
user1.withdraw()

    


    






    

    