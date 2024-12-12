##Caden Beaty
##10/26/2024
##P3HW2
##Calculating the gross and overtimepay of an employee.


name = input("Enter employee's name: ")
hours = float(input('Enter number of hours worked: '))
rate = float(input("Enter employee's pay rate: "))
over = hours - 40
if hours > 40:
    base = rate*40
    overpay = (rate*1.5)*over
    total = base+overpay
else:
    base = hours*rate
    total = base
print('---------------------------')
print('Employee name:', name)
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<11}{"OverTime":<11}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay"}')
print('--------------------------------------------------------------------------------')
print(f'{hours:<15}{rate:<11}{over:<11}{overpay:<15}${base:<15}${total}')


##Pseudocode:
##Defining the name of an employee named by the user
##Defining the amount of hours the given employee has worked
##Defining the rate of pay for the employee
##If the hours the employee worked is over 40 than define the overtime pay rate
##Or if the hours aren't over forty then calculate normally without overtime rate
##then display the employee's name and all of the hour and payment numbers
