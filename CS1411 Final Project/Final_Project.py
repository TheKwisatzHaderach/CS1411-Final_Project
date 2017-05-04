def makeChange(total, cash):
    money = 0
    changeValues = []
    names = ["Twentys:", "Tens :","Fives:","Ones:","Quarters:", "Dimes:", "Nickels:", "Pennies:"]
    values = [20.00,10.00,5.00,1.00,0.25,0.10,0.05,0.01]
    if(cash < total):
        print("You did not give enough cash, please give", total, "dollars")
        return False
    try:
        with open("register.txt") as f:
            for line in f:
                line = line.split() # to deal with blank 
            if (line):            # lines (ie skip them)
                registerValues = [int(i) for i in line]
    except FileNotFoundError:
        print("Your register is not open, please exit the program and add register.txt file to your path with the cash couts inside")
        return False
    change = cash - total
    totalChange = cash - total
    for i in range(0,8):
        if(change >= values[i]):
            temp = int(change//values[i])
            if(temp > registerValues[i]):
                changeValues.append(registerValues[i])
                change = change = change - (registerValues[i]*values[i])
                registerValues[i] = 0
            else: 
                changeValues.append(temp)
                change = change - (temp*values[i])
                registerValues[i] = registerValues[i] - temp
        else:
            changeValues.append(0)
    print(change)
    if(change > 0):
        print("This register does not have enough change, please give a lower cash value so that we can complete your order. ")
        return False
    for x in range(0,8):
        print(names[x], changeValues[x])
    with open("register.txt", "w") as w:
        for x in registerValues:
            w.write(str(x))
            w.write(" ")
    print("Total Change:",totalChange)
    return True


def findItem(item,iDict): # pass in item from user and inventory dictionary
    #checks if item exist
    try:
        return float(iDict[item]) # returns item price as float
    except KeyError:
        return False #if item is not found  

#main passes in a dictionary with the items as the key and price as the values
def main(itemDict):
    import time #imports time module
    total = 0.00
    change = 0.00
    print("\n")
    print("Hello welcome to The Grocery Store!")
    time.sleep(2) #waits 2 seconds
    print("If at any time you would like to exit please enter exit")
    time.sleep(2)
    print("When you are finished entering your items please enter done")
    time.sleep(2)
    print("\n")
    
    while(True): #Taking in items until done or exit is entered
        item = input("Enter item: ")
        item = item.lower()
        if(item == "exit"):
            return False #exits main 
            break
        elif(item == "done"):
            break
        else:
            price = findItem(item, itemDict) #calls findItem passes in the item entered by user and the Inventory Dictionary
            if(price == False):
                print("Item not found please make sure you enter the item correctly")
            else:
                total = total + price
                
    print("Your total is:",total)
    while(True):
        cash = (input("Please enter the cash amount you would like to pay with as a float: ")) #Taking user payment
        try:
            cash = cash.lower() 
            if(cash == "exit"):
                return False
            elif(item == "done"):
                break
            else:
                print("Not a valid input")
        except AttributeError: #Haappens if user enters number
            pass
        
    while(True): #checks if its a float
        try:
            cashf = float(cash)
            checker = makeChange(total,cashf)
            if (checker == False):
                pass
            else:
                break
        except ValueError:
            print("Please make sure you enter a float")
            
    print("Thanks for coming!")
    check = input("If you would like to go again enter anything, if you would like to exit enter exit: ")
    print(" ")
    print(" ")
    if(check.lower() == "exit"):
        return False
    else:
        return True

import time #imports time module
import csv #imports csv module to read csv files easier
itemsList = [] #empty list 
with open('inventory.csv','r') as f: #Opens file before while loop so that file is only opened once This imporves program speed
    inventoryDict = {}#empty dictionary for items
    reader = csv.reader(f) #csv.reader reads csv file csv is module .reader() is function
    for row in reader: #reads each row as list
        print(row)
        k,v = row #k is the items and v is the price k,v are strings
        itemString = ' '.join(map(str, row)) #takes list an converts to 1 string for easier console printing
        itemsList.append(itemString) #adds to item list
        inventoryDict[k] = v #creates dictionary
#file is closed
        
while(True): #start of User program
    print("Available Items:")
    for itemandprice in itemsList: #prints item and price
        print (itemandprice)
    print("\n")
    input("Press Enter to start!")
    if(main(inventoryDict)): #calls main function passes in invernotry dictionary as argument
        pass 
    else:
        print("Session Exited...")
        time.sleep(3)

