#finance calculator to calculate peoples finances  
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your montly expenses:"))
# monthly savings calculations 
monthly_savings = monthly_income - monthly_expenses 
# annual savings with interest calculations 
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
# printing of monthly savings and projected annual savings
print(f"Your monthly savings is {monthly_savings}")
print(f"Your projected annual savings with 5% interest will be {projected_savings}")

