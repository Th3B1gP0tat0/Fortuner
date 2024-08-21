from cmu_graphics import *
import time
import money
import datetime
import casino
import pyautogui


playerBank = money.Bank(100000, 0, 0) #temporary, will store in a seperate txt file later
stock1 = money.Stocks(100, 1000)
stock2 = money.Stocks(500, 5000)
stock3 = money.Stocks(1000, 10000)

slots = casino.SlotMachine

app.setMaxShapeCount(100000)


def buyStock(stockName, amount):
    if stockName == "stock1":
        if amount * stock1.price > playerBank.balance:
            return 0
        stock1.shares += amount
        playerBank.balance -= amount * stock1.price
        return 1
    
    if stockName == "stock2":
        if amount * stock2.price > playerBank.balance:
            return 0
        stock2.shares += amount
        playerBank.balance -= amount * stock2.price
        return 1
    
    if stockName == "stock3":
        if amount * stock3.price > playerBank.balance:
            return 0
        stock3.shares += amount
        playerBank.balance -= amount * stock3.price
        return 1
        

app.width = 1500
app.height = 1000
app.ucounter = 0
app.daycounter = 0
app.vanishcounter = 0
#pastTime = ''
dayPlaceholder = 0

app.screens = 1

#   savings.value = "Current Savings: " + str(playerBank.savings)
app.date1 = Rect(1260, 20, 200, 100, fill=gradient('gold', 'orangeRed', 'coral', start='top-right'), border='black') # Date box
app.dateLabel = Label('', 1360, 70, size=40, bold=True)
app.savings1 = Rect(320, 20, 830, 100, fill=gradient(rgb(127, 159, 159), rgb(134, 169, 171), rgb(145, 180, 183), rgb(158, 192, 196), rgb(172, 211, 214), rgb(184, 225, 228), rgb(197, 239, 239), start='right'), border='black')  # Savings Box
app.savingsLabel = Label('', 710, 70, size=40, bold=True)

    # Drawing the main stock sections
app.stock1box = Rect(60, 200, 400, 300, fill=gradient(rgb(128, 0, 32),rgb(153, 37, 58), rgb(179, 64, 84), rgb(204, 88, 111),rgb(229, 113, 138), start='right'), border='black')  # Stock 1
app.stock1Label = Label("Apple", 260, 310, size=50, bold=True)
app.stock1PriceLabel = Label('', 260, 390, size=50, bold=True)
app.stock1ShareLabel = Label('', 260, 470, size=30, bold=True)

app.stock2box = Rect(560, 200, 400, 300, fill=gradient(rgb(30, 77, 146), rgb(34, 111, 162), rgb(70, 130, 180), rgb(100, 149, 237), start='top-right'), border='black')  # Stock 2
app.stock2Label = Label("Microsoft", 760, 310, size=50, bold=True)
app.stock2PriceLabel = Label('', 760, 390, size=50, bold=True)
app.stock2ShareLabel = Label('',760, 470, size=30, bold=True)

app.stock3box = Rect(1060, 200, 400, 300, fill=gradient( rgb(99, 74, 58), rgb(172, 130, 80), rgb(232, 197, 174), start='bottom-left'), border='black')  # Stock 3
app.stock3Label = Label("Google", 1260, 310, size=50, bold=True)
app.stock3PriceLabel = Label('', 1260, 390, size=50, bold=True)
app.stock3ShareLabel = Label('', 1260, 470, size=30, bold=True)

# Drawing the Buy/Sell buttons

app.buy1Button = Rect(60, 550, 190, 100, fill= gradient(rgb(51, 214, 85), rgb(41, 172, 74), rgb(33, 130, 62), rgb(25, 100, 52), rgb(18, 73, 43), start='top-left'), border='black')  # Buy Stock 1
app.buy1Label = Label('Buy', 150, 600, size=40)

app.sell1Button = Rect(270, 550, 190, 100, fill= gradient(rgb(255, 110, 64), rgb(255, 68, 43), rgb(209, 40, 16), rgb(171, 52, 34), start='top-left'), border='black')  # Sell Stock 1
app.sell1Label = Label('Sell', 370, 600, size=40, fill='black')

