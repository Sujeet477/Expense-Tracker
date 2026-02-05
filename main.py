# Expence Tracer
my_list = list()

print("Welcome to Expense Tracer : ")

while True:
    print("===MENU===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))

# Add Expense
    if(choice == 1):
        date = input("Enter Your Date : ")
        category = input("Enter Type of Expense :")
        description = input("Add more details : ")
        amount = float(input("Enter the amount :"))
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        my_list.append(expense)
        print(" \n Done... Expense is added succesfully ")

# View All Expense
    elif(choice == 2):
        if(len(my_list) == 0):
            print("No Expenses Added")
        else:
            print("===Your all Expenses===")
            count = 1
            for eachExpense in my_list:
                print(f"Expense Number {count} -> {eachExpense['date']}, {eachExpense['category']},{eachExpense['description']}, {eachExpense['amount']}")
                count += 1

# View Total Spending
    elif(choice == 3):
        total = 0
        for eachExpense in my_list:
            total = total + eachExpense["amount"]

            print("\n Total Expense :", total)
            
# Exit
    elif(choice == 4):
        print("Thank You... for visiting here...")
        break

    else:
        print("Invalid Choice...Please Try Again...")