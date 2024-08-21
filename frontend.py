from cmu_graphics import *
import time
import money
import datetime
import casino
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



background = Rect(0,0,1500,1000,fill=gradient(rgb(98,132,255), 'white', 'red',
     start='left-top'))
background2 = Rect(0,0,1500,1000,fill=gradient(rgb(48, 207, 208), rgb(51, 8, 103)),opacity=0)
background3 = Rect(0,0,1500,1000,fill=gradient('darkred', 'black'),opacity=0)

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
dayLabel = Label("",1400,25,size=40,fill = "white")
balance = Label("",750, 30, size=37,fill="white",border = "white", borderWidth = 2)

savings = Label("",750,60,size=30,fill="white")
quitGame = Circle(59, 60, 40, fill="red")
quitGameText = Label("Save & Quit",59,60,size=15,font="symbols")

machineBase = Rect(150,120,1200,500,fill="gold")
slotsBackground = Rect(250,200,1000,300,fill="white")
slotsdivider1 = Rect(583,200,5,300,fill="gray",opacity = 30)
slotsdivider2 = Rect(916,200,5,300,fill="gray",opacity = 30)

gotostocks = Circle(1357,632,60,fill="white")
gotosm = Circle(1357,832,60, fill="white")
gotomain = Circle(1357,832,60, fill="white")
gotomain2 = Circle(140,70,60, fill="lightSalmon")
stocksImage = Image("https://icon-icons.com/downloadimage.php?id=258648&root=4066/PNG/64/&file=arrow_exchanges_exchange_growth_stock_market_bars_economy_stocks_icon_258648.png",1325,600)
smImage = Image("https://icon-icons.com/downloadimage.php?id=139008&root=2249/PNG/64/&file=slot_machine_outline_icon_139008.png",1325,800)
homeImage = Image("https://icon-icons.com/downloadimage.php?id=113416&root=1744/PNG/64/&file=3643769-building-home-house-main-menu-start_113416.png",1325,800)
homeImage2 = Image("https://icon-icons.com/downloadimage.php?id=113416&root=1744/PNG/64/&file=3643769-building-home-house-main-menu-start_113416.png",108, 35)
Screen1 = Group(background,options,withdraw,deposit,inputBox,inputText,errorText,dayLabel,balance,savings,quitGame,quitGameText,gotosm,smImage,gotostocks,stocksImage)
Screen2 = Group(background2,gotomain,homeImage,machineBase,slotsBackground,slotsdivider1,slotsdivider2)


Screen2.opacity = 0


with open("data.txt", "r") as read:
    data = read.readlines()
    for line in data:
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
            dayNumber = 0
            if day != '':
                dayNumber = int(day)
            
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



date1 = Rect(1260, 20, 200, 100, fill=gradient('gold', 'orangeRed', 'coral', start='top-right'), border='black') # Date box
dateLabel = Label(f'Day: {app.daycounter}', 1360, 70, size=40, bold=True)


savings1 = Rect(320, 20, 830, 100, fill=gradient('lightGray',  'silver','lightSlateGray', start='right'), border='black')  # Savings Box
savingsLabel = Label(f'Balance: ${playerBank.balance}', 710, 70, size=40, bold=True)

# Drawing the main stock sections
stock1 = Rect(60, 200, 400, 300, fill=gradient('red', 'orange', 'yellow', start='right'), border='black')  # Stock 1
stock1Label = Label("stock1Name", 260, 350, size=50, bold=True)

stock2 = Rect(560, 200, 400, 300, fill=gradient(rgb(57, 105, 94), rgb(85, 139, 121) , rgb(147, 191, 159), start='top-right'), border='black')  # Stock 2
stock2Label = Label("stock2Name", 760, 350, size=50, fill='white', bold=True)

stock3 = Rect(1060, 200, 400, 300, fill=gradient('green', 'cyan', start='bottom-left'), border='black')  # Stock 3
stock3Label = Label("stock3Name", 1260, 350, size=50, bold=True)

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


Screen3 = Group(background3,gotomain2,homeImage2, savings1, savingsLabel, stock1, stock1Label, stock2, stock2Label, stock3, stock3Label, buy1Button, buy2Button, buy3Button, buy1Label, buy2Label, buy3Label,  sell1Button, sell2Button, sell3Button, sell1Label, sell2Label, sell3Label, date1, dateLabel)
Screen3.opacity = 0


