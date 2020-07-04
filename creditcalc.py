from math import ceil
print("Enter the credit principal:")
credit_principal = int(input())

print('What do you want to calculate?')
print('type "m" - for count of months,')
print('type "p" - for monthly payment:')
choose = input()
if choose.lower() == "m":
    print('Enter monthly payment:')
    monthly_payment = int(input())
    months_to_repay = credit_principal / monthly_payment
    if months_to_repay <= 1:
        print(f'It takes 1 month to repay the credit')
    else:
        print(f'It takes {round(months_to_repay)} months to repay the credit')
elif choose.lower() == "p":
    print('Enter count of months:')
    count_of_month = int(input())
    monthly_payment = credit_principal / count_of_month
    if monthly_payment % 1 == 0:
        print(f'Your monthly payment = {int(monthly_payment)}')
    else:
        last_payment = credit_principal - (count_of_month - 1) * ceil(monthly_payment)
        print(f'Your monthly payment = {ceil(monthly_payment)} with last month payment = {last_payment}')