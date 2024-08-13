import time

class Bank():
    def __init__(self, balance, savings, paycheck):
        self.balance = balance
        self.savings = savings
        self.paycheck = paycheck
    def getInterest(self, interest_rate):
        self.savings = self.savings * (interest_rate + 1)
    def depositSavings(self, amount):
        self.savings +=  amount
        self.balance -= amount
        if amount > self.balance:
            return "Error: deposit amount is higher than current balance"
    def withdrawSavings(self, amount):
        self.savings -= amount
        self.balance += amount
        if amount > self.savings:
            return "Error: withdraw amount is higher than current savings"
    def payCheck(self):
        self.balance += self.paycheck
    def incomeTax(self, tax_rate):
        self.balance -= tax_rate*self.paycheck

