from cmu_graphics import *
import time
import money
import datetime
import pyautogui


playerBank = money.Bank(100000, 0, 0) #temporary, will store in a seperate txt file later
app.width = 1500
app.height = 1000
app.ucounter = 0
app.daycounter = 0
#pastTime = ''
dayPlaceholder = 0



background = Rect(0,0,1500,1000,fill="grey")

#deposit1000box = Rect(150,400,150,150,fill="blue")
#deposit10000box = Rect(320,400,150,150,fill="blue")
#deposit100000box = Rect(490,400,150,150,fill="blue")
#depositallbox = Rect(660,400,150,150,fill="blue")
#withdraw1000box = Rect(150,590,150,150,fill="red")
#withdraw10000box = Rect(320,590,150,150,fill="red")
#withdraw100000box = Rect(490,590,150,150,fill="red")
#withdrawallbox = Rect(660,590,150,150,fill="red")

withdraw = Label("Withdraw",495,475,size=30,bold=True)
deposit = Label("Deposit",200,475,size=30,bold=True)

inputBox = Rect(150,500,400,100,fill="white",border="black")
inputText = Label('',350,550,size = 30)
errorText = Label("",350,610,size=20,fill = "red")
#withdrawBox = Rect(150,610,400,100,fill="white",border="black")
#withdrawText = Label('',350,660,size = 30)
dayLabel = Label("",1400,25,size=20)
balance = Label("",750, 30, size=30,border = "black", borderWidth = 2)

savings = Label("",750,60,size=25)
quitGame = Circle(59, 60, 40, fill="red")
quitGameText = Label("Save & Quit",59,60,size=15,font="symbols")




#saveImage = Image("https://drive.google.com/u/0/drive-viewer/AKGpihaQTAPspoZ43noYckiRqx2MtrHShWKPMN0hKW7pW4bgvPBGjvLHiBp0rMDT7bW2MKe_m5utfi39rpgGwtfQGU9x35tnEXN9JdQ=s2560",30,20)

with open("data.txt", "r") as read:

    for line in read.readlines():
        if line.startswith("money="):
            money_value = line.split('=')[1].strip()
            print(money_value)
            playerBank.balance = float(money_value)
        elif line.startswith("savings"):
            savings_value = line.split("=")[1].strip()
            print(savings_value)
            playerBank.savings = float(savings_value)
        elif line.startswith("paycheck"):
            paycheck_value = line.split("=")[1].strip()
            playerBank.paycheck = float(paycheck_value)
        elif line.startswith("time"):
            pastTime = line.split("=")[1].strip()
        elif line.startswith("didQuit"):
            quit1 = line.split("=")[1].strip()
            didQuit = bool(quit1)
        elif line.startswith("day#"):
            day = line.split("=")[1].strip()
            dayNumber = int(day)
            



now = datetime.datetime.now()
then = datetime.datetime.strptime(pastTime, '%Y-%m-%d %H:%M:%S')

elapsed_time = (now-then).total_seconds()
print(int(elapsed_time))
app.daycounter += int(elapsed_time/60)
def giveInterest():
    playerBank.getInterest(0.05)
    print(playerBank.savings)
    #print on the screen that they gained interest

for r in range(int(elapsed_time)):
    days = int(r/60)
    dayPlaceholder = days

    app.daycounter = dayNumber
    if days != 0 and days % 182.5 == 0:
        giveInterest()
    if days != 0 % 7 == 0:
        playerBank.payCheck()

app.daycounter += dayPlaceholder

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
    global inputIsClicked
    global inputmode
    
    if quitGame.hits(mouseX,mouseY) == True:
        Label('GAME SAVED. YOU CAN NOW EXIT OUT OF THE WINDOW',app.width/2,app.height/2,size = 35,fill = 'red', bold=True)
        save(1)

        #pyautogui.hotkey("alt", "f4")
        app.stop()
    if inputBox.hits(mouseX,mouseY) == True:
        inputIsClicked = True
    else:
        inputIsClicked = False
        inputmode = 0
    if deposit.hits(mouseX,mouseY) == True:
        deposit.fill = "red"
        withdraw.fill = "black"
        inputmode = 1
    elif withdraw.hits(mouseX,mouseY) == True:
        deposit.fill = "black"
        withdraw.fill = "red"
        inputmode = 2
    
def onKeyPress(key):
    
    if inputIsClicked == True:
        if key in ["1","2","3","4","5","6","7","8","9","0"]:
            inputText.value += str(key)   
        elif key == "backspace" and len(str(inputText.value)) > 0:
            inputText.value = str(inputText.value).replace(str(inputText.value)[len(str(inputText.value))-1], '', 1)
        elif key == "enter" and len(str(inputText.value)) > 0:
            amount = float(inputText.value)
            inputText.value = ''
            withdraw.fill = "black"
            deposit.fill = "black"
            if inputmode == 1:
                r = playerBank.depositSavings(amount)
                if r != None:
                    errorText.value = r
                else:
                    errorText.value = ''
                    
            elif inputmode == 2:
                r = playerBank.withdrawSavings(amount)
                if r != None:
                    errorText.value = r
                else:
                    errorText.value = ''
                    
            else:
                errorText.value = "Please choose deposit/withdraw mode"
            
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
        file.write("day#= " + str(int(app.daycounter)))

cmu_graphics.run()