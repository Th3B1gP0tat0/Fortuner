from cmu_graphics import *
import time
import money
import datetime
import pyautogui


playerBank = money.Bank(100000, 0, 0) #temporary, will store in a seperate txt file later
stock1 = money.Stonks(0.95,1.1)
stock2 = money.Stonks(0.5,2)
stock3 = money.Stonks(0.85,1.25)

app.width = 1500
app.height = 1000
app.ucounter = 0
app.daycounter = 0
app.vanishcounter = 0
#pastTime = ''
dayPlaceholder = 0

app.screens = 1



background = Rect(0,0,1500,1000,fill="grey")
background2 = Rect(0,0,1500,1000,fill=gradient('darkred', 'black'),opacity=0)
app.inputmode = 0
#deposit1000box = Rect(150,400,150,150,fill="blue")
#deposit10000box = Rect(320,400,150,150,fill="blue")
#deposit100000box = Rect(490,400,150,150,fill="blue")
#depositallbox = Rect(660,400,150,150,fill="blue")
#withdraw1000box = Rect(150,590,150,150,fill="red")
#withdraw10000box = Rect(320,590,150,150,fill="red")
#withdraw100000box = Rect(490,590,150,150,fill="red")
#withdrawallbox = Rect(660,590,150,150,fill="red")



options = Label('Click on the desired transaction and enter the amount of money', 750, 425, size = 25, fill="yellow")
withdraw = Label("Withdraw",895,475,size=35,bold=True)
deposit = Label("Deposit",600,475,size=35,bold=True)

inputBox = Rect(550,500,400,100,fill="gray",border="black")
inputText = Label('',750,550,size = 30)
errorText = Label("",750,610,size=20,fill = "red")
#withdrawBox = Rect(150,610,400,100,fill="white",border="black")
#withdrawText = Label('',350,660,size = 30)
dayLabel = Label("",1400,25,size=30)
balance = Label("",750, 30, size=37,border = "black", borderWidth = 2)

savings = Label("",750,60,size=30)
quitGame = Circle(59, 60, 40, fill="red")
quitGameText = Label("Save & Quit",59,60,size=15,font="symbols")

machineBase = Rect(150,120,1200,500,fill="black")
slotsBackground = Rect(250,200,1000,300,fill="white")
slotsdivider1 = Rect(583,200,5,300,fill="gray",opacity = 30)
slotsdivider2 = Rect(916,200,5,300,fill="gray",opacity = 30)

gotostocks = Circle(1357,832,60, fill="white")
gotomain = Circle(140,70,60, fill="lightSalmon")
stocksImage = Image("https://icon-icons.com/downloadimage.php?id=258648&root=4066/PNG/64/&file=arrow_exchanges_exchange_growth_stock_market_bars_economy_stocks_icon_258648.png",1325,800)
homeImage = Image("https://icon-icons.com/downloadimage.php?id=113416&root=1744/PNG/64/&file=3643769-building-home-house-main-menu-start_113416.png",108, 35)


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
            #didQuit = bool(quit1)
            print(quit1)
            data[4] = "didQuit= False\n"
        elif line.startswith("day#"):
            day = line.split("=")[1].strip()
            dayNumber = int(day)
        elif line.startswith("stock1"):
            stock1Name = line.split("=")[1].strip()
        elif line.startswith("stock2"):
            stock2Name = line.split("=")[1].strip()
        elif line.startswith("stock3"):
            stock3Name = line.split("=")[1].strip()
            
with open("data.txt","w") as write:
    write.writelines(data)
if quit1 == True:
    now = datetime.datetime.now()
    if pastTime != '':
        then = datetime.datetime.strptime(pastTime, '%Y-%m-%d %H:%M:%S')
    else:
        then = datetime.datetime.now()
    elapsed_time = (now-then).total_seconds()
    print(int(elapsed_time))
    app.daycounter += (elapsed_time/60)
app.daycounter += dayNumber

date = Rect(1260, 20, 200, 100, fill=gradient('gold', 'orangeRed', 'coral', start='top-right'), border='black') # Date box
dateLabel = Label(f'Day: {day}', 1360, 70, size=40, bold=True)


savings = Rect(320, 20, 830, 100, fill=gradient('lightGray',  'silver','lightSlateGray', start='right'), border='black')  # Savings Box
savingsLabel = Label(f'Savings Current Value: ${savings_value}', 710, 70, size=40, bold=True)

#goBack = Rect(1300, 20, 160, 100, fill="red", border='black')  # Back Button
#goBackLabel = Label('Back', 1380, 70, size=40, bold=True)

# Drawing the main stock sections
stock1 = Rect(60, 200, 400, 300, fill=gradient('red', 'orange', 'yellow', start='right'), border='black')  # Stock 1
stock1Label = Label(stock1Name, 260, 350, size=50, bold=True)

