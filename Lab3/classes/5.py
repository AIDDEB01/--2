class Acc():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        if num > 0:
            self.balance += num
            print(f"Deposit successful! New balance: {self.balance}")
        else:
            print("ERROR: Deposit amount must be positive")

    def withdraw(self, num):
        if num <= 0:
            print("ERROR: Withdrawal amount must be positive")
        elif num > self.balance:
            print("ERROR: Insufficient funds")
        else:
            self.balance -= num
            print(f"Withdrawal successful! New balance: {self.balance}")

            
name = input("Name: ")

balance = int(input("Money: "))

obj = Acc(name,balance)
obj.deposit(-100)
obj.withdraw(-500)

obj.deposit(10)

obj.withdraw(20)
obj.withdraw(1000000000000000000000)


