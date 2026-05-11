# Expense Tracker Application

expenses=[]
print("Welcome to Expense Tracker ")
def take_input():
     
    amount=input("Enter a Amount of expenses : ")
    category=input("Enter a Category : ")
    desc=input("Give Description for Expense : ")
    date = input("Enetr a date ")

    expense ={
        "amount":amount,
        "category":category,
        "description":desc,
        "date":date
    }
    expenses.append(expense)