app.buy2Button = Rect(560, 550, 190, 100, fill= gradient(rgb(51, 214, 85), rgb(41, 172, 74), rgb(33, 130, 62), rgb(25, 100, 52), rgb(18, 73, 43), start='top-left'), border='black')  # Buy/Sell Stock 2
app.buy2Label = Label('Buy', 650, 600, size=40)
app.sell2Button = Rect(770, 550, 190, 100, fill= gradient(rgb(255, 110, 64), rgb(255, 68, 43), rgb(209, 40, 16), rgb(171, 52, 34), start='top-left'), border='black')  # Buy/Sell Stock 1
app.sell2Label = Label('Sell', 870, 600, size=40)

app.buy3Button = Rect(1060, 550, 190, 100, fill= gradient(rgb(51, 214, 85), rgb(41, 172, 74), rgb(33, 130, 62), rgb(25, 100, 52), rgb(18, 73, 43), start='top-left'), border='black')  # Buy/Sell Stock 3
app.buy3Label = Label('Buy', 1150, 600, size=40)
app.sell3Button = Rect(1270, 550, 190, 100, fill= gradient(rgb(255, 110, 64), rgb(255, 68, 43), rgb(209, 40, 16), rgb(171, 52, 34), start='top-left'), border='black') # Buy/Sell Stock 1
app.sell3Label = Label('Sell', 1370, 600, size=40)


background = Rect(0,0,1500,1000,fill=gradient(rgb(0, 18, 23), rgb(0, 32, 39), rgb(0, 46, 54), rgb(0, 60, 69), rgb(0, 73, 84), rgb(57, 105, 94), rgb(85, 139, 121), start='left-top'))
background2 = Rect(0,0,1500,1000,fill=gradient(rgb(83, 2, 0), rgb(115, 0, 0), rgb(147, 0, 0), rgb(179, 0, 0), start='top-left'))
background3 = Rect(0,0,1500,1000,fill=gradient(rgb(48, 207, 208), rgb(51, 8, 103), 'black', start='top-left'))

app.inputmode = 0



dayLabel = Label("",1400,25,size=40,fill = "white",opacity=100)


savings = Label("",750,60,size=30,fill="white")


options = Label('Click on the desired transaction and enter the amount of money', 750, 425, size = 25, fill="yellow")
withdraw = Label("Withdraw",895,475,size=35,bold=True)
deposit = Label("Deposit",600,475,size=35,bold=True)

inputBox = Rect(550,500,400,100,fill="gray",border="black")
inputText = Label('',750,550,size = 30)
errorText = Label("",750,610,size=20,fill = "red")
#withdrawBox = Rect(150,610,400,100,fill="white",border="black")
#withdrawText = Label('',350,660,size = 30)

quitGame = Circle(59, 60, 40, fill="red")
quitGameText = Label("Save & Quit",59,60,size=15,font="symbols")

machineBase = Rect(150,120,1200,500,fill="gold")
slotsBackground = Rect(250,200,1000,300,fill="white")
slotsdivider1 = Rect(583,200,5,300,fill="gray",opacity = 30)
slotsdivider2 = Rect(916,200,5,300,fill="gray",opacity = 30)

gotostocks = Circle(1357,632,60,fill="white")
gotosm = Circle(1357,832,60, fill="white")
gotomain = Circle(90,70,60, fill="white")
gotomain2 = Circle(140,70,60, fill="lightSalmon")
stocksImage = Image("https://icon-icons.com/downloadimage.php?id=258648&root=4066/PNG/64/&file=arrow_exchanges_exchange_growth_stock_market_bars_economy_stocks_icon_258648.png",1325,600)
smImage = Image("https://icon-icons.com/downloadimage.php?id=139008&root=2249/PNG/64/&file=slot_machine_outline_icon_139008.png",1325,800)
homeImage = Image("https://icon-icons.com/downloadimage.php?id=113416&root=1744/PNG/64/&file=3643769-building-home-house-main-menu-start_113416.png",58,35)
homeImage2 = Image("https://icon-icons.com/downloadimage.php?id=113416&root=1744/PNG/64/&file=3643769-building-home-house-main-menu-start_113416.png",108, 35)

