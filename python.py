balance = 2000
while True:
    print("1.check balance")
    print("2.deposite")
    print("3.cash widrawl")
    print("4.exit")

    n = int(input("what you wanna do:"))
    if(n==1):
        print("your balance is: ",balance)
    elif(n==2):
        deposite = int(input("enter your deposite"))
        if(deposite<0):
            print("invalid amount")
        else:
            balance += deposite
            print(F"your deposite is {deposite}\nyour new balance is {balance}")
    elif(n==3):
        wid = int(input("enter your widrawal amount"))
        if(wid>balance):
            print("unvalid amount")
        else:
            balance -= wid
            print(f" widrawl money:{wid}\nyour balance now :{balance}")
    else:
        print("thank you")
        break            