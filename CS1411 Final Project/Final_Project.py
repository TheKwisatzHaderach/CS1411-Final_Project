#makeChange()
#requires a register.txt file with amount of "Twentys:", "Tens :","Fives:","Ones:","Quarters:", "Dimes:", "Nickels:", "Pennies:
#file should look like 5 10 15 20 20 20 20 20 which means the register has 5 twentys, 10 tens, 15 fives, 20 ones, 20 quarters etc...
#register.txt example: 5 10 15 20 20 20 20 20
#Inputs: total cost and Cash given by user
#Outputs: False if register.txt isnt found
#False if cash < total
#False if not enough change in register
#True with change values printed also updates register with new totals
def makeChange(total, cash): #(makeChange() made by Sterling)
    total = int(total*100)#to avoid float innacuracy problems
    cash = int(cash*100) #to avoid float innacuracy problems
    money = 0
    changeValues = []
    names = ["Twentys:", "Tens :","Fives:","Ones:","Quarters:", "Dimes:", "Nickels:", "Pennies:"] #list representing registers
    values = [2000,1000,500,100,25,10,5,1]
    if(cash < total): #makes sure enough cash was given
        print("You did not give enough cash, please give", total, "dollars")
        return False
    try:#exception handling to make sure register file exist
        with open("register.txt") as f:
            for line in f:
                line = line.split() # to deal with blank 
            if (line):            # lines (ie skip them)
                registerValues = [int(i) for i in line]
    except FileNotFoundError:
        print("Your register is not open, please exit the program and open the register by creating a register.txt file with the cash couts inside")
        return False
    change = cash - total
    totalChange = cash - total
    for i in range(0,8): # calculates change
        if(change >= values[i]): #marks change value
            temp = int(change//values[i])
            if(temp > registerValues[i]):
                changeValues.append(registerValues[i])
                print(change,"1")
                change = change - (registerValues[i]*values[i])
                print(change,"2")
                registerValues[i] = 0
            else: 
                changeValues.append(temp)
                change = change - (temp*values[i])
                registerValues[i] = registerValues[i] - temp
        else:
            changeValues.append(0)
    if(change > 0):
        print("This register does not have enough change, please give a lower cash value so that we can complete your order. ")
        return False
    for x in range(0,8): # prints change exact values
        print(names[x], changeValues[x])
    with open("register.txt", "w") as w: #updates register
        for x in registerValues:
            w.write(str(x))
            w.write(" ")
    print("Total Change:",(totalChange/100))
    return True

#findItem() passes in the user inputted item and a items dictionary with the corresponding prices
#the function checks if the item exist and return corresponding item price as float if it does and return False if item dosent exist
def findItem(item,iDict): # pass in item from user and inventory dictionary (findItem() made by Nate)
    #checks if item exist
    try:
        return float(iDict[item]) # returns item price as float
    except KeyError:
        return False #if item is not found  

#main passes in a dictionary with the items as the key and price as the values
#has exception handling for user inputs as floats
def main(itemDict): #(made by Garrett)
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
    while(True): #exception handling looking for float and exit
        cash = input("Enter how much cash you want to pay with: ")
        if(cash.lower() == "exit"):
            return False
        try:
            cash = float(cash)
            makeChange(total,cash)
            break
        except ValueError:
            print("Please enter a float")
                           
            
    print("Thanks for coming!")
    print(" ")
    print(" ")
    return False

#main run of the program (main() Made by Nate)
import time #imports time module
import csv #imports csv module to read csv files easier
itemsList = [] #empty list 
with open('inventory.csv','r') as f: #Opens file before while loop so that file is only opened once This imporves program speed
    inventoryDict = {}#empty dictionary for items
    reader = csv.reader(f) #csv.reader reads csv file csv is module .reader() is function
    for row in reader: #reads each row as list
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
        print("\n")
        print("\n")
        print("\n")

