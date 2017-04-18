#requires a register.txt file with amount of "Twentys:", "Tens :","Fives:","Ones:","Quarters:", "Dimes:", "Nickels:", "Pennies:
#file should look like 5 10 15 20 20 20 20 20 which means the register has 5 twentys, 10 tens, 15 fives, 20 ones, 20 quarters etc...
#register.txt example: 5 10 15 20 20 20 20 20
#Inputs: total cost and Cash given by user
#Outputs: False if register.txt isnt found
#False if cash < total
#False if not enough change in register
#True with change values printed also updates register with new totals

total = 11.75
cash = 20.00

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
        print("Your register is not open, please exit the program and open the register by creating a register.txt file with the cash couts inside")
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
    

makeChange(total,cash)