spinButton = Circle(750,800,80,fill=gradient("red","darkred"))
spinLabel = Label("SPIN!",750,800,fill = "gold",size=30,bold=True)

infoLabel = Label("Win up to $15000!!! $1000 per spin.",750,60,size=20,fill="lightGreen",bold=True)
notificationsLabel = Label("",750,700,size=20,fill = "white", bold=True)

Screen1 = Group(background,options,withdraw,deposit,inputBox,inputText,errorText,quitGame,quitGameText,gotosm,smImage,gotostocks,stocksImage,dayLabel,savings)
Screen2 = Group(background2,gotomain,homeImage,machineBase,slotsBackground,slotsdivider1,slotsdivider2,spinButton,spinLabel,infoLabel,notificationsLabel)
Screen3 = Group(background3,gotomain2,homeImage2, app.savings1, app.savingsLabel, app.stock1box, app.stock1Label, app.stock2box, app.stock2Label, app.stock3box, app.stock3Label, app.buy1Button, app.buy2Button, app.buy3Button, app.buy1Label, app.buy2Label, app.buy3Label,  app.sell1Button, app.sell2Button, app.sell3Button, app.sell1Label, app.sell2Label, app.sell3Label, app.date1, app.dateLabel, app.stock1PriceLabel, app.stock2PriceLabel, app.stock3PriceLabel, app.stock1ShareLabel, app.stock2ShareLabel, app.stock3ShareLabel)
Screen3.opacity = 0

Screen1.opacity = 100
Screen2.opacity = 0

balance = Label("",750, 30, size=37,fill="white",border = "white", borderWidth = 2, opacity = 100)

with open("data.txt", "r") as read:
    data = read.readlines()
    for line in data:
        if line.startswith("money="):
            money_value = line.split('=')[1].strip()
            # print(money_value)
            playerBank.balance = float(money_value)
        elif line.startswith("savings"):
            savings_value = line.split("=")[1].strip()
            # print(savings_value)
            playerBank.savings = float(savings_value)
        elif line.startswith("paycheck"):
            paycheck_value = line.split("=")[1].strip()
            playerBank.paycheck = float(paycheck_value)
        elif line.startswith("time"):
            pastTime = line.split("=")[1].strip()
        elif line.startswith("didQuit"):
            quit1 = line.split("=")[1].strip()
            #didQuit = bool(quit1)
            # print(quit1)
            data[4] = "didQuit= False\n"
        elif line.startswith("day#"):
            day = line.split("=")[1].strip()
            dayNumber = 0
            if day != '':
                dayNumber = int(day)
                
        elif line.startswith("stock1.shares="):
            stock1.shares = float(line.split('=')[1].strip())
        elif line.startswith("stock1.rate="):
            stock1.rate = float(line.split('=')[1].strip())
        elif line.startswith("stock1.price="):
            stock1.price = float(line.split('=')[1].strip())
            
        elif line.startswith("stock2.shares="):
            stock2.shares = float(line.split('=')[1].strip())
        elif line.startswith("stock2.rate="):
            stock2.rate = float(line.split('=')[1].strip())
        elif line.startswith("stock2.price="):
            stock2.price = float(line.split('=')[1].strip())

        elif line.startswith("stock3.shares="):
            stock3.shares = float(line.split('=')[1].strip())
        elif line.startswith("stock3.rate="):
            stock3.rate = float(line.split('=')[1].strip())
        elif line.startswith("stock3.price="):
            stock3.price = float(line.split('=')[1].strip())
        
            
with open("data.txt","w") as write:
    write.writelines(data)
