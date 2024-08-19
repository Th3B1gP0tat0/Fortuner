from cmu_graphics import *
import time
import money
import datetime
import pyautogui

playerBank = money.Bank(0, 0, 0) #temporary, will store in a seperate txt file later
app.width = 1500
app.height = 1000
app.ucounter = 0
app.daycounter = 0
pastTime = ''
dayLabel = Label("",1400,25,size=20)
balance = Label("",750, 30, size=30,border = "black", borderWidth = 2)

savings = Label("",750,60,size=25)
quitGame = Circle(59, 60, 40, fill="red")
quitGameText = Label("Save & Quit",59,60,size=15,font="symbols")




#saveImage = Image("https://drive.google.com/u/0/drive-viewer/AKGpihaQTAPspoZ43noYckiRqx2MtrHShWKPMN0hKW7pW4bgvPBGjvLHiBp0rMDT7bW2MKe_m5utfi39rpgGwtfQGU9x35tnEXN9JdQ=s2560",30,20)

with open("data.txt", "r") as read:
    for line in read.readlines():
        if line.startswith("money"):
            money_value = line.split('=')[1].strip()
            playerBank.balance = float(money_value)
        elif line.startswith("savings"):
            savings_value = line.split("=")[1].strip()
            playerBank.savings = float(savings_value)
        elif line.startswith("paycheck"):
            paycheck_value = line.split("=")[1].strip()
            playerBank.paycheck = float(paycheck_value)
        elif line.startswith("time"):
            pastTime = line.split("=")[1].strip()

now = datetime.datetime.now()
then = datetime.datetime.strptime(pastTime, '%Y-%m-%d %H:%M:%S')

elapsed_time = (now-then).total_seconds()
print(int(elapsed_time))
def giveInterest():
    playerBank.balance = playerBank.getInterest(0.05)
    #print on the screen that they gained interest

for r in range(int(elapsed_time)):
    days = r/60
    if days % 182.5 == 0:
        giveInterest()
    if days % 7 == 0:
        playerBank.payCheck()

def onStep():
    app.ucounter += 1/30
    app.daycounter += (1/30)/60
    if app.daycounter % 182.5 == 0:
        giveInterest()
    if app.daycounter % 7 == 0:
        playerBank.payCheck()
    dayLabel.value = "day " + str(int(app.daycounter))
    balance.value = "$" +  str(pythonRound(playerBank.balance,2))
    savings.value = "Savings: $" + str(pythonRound(playerBank.savings,2))
 #   savings.value = "Current Savings: " + str(playerBank.savings)

def onMousePress(mouseX, mouseY):
    if quitGame.hits(mouseX,mouseY) == True:
        Label('GAME SAVED. YOU CAN NOW EXIT OUT OF THE WINDOW',app.width/2,app.height/2,size = 35,fill = 'red', bold=True)
        save(1)

        pyautogui.hotkey("alt", "f4")
        app.stop()



def save(quit):
    with open("data.txt", "w") as file:
        file.write("money= " + str(playerBank.balance) + "\n")
        file.write("savings= " + str(playerBank.savings) + "\n")
        file.write("paycheck= " + str(playerBank.paycheck) + "\n")
        file.write("time= " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        if quit == 1:
            file.write("didQuit= True" + "\n")
        else:
            file.write("didQuit= False" + "\n")
        file.write("stock1= " + "\n")
        file.write("stock2= " + "\n")
        file.write("stock3= " + "\n")

cmu_graphics.run()