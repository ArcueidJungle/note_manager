class BankAccount:
    __balance = 0
    __owner = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, ammount):
        self.balance +=  ammount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance

account = BankAccount("Иван Иванов", 1000)
account.deposit(500)
account.withdraw(200)
print(account.check_balance())  # Ожидаемый результат: 1300