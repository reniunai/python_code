"""
银行账户私有化案例
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance # 私有属性，外部不可以访问

    def deposit(self, amount):  # 存款
        self.__balance += amount

    def withdraw(self, amount):  # 提现
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__pay_interest()
            return amount
        else:
            print("提现失败")
            return 0

    def __pay_interest(self): # 私有方法，外部不可以访问
        self.__balance -= 5

    def get_balance(self):
        return self.__balance
    


account = BankAccount("123456", 1000)
account.deposit(200)
print(account.withdraw(300))

print(account.get_balance())

# 可以访问，不建议直接访问
print(account._account_number)