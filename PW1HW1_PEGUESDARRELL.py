


#SummerFun

#3/7/23

#CTI-110 P1HW1-Travel Expense

#DarrellPegues

#


budget = int(input("Enter the budget: "))
print()

destination = input("Enter your destination: ")
print()

gas = int(input("Enter amount that you will spend on gas: "))
print()

accomodation = int(input("Enter amount that you will spend on accommodation: "))
print()

food = int(input("Enter amount that you will spend on food: "))
print()

# Calculate total expenses
gas_expenses = gas
food_expenses = food
total_expenses = gas_expenses + accomodation + food_expenses

# Calculate remaining balance
remaining_balance = budget - total_expenses

print("------------------------------Travel expenses----------------------------------")
print("Location: " + destination)
print("Initial budget: " + str(budget))
print()
print("Fuel: " + str(gas_expenses))
print("Accommodation: " + str(accomodation))
print("Food: " + str(food_expenses))
print()
print("Total expenses: " + str(total_expenses))
print("Remaining balance: " + str(remaining_balance))

