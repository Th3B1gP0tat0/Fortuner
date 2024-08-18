from cmu_graphics import *
import time
import money


app.width = 1500
app.height = 1000
app.ucounter = 0
app.daycounter = 0
dayLabel = Label("",30,25,size=20)
balance = Label("",750, 30, size=30)

playerBank = money.Bank(100000, 0, 20000) #temporary, will store in a seperate txt file later

def onStep():
    app.ucounter += 1/30
    app.daycounter += (1/30)/60
    dayLabel.value = "day " + str(int(app.daycounter))
    balance.value = "Current Balance: " +  str(playerBank.balance)


cmu_graphics.run()
