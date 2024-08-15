import random
class Bank():
    def __init__(self, balance, savings, paycheck):
        self.balance = balance
        self.savings = savings
        self.paycheck = paycheck
    def getInterest(self, interest_rate):
        self.savings = self.savings * (interest_rate + 1)
        return self.savings * (interest_rate + 1)
    def depositSavings(self, amount):
        if amount > self.balance:
            return "Error: Amount deposited is higher than current balance"
        elif amount < 0:
            return "Error: Cannot deposit/withdraw negative numbers"
        else:
            self.savings +=  amount
            self.balance -= amount
            return amount
    def withdrawSavings(self, amount):
        if amount > self.savings:
            return "Error: Amount withdrawed is higher than current balance"
        elif amount < 0:
            return "Error: Cannot deposit/withdraw negative numbers"
        else:
            self.savings -= amount
            self.balance += amount
    def payCheck(self):
        self.balance += self.paycheck
    def incomeTax(self, tax_rate):
        self.balance -= tax_rate*self.paycheck
    def chargeRent(self, rent):
        self.balance -= rent
#p1 = Bank(100000, 0, 800)
#p1.chargeRent(5000)
#print(p1.balance)
class Stonks():
    def __init__(self,rate,investment):
        self.rate = rate
        self.investment = investment
    def fluctuation(self):
        l = [1,2]