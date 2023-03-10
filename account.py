

# Task 4
#will display the balance
def show_balance(balance):
    print("Current Balance: $" + str(balance))

# will ask the user to enter amount to deposit
def deposit():
    return float(input("Enter amount to deposit: "))


# will ask the user to enter amount to be withdrawn 
def withdraw(balance):
    amountList = [20,40,60,80,100,200]
    #bonus 3
    #display fast menu to withdraw from
    #start loop
    while True:
        print("                  === Select an amount to withdraw ===     ")
        print(" ---------------------------------------------------------------")
        print("|            $20                |              $80              |")
        print(" ---------------------------------------------------------------")
        print("|            $40                |              $100             |")
        print(" ---------------------------------------------------------------")
        print("|            $60                |              $200             |")
        print(" ---------------------------------------------------------------")
        print("|1- Enter Different Amount >    |2-            Cancel           |")
        print(" ---------------------------------------------------------------\n")

        opt = int(input("Enter Option: "))

        if opt == 2:
            return 0
        elif opt == 1:
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Where are you going to get that kind of money?")
                return 0
            else:
                return amount
        elif opt in amountList and opt < balance:
            return opt
        else:
            print("Where are you going to get that kind of money?")
            return 0
    #end loop
# will say goodbye to the current user
def logout(name):
    print('Goodbye', name + "!")