orange1 = Image("https://icon-icons.com/downloadimage.php?id=122731&root=1954/PNG/256/&file=orangefruit_122731.png",285,200,opacity=0)
orange2 = Image("https://icon-icons.com/downloadimage.php?id=122731&root=1954/PNG/256/&file=orangefruit_122731.png",618,200,opacity=0)
orange3 = Image("https://icon-icons.com/downloadimage.php?id=122731&root=1954/PNG/256/&file=orangefruit_122731.png",951,200,opacity=0)

cherry1 = Image("https://icon-icons.com/downloadimage.php?id=68770&root=881/PNG/256/&file=Cherry_icon-icons.com_68770.png",285,200,opacity=0)
cherry2 = Image("https://icon-icons.com/downloadimage.php?id=68770&root=881/PNG/256/&file=Cherry_icon-icons.com_68770.png",618,200,opacity=0)
cherry3 = Image("https://icon-icons.com/downloadimage.php?id=68770&root=881/PNG/256/&file=Cherry_icon-icons.com_68770.png",951,200,opacity=0)

grape1 = Image("https://icon-icons.com/downloadimage.php?id=182560&root=2879/PNG/256/&file=food_fruit_grape_icon_182560.png",285,200,opacity=0)
grape2 = Image("https://icon-icons.com/downloadimage.php?id=182560&root=2879/PNG/256/&file=food_fruit_grape_icon_182560.png",618,200,opacity=0)
grape3 = Image("https://icon-icons.com/downloadimage.php?id=182560&root=2879/PNG/256/&file=food_fruit_grape_icon_182560.png",951,200,opacity=0)

bell1 = Image("https://icon-icons.com/downloadimage.php?id=100835&root=1465/PNG/256/&file=685bell_100835.png",285,200,opacity=0)
bell2 = Image("https://icon-icons.com/downloadimage.php?id=100835&root=1465/PNG/256/&file=685bell_100835.png",618,200,opacity=0)
bell3 = Image("https://icon-icons.com/downloadimage.php?id=100835&root=1465/PNG/256/&file=685bell_100835.png",951,200,opacity=0)

bar1 = Image("https://icon-icons.com/downloadimage.php?id=260005&root=4102/PNG/256/&file=shape_rectangular_thick_geometry_horisontal_rectangle_icon_260005.png",285,200,opacity=0)
bar2 = Image("https://icon-icons.com/downloadimage.php?id=260005&root=4102/PNG/256/&file=shape_rectangular_thick_geometry_horisontal_rectangle_icon_260005.png",618,200,opacity=0)
bar3 = Image("https://icon-icons.com/downloadimage.php?id=260005&root=4102/PNG/256/&file=shape_rectangular_thick_geometry_horisontal_rectangle_icon_260005.png",951,200,opacity=0)

seven1 = Image("https://icon-icons.com/downloadimage.php?id=259982&root=4101/PNG/256/&file=numbers_mathematics_seven_number_icon_259982.png",285,200,opacity=0)
seven2 = Image("https://icon-icons.com/downloadimage.php?id=259982&root=4101/PNG/256/&file=numbers_mathematics_seven_number_icon_259982.png",618,200,opacity=0)
seven3 = Image("https://icon-icons.com/downloadimage.php?id=259982&root=4101/PNG/256/&file=numbers_mathematics_seven_number_icon_259982.png",951,200,opacity=0)



def onStep():
    
    app.ucounter += 1/30
    app.daycounter += (1/30)/60
    if app.daycounter % 182 == 0:
        giveInterest()
    if app.daycounter % 7 == 0:
        playerBank.payCheck()
        playerBank.incomeTax(0.136)

        
    dayLabel.value = "Day " + str(int(app.daycounter))
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
        if gotostocks.hits(mouseX,mouseY) == True:
            Screen1.opacity = 0
            Screen3.opacity = 100
            app.screens = 3
    elif app.screens == 2:
        if gotomain.hits(mouseX,mouseY) == True:
            Screen1.opacity = 100
            Screen2.opacity = 0
            app.screens = 1
    elif app.screens == 3:
        if gotomain2.hits(mouseX,mouseY)==True:
            Screen1.opacity = 100
            Screen3.opacity = 0
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