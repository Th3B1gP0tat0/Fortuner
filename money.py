import random

class BankAndStocks():
    def __init__(self, balance, savings, paycheck,investment):
        self.balance = balance
        self.savings = savings
        self.paycheck = paycheck
        self.investment = investment
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
    def fluctuation(self, lowerRate, upperRate):
        rate = random.choice([lowerRate,upperRate]) #lower rate is the percent decreased, upper rate is percent increased (example: 5% decrease and 10% increase would be 0.95 and 1.1)
        self.investment = self.investment * rate
    def invest(self, amount):
        if amount > self.balance:
            return "Error: Amount invested is higher than current balance"
        elif amount < 0:
            return "Error: Cannot invest/liquidate negative numbers"
        else:
            self.balance -= amount
            self.investment += amount
    def liquidate(self):
        if self.investment == 0:
            return "You don't have anything invested"
        else:
            self.balance += self.investment
            self.investment = 0
