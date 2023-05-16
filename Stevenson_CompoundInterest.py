#This program will calculate compound interest earn by the account after a specified number of years
def compoundInterest():
    #asking the user for input
    p = float(input("Enter the amount of principal amount to be deposited: "))
    r = float(input("Enter annual interest rate paid by the account: "))
    n = int(input("Enter the number of times per year that the interest is compounded: "))
    t = float(input("Enter the number of years the account will be left to earn interest: "))

    #caluclating the balance of the account after a specified number of years
    amount = p*(1+(r*.01)/n)**(n*t)

    print("This amount of money will be in the account after ", t, "years:", round(amount,2))

compoundInterest() #main function gets called