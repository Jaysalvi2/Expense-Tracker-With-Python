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
    
def dis():
    if(len(expenses)==0):
            print("Add expenses First")
    else:
         print()
         print("=== Here Is your all Expenses")
         print()
         count=1
         for r in expenses:
            
            print(f"{count},{r}")
            count+=1

while True:
    print()
    print
    print("==== MENU ====")
    print()
    print("1. Add Expenses :")
    print("2. View All Expenses :")
    print("3. Exit : ")

    choice=input("Enter a Choice : ")
    match choice:
        case "1":  
             take_input()
            
        case "2" :  
             dis()
            
        case "3" :
            print("Exit")
            break 
        case _:
            print("Enter a Valide Choice ")