from cmu_graphics import *
import time
import money
import datetime
import pyautogui

app.width = 1500
app.height = 1000
app.ucounter = 0
app.daycounter = 0
dayLabel = Label("",1400,25,size=20)
balance = Label("",750, 30, size=30,border = "black", borderWidth = 2)

savings = Label("",750,60,size=25)
quitGame = Circle(59, 60, 40, fill="red")
quitGameText = Label("Save & Quit",59,60,size=15,font="symbols")

#saveImage = Image("https://drive.google.com/u/0/drive-viewer/AKGpihaQTAPspoZ43noYckiRqx2MtrHShWKPMN0hKW7pW4bgvPBGjvLHiBp0rMDT7bW2MKe_m5utfi39rpgGwtfQGU9x35tnEXN9JdQ=s2560",30,20)
playerBank = money.Bank(100000, 0, 20000) #temporary, will store in a seperate txt file later


def onStep():
    app.ucounter += 1/30
    app.daycounter += (1/30)/60
    dayLabel.value = "day " + str(int(app.daycounter))
    balance.value = "$" +  str(playerBank.balance)
    savings.value = "Savings: $" + str(playerBank.savings)
 #   savings.value = "Current Savings: " + str(playerBank.savings)
def onMousePress(mouseX, mouseY):
    if quitGame.hits(mouseX,mouseY) == True:
        Label('GAME SAVED. YOU CAN NOW EXIT OUT OF THE WINDOW',app.width/2,app.height/2,size = 35,fill = 'red', bold=True)
        save()
        time.sleep(1)
        pyautogui.hotkey("alt", "f4")
        #app.stop()

def save():
    with open("data.txt", "w") as file:
        file.write("money: " + str(playerBank.balance) + "\n")
        file.write("savings: " + str(playerBank.savings) + "\n")
        file.write("time: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write("didQuit: True" + "\n")
        file.write("stock1: " + "\n")
        file.write("stock2: " + "\n")
        file.write("stock3: " + "\n")

cmu_graphics.run()