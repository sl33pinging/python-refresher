# import numpy as np
# TODO: use _ before


class BankAcct:
    def __init__(self, balance, name, acctNumber):
        self.balance = balance
        self.name = name
        self.acctNumber = acctNumber

    def withdraw(self, amountWithdrawn):
        if self.balance >= amountWithdrawn:
            # print(
            #     f"You have withdrawn: $"
            #     + str(amountWithdrawn)
            #     + " current balance: $"
            #     + str(self.balance)
            # )
            return self.balance - amountWithdrawn
        else:
            raise ValueError(
                f"You do not have enough balance, your current balance is: $"
                + self.balance
            )

    def deposit(self, amountDeposit):
        self.balance += amountDeposit
        print(
            "You have deposited: $"
            + str(amountDeposit)
            + " current balance: $"
            + str(self.balance)
        )
        return self.balance

    def checkBalance(self):
        print("you current balance is: $" + self.balance)
