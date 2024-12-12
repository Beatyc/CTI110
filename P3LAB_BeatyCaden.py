##Caden Beaty
##10/20/2024
##P3Lab1
##Using if statements to calculate the most efficient change combination

money = float(input('Enter the amount of money as a float: $'))
dollar = 0
quarter = 0
dime = 0
nickel = 0
penny = 0
money = int(money*100)

dollar = money//100
money = money%100
quarter = money//25
money = money%25
dime = money//10
money = money%10
nickel = money//5
money = money%5
penny = money

if dollar == 1:
    print(dollar, 'Dollar')

if dollar > 1:
    print(dollar, 'Dollars')
    
if quarter == 1:
    print(quarter, 'Quarter')

if quarter > 1:
    print(quarter, 'Quarters')

if dime == 1:
    print(dime, 'Dime')

if dime > 1:
    print(dime, 'Dimes')

if nickel == 1:
    print(nickel, 'Nickel')

if penny == 1:
    print(penny, 'Penny')

if penny >= 1:
    print(penny, 'Pennies')

if money == 0:
    print('No change.')
