begin_balance = float(input("Enter the beginning balance $"))
apy = float(input("Enter the interest rate as a percent 5.2% = 5.2 "))
month_deposit = float(input("How much money to you want to invest each month $"))
years = int(input("How many years is this investment going to be? "))

rate = apy/100
total_months = years * 12
month_no = 1
line_ct = 0
max_lines = 15