""""

Program that allows the user to access two different financial calculators: 
an investment calculator and a home loan repayment calculator.

"""""
# We import the module math to extend the list of mathematical functions allowed
import math

# Display that is shown as soon as the user start to use the program
print("investment       - to calculate the amount of interest you'll earn on your investment")
print("bond             - to calculate the amount you'll have to pay on a home loan")
print()
# Program asks user which option to choose 
selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Use of conditionals to calculate what the user has chosen 
if selection.lower() == "investment":
    P = float(input("What's the amount you are depositing? "))
    r = float(input("What's the interest rate? (only the number of the interest rate) "))
    t = float(input("How many years do you plan on investing? "))
    interest = input("Do you want simple or compound interest? ")
    

    if interest == "simple":
         A = P*(1 + (r/100)*t)
         print ("The total amount once the simple interest has been applied is" , A)

    if interest == "compound":
         A = P * math.pow((1+(r/100)),t)
         print ("The total amount once the compound interest has been applied is" , A)

elif selection.lower() == "bond":
    P = float(input("What's the present value of the house? "))
    i = float(input("What's the annual interest rate? "))
    n = float(input("How many months do you plan to take to repay? "))    

    # Convert annual interest rate to monthly and percentage to decimal
    r = (i / 100) / 12

    # Calculate monthly repayment using the correct formula
    repayment = (P * r * (1 + r)**n) / ((1 + r)**n - 1)
    print("The user will have to repay", round(repayment, 2), "each month")

# Message to let the user knows that the program only accept one of the options provided in the menu 
else:
    print ("The option you have entered is not valid, please enter one of the options from the menu above ")