if quit1 == True:
    now = datetime.datetime.now()
    if pastTime != '':
        then = datetime.datetime.strptime(pastTime, '%Y-%m-%d %H:%M:%S')
    else:
        then = datetime.datetime.now()
    elapsed_time = (now-then).total_seconds()
    # print(int(elapsed_time))
    app.daycounter += (elapsed_time/60)
app.daycounter += dayNumber

def giveInterest():
    playerBank.getInterest(0.05)
    # print(playerBank.savings)
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
    dayLabel.value = "Day " + str(int(app.daycounter))
    balance.value = "$" +  str(pythonRound(playerBank.balance,2))
    savings.value = "Bank: $" + str(pythonRound(playerBank.savings,2))    
    if app.screens == 3:

    #   savings.value = "Current Savings: " + str(playerBank.savings)
        #app.date1 = Rect(1260, 20, 200, 100, fill=gradient('gold', 'orangeRed', 'coral', start='top-right'), border='black') # Date box
        app.dateLabel.value = f'Day: {int(app.daycounter)}'


        #app.savings1 = Rect(320, 20, 830, 100, fill=gradient(rgb(127, 159, 159), rgb(134, 169, 171), rgb(145, 180, 183), rgb(158, 192, 196), rgb(172, 211, 214), rgb(184, 225, 228), rgb(197, 239, 239), start='right'), border='black')  # Savings Box
        app.savingsLabel.value = f'Balance: ${pythonRound(playerBank.balance,2)}'

        # Drawing the main stock sections
        #app.stock1box = Rect(60, 200, 400, 300, fill=gradient(rgb(128, 0, 32),rgb(153, 37, 58), rgb(179, 64, 84), rgb(204, 88, 111),rgb(229, 113, 138), start='right'), border='black')  # Stock 1
        #app.stock1Label = Label("Apple", 260, 310, size=50, bold=True)
        app.stock1PriceLabel.value = f'${pythonRound(stock1.price)}'
        app.stock1ShareLabel.value = f'Stocks Owned : {stock1.shares}'

        #app.stock2box = Rect(560, 200, 400, 300, fill=gradient(rgb(30, 77, 146), rgb(34, 111, 162), rgb(70, 130, 180), rgb(100, 149, 237), start='top-right'), border='black')  # Stock 2
        #app.stock2Label = Label("Microsoft", 760, 310, size=50, bold=True)
        app.stock2PriceLabel.value = f'${pythonRound(stock2.price)}'
        app.stock2ShareLabel.value = f'Stocks Owned : {stock2.shares}'

       # app.stock3box = Rect(1060, 200, 400, 300, fill=gradient( rgb(99, 74, 58), rgb(172, 130, 80), rgb(232, 197, 174), start='bottom-left'), border='black')  # Stock 3
       # app.stock3Label = Label("Google", 1260, 310, size=50, bold=True)
        app.stock3PriceLabel.value = f'${pythonRound(stock3.price,2)}'
        app.stock3ShareLabel.value = f'Stocks Owned : {stock3.shares}'
    else:
        Screen3.opacity = 0
    app.ucounter += 1/30
    app.daycounter += (1/30)/60
    if app.daycounter % 182 == 0:
        giveInterest()
    if app.daycounter % 7 == 0:
        playerBank.payCheck()
        playerBank.incomeTax(0.136)
    if app.ucounter != 0 and app.ucounter % 15 == 0:
        stock1.fluctuation()
        stock2.fluctuation()
        stock3.fluctuation()







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
            balance.opacity = 0
            app.screens = 3
    elif app.screens == 2:
        if gotomain.hits(mouseX,mouseY) == True:
            Screen1.opacity = 100
            Screen2.opacity = 0
            app.screens = 1
            orange1.opacity = 0
            orange2.opacity = 0
            orange3.opacity = 0
            
            cherry1.opacity = 0
            cherry2.opacity = 0
            cherry3.opacity = 0
            
            grape1.opacity = 0
            grape2.opacity = 0
            grape3.opacity = 0
            
            bell1.opacity = 0
            bell2.opacity = 0
            bell3.opacity = 0
            
            bar1.opacity = 0
            bar2.opacity = 0
            bar3.opacity = 0
            
            seven1.opacity = 0
            seven2.opacity = 0
            seven3.opacity = 0
        if spinButton.hits(mouseX,mouseY)==True:
            orange1.opacity = 0
            orange2.opacity = 0
            orange3.opacity = 0
            
            cherry1.opacity = 0
            cherry2.opacity = 0
            cherry3.opacity = 0
            
            grape1.opacity = 0
            grape2.opacity = 0
            grape3.opacity = 0
            
            bell1.opacity = 0
            bell2.opacity = 0
            bell3.opacity = 0
            
            bar1.opacity = 0
            bar2.opacity = 0
            bar3.opacity = 0
            
            seven1.opacity = 0
            seven2.opacity = 0
            seven3.opacity = 0
            playerBank.reduceBalance(1000)
            result = slots.play()
            playerBank.balance += result[3]
            notificationsLabel.value = f"Congratulations! You won ${result[3]}!"
            if result[0] == "orange":
                orange1.opacity = 100
            elif result[0] == "cherry":
                cherry1.opacity = 100
            elif result[0] == "grape":
                grape1.opacity = 100
            elif result[0] == "bell":
                bell1.opacity = 100
            elif result[0] == "bar":
                bar1.opacity = 100
            elif result[0] == "seven":
                seven1.opacity = 100
                
            if result[1] == "orange":
                orange2.opacity = 100
            elif result[1] == "cherry":
                cherry2.opacity = 100
            elif result[1] == "grape":
                grape2.opacity = 100
            elif result[1] == "bell":
                bell2.opacity = 100
            elif result[1] == "bar":
                bar2.opacity = 100
            elif result[1] == "seven":
                seven2.opacity = 100
                
            if result[2] == "orange":
                orange3.opacity = 100
            elif result[2] == "cherry":
                cherry3.opacity = 100
            elif result[2] == "grape":
                grape3.opacity = 100
            elif result[2] == "bell":
                bell3.opacity = 100
            elif result[2] == "bar":
                bar3.opacity = 100
            elif result[2] == "seven":
                seven3.opacity = 100
    elif app.screens == 3:
        if gotomain2.hits(mouseX,mouseY)==True:
            Screen1.opacity = 100
            Screen3.opacity = 0
            balance.opacity = 100

            app.screens = 1 
            
        if app.buy1Button.hits(mouseX,mouseY)==True:
            playerBank.reduceBalance(stock1.price)
            stock1.shares += 1
        if app.sell1Button.hits(mouseX,mouseY)==True:
            amount = stock1.liquidate()
            if amount != "You don't have anything to liquidate":
                playerBank.balance += amount
                
        if app.buy2Button.hits(mouseX,mouseY)==True:
            playerBank.reduceBalance(stock2.price)
            stock2.shares += 1
        if app.sell2Button.hits(mouseX,mouseY)==True:
            amount = stock2.liquidate()
            if amount != "You don't have anything to liquidate":
                playerBank.balance += float(amount)
                
        if app.buy3Button.hits(mouseX,mouseY)==True:
            playerBank.reduceBalance(stock3.price)
            stock3.shares += 1
        if app.sell3Button.hits(mouseX,mouseY)==True:
            amount = stock3.liquidate()
            if amount != "You don't have anything to liquidate":
                playerBank.balance += amount
        
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
        file.write("stock1.shares= " + str(stock1.shares) + "\n")
        file.write("stock1.rate= " + str(stock1.rate) + "\n")
        file.write("stock1.price= " + str(stock1.price) + "\n")

        file.write("stock2.shares= " + str(stock2.shares) + "\n")
        file.write("stock2.rate= " + str(stock2.rate) + "\n")
        file.write("stock2.price= " + str(stock2.price) + "\n")

        file.write("stock3.shares= " + str(stock3.shares) + "\n")
        file.write("stock3.rate= " + str(stock3.rate) + "\n")
        file.write("stock3.price= " + str(stock3.price) + "\n")

        file.write("day#= " + str(int(app.daycounter)))

cmu_graphics.run()