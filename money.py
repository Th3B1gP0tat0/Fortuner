import random
class Bank():
    def __init__(self, balance, savings, paycheck):
        self.balance = balance
        self.savings = savings
        self.paycheck = paycheck
        self.debtLimit = 3
        self.debtCounter = 0
    def getInterest(self, interest_rate):
        self.savings = self.savings * (interest_rate + 1)
        #return self.savings * (interest_rate + 1)
    def depositSavings(self, amount):
        if amount > self.balance:
            return "Error: Amount deposited is higher than current balance"
        elif amount < 0:
            return "Error: Cannot deposit/withdraw negative numbers"
        elif self.balance < 0:
            return "You are in debt, you don't have anything to put in savings"
        else:
            self.savings +=  amount
            self.balance -= amount

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
        if (self.balance - tax_rate*self.paycheck < 0):
            if self.debtCounter < self.debtLimit:
                self.balance -= tax_rate*self.paycheck
                self.debtCounter += 1
                return "You have currently gone more into debt"
            else:
                return "You have been in debt for far too long. You lose!"
        else:
            self.balance -= tax_rate*self.paycheck
            return tax_rate*self.paycheck
    def reduceBalance(self, amount): #can be used to charge rent/fees or can be used to subtract amounts from balance after investing them into stocks
        if (self.balance - amount < 0):
            if self.debtCounter < self.debtLimit:
                self.balance -= amount
                self.debtCounter += 1
                return "You have currently gone more into debt"
            else:
                return "You have been in debt for far too long. You lose!"
        else:
            self.balance -= amount
            return amount
        
class Stocks():
    def __init__(self, rate, start):
        self.rate = rate
        self.price = start
        self.shares = 0
    def addToPrice(self, price):
        self.price += price
    def liquidate(self):
        if self.shares == 0:
            return "You don't have anything to liquidate"
        else:
            r = self.price
            self.shares -= 1
            return r
    def fluctuation(self):
        rate = 0
        rate += self.rate * float(random.choice([-0.05, -0.10,-0.15,-0.25,-0.20,0.05,0.15,0.25,0.20,0.10]))
        self.price += rate
        if self.price <= 0:
            self.price = 0
            self.price -= rate