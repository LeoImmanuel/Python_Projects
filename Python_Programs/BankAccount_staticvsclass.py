class BankAccount:
    min_bal = 1000

    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.balance = balance

    @staticmethod
    def checkAccountNumber(account_num):
        return len(account_num) == 10
    
    @classmethod
    def changeMinBalance(cls, amount):
        cls.min_bal = amount
    
print(BankAccount.checkAccountNumber("1234567890"))
BankAccount.changeMinBalance(1500)
print(f"Minimum Balance: {BankAccount.min_bal}")