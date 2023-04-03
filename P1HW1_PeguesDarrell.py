Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #SummerFunWeekend
>>> #April7-9
>>> #CTI-110P1HW1-TravelExpense
>>> #DarrellPegues
>>> budget = float(input("Enter your budget for the trip: $"))
Enter your budget for the trip: $1200
>>> destination = input("Enter your travel destination: ")
Enter your travel destination: MyrtleBeach,SC
>>> gas_expense = float(input("Enter your estimated gas expense: $"))
Enter your estimated gas expense: $80
>>> accommodation_expense = float(input("Enter your estimated accommodation expense: $"))
Enter your estimated accommodation expense: $450
>>> food_expense = float(input("Enter your estimated food expense: $"))
Enter your estimated food expense: $150
>>> other_expenses = float(input("Enter any other expenses (e.g. souvenirs): $"))
Enter any other expenses (e.g. souvenirs): $50
>>> total_expenses = gas_expense + accommodation_expense + food_expense + other_expenses
>>> #total_expenses = gas_expense + accommodation_expense + food_expense + other_expenses
>>> remaining_budget = budget - total_expenses
>>> #remaining_budget = budget - total_expenses
>>> print("Travel Destination:", destination)
... print("Total Expenses: $", format(total_expenses, ".2f"))
... if remaining_budget < 0:
... print("You are over budget by $", format(abs(remaining_budget), ".2f"))
... else:
... print("Remaining Budget: $", format(remaining_budget, ".2f"))
SyntaxError: multiple statements found while compiling a single statement
>>> print("Travel Destination:", destination)
... print("Total Expenses: $", format(total_expenses, ".2f"))
... if remaining_budget < 0:
... print("You are over budget by $", format(abs(remaining_budget), ".2f"))
... else:
... print("Remaining Budget: $", format(remaining_budget, ".2f"))budget = float(input("Enter your budget for the trip: $"))
SyntaxError: multiple statements found while compiling a single statement
