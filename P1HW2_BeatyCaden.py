##Caden Beaty
##9/29/2024
##P1HW2
##subtraction with multiple variables

print('This program calculates and displays travel expenses')
print()
print('Enter Budget:', end='')
budval=int(input())
print()
print('Enter your travel destination:', end='')
destval=input()
print()
print('How much do you think you will spend on gas?', end='')
gasval=int(input())
print()
print('Approximately, how much will you need for accomodation/hotel?', end='')
hotval=int(input())
print()
print('Last, how much do you need for food?', end='')
foodval=int(input())
print()
print('------------Travel Expenses------------')
print('location:', destval)
print('Initial Budget:', budval)
print()
print('Fuel:', gasval)
print('Accomodation:', hotval)
print('food:', foodval)
print()
print('Remaining Balance:', budval-gasval-hotval-foodval)