# TODO: a bunch more things to check such as depositing negative values
#       not letting people access other bank accounts and balances
#

import unittest
from bank import BankAcct

acctOne = BankAcct(100, "Account One", 1)


class TestBank(unittest.TestCase):
    def test_withdraw(self):
        self.assertEqual(acctOne.withdraw(34), 100)
        # try:
        #     acctOne.withdraw(103)
        # except ValueError as v:
        # self.assertEqual(
        #     "You do not have enough balance, your current balance is: $"
        #     + str(acctOne.balance),
        #     str(v),
        # )

    def test_deposit(self):
        self.assertEqual(acctOne.deposit(34), 134)


if __name__ == "__main__":
    unittest.main()