stock2 = Rect(560, 200, 400, 300, fill=gradient('lightSteelBlue', 'navy' , 'purple', start='top-right'), border='black')  # Stock 2
stock2Label = Label(stock2Name, 760, 350, size=50, fill='white', bold=True)

stock3 = Rect(1060, 200, 400, 300, fill=gradient('green', 'cyan', start='bottom-left'), border='black')  # Stock 3
stock3Label = Label(stock3Name, 1260, 350, size=50, bold=True)

# Drawing the Buy/Sell buttons

buy1Button = Rect(60, 550, 190, 100, fill='green', border='black')  # Buy Stock 1
buy1Label = Label('Buy', 150, 600, size=40)

sell1Button = Rect(270, 550, 190, 100, fill='red', border='black')  # Sell Stock 1
sell1Label = Label('Sell', 370, 600, size=40, fill='black')

buy2Button = Rect(560, 550, 190, 100, fill='green', border='black')  # Buy/Sell Stock 2
buy2Label = Label('Buy', 650, 600, size=40)
sell2Button = Rect(770, 550, 190, 100, fill='red', border='black')  # Buy/Sell Stock 1
sell2Label = Label('Sell', 870, 600, size=40)

buy3Button = Rect(1060, 550, 190, 100, fill='green', border='black')  # Buy/Sell Stock 3
buy3Label = Label('Buy', 1150, 600, size=40)
sell3Button = Rect(1270, 550, 190, 100, fill='red', border='black') # Buy/Sell Stock 1
sell3Label = Label('Sell', 1370, 600, size=40)



Screen1 = Group(background,options,withdraw,deposit,inputBox,inputText,errorText,dayLabel,balance,savings,quitGame,quitGameText,gotostocks,stocksImage)
Screen2 = Group(background2,gotomain,homeImage, savings, savingsLabel, stock1, stock1Label, stock2, stock2Label, stock3, stock3Label, buy1Button, buy2Button, buy3Button, buy1Label, buy2Label, buy3Label,  sell1Button, sell2Button, sell3Button, sell1Label, sell2Label, sell3Label, date, dateLabel)
Screen2.opacity = 0


now = datetime.datetime.now()
then = datetime.datetime.strptime(pastTime, '%Y-%m-%d %H:%M:%S')

elapsed_time = (now-then).total_seconds()
print(int(elapsed_time))
app.daycounter += int(elapsed_time/60)
def giveInterest():
    playerBank.getInterest(0.05)
    print(playerBank.savings)
    #print on the screen that they gained interest
if quit1 == True:
    for r in range(int(elapsed_time)):
        days = int(r/60)
        dayPlaceholder = days

        app.daycounter = dayNumber
        if days != 0 and days % 365 == 0:
            giveInterest()
        if days != 0 and days % 14 == 0:
            playerBank.payCheck()
if quit1 == True:
    app.daycounter += dayPlaceholder

def onStep():
    
    app.ucounter += 1/30
    app.daycounter += (1/30)/60
    if app.daycounter % 182 == 0:
        giveInterest()
    if app.daycounter % 7 == 0:
        playerBank.payCheck()
        playerBank.incomeTax(0.136)

        
    dayLabel.value = "day " + str(int(app.daycounter))
    balance.value = "$" +  str(pythonRound(playerBank.balance,2))
    savings.value = "Bank: $" + str(pythonRound(playerBank.savings,2))
 #   savings.value = "Current Savings: " + str(playerBank.savings)

def onMousePress(mouseX, mouseY):
    global inputIsClicked
    
    if app.screens == 1:
        if quitGame.hits(mouseX,mouseY) == True:
            Label('GAME SAVED. YOU CAN NOW EXIT OUT OF THE WINDOW',app.width/2,app.height/2,size = 35,fill = 'red', bold=True)
            save(1)
        #pyautogui.hotkey("alt", "f4")
            app.stop()
        if inputBox.hits(mouseX,mouseY) == True:
            inputIsClicked = True
            inputBox.fill = "white"
        else:
            inputIsClicked = False
            app.inputmode = 0
            inputBox.fill="gray"
        if deposit.hits(mouseX,mouseY) == True:
            deposit.fill = "red"
            withdraw.fill = "black"
            app.inputmode = 1
        elif withdraw.hits(mouseX,mouseY) == True:
            deposit.fill = "black"
            withdraw.fill = "red"
            app.inputmode = 2
        
        if gotosm.hits(mouseX,mouseY) == True:
            Screen1.opacity = 0
            Screen2.opacity = 100
            app.screens = 2
    elif app.screens == 2:
        if gotomain.hits(mouseX,mouseY) or goBack.hits(mouseX, mouseY) == True:
            Screen1.opacity = 100
            Screen2.opacity = 0
            app.screens = 1
        
    
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
            if app.inputmode == 1:
                r = playerBank.depositSavings(amount)
                if r != None:
                    errorText.value = r
                else:
                    errorText.value = ''
                    
            elif app.inputmode == 2:
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