##Caden Beaty
##10/20/2024
##P3HW1_debug
##Fixing bugs in the code to accurately produce a letter grade.


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


# add grades entered to a list

grades = set([mod_1, mod_2, mod_3, mod_4, mod_5, mod_6])
# TO DO: determine lowest, highest , sum and average for grades
print()
print('------------Results-----------')
print(f'{"Lowest Grade:":<15} {min(grades)}')
print(f'{"Highest Grade:":<15} {max(grades)}')
print(f'{"Sum of Grades:":<15} {sum(grades)}')
print(f'{"Average:":<15} {sum(grades)/6:.2f}')
print('-------------------------------')
avg = float(f'{sum(grades)/6:.2f}')
# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
     print('Your grade is: B')
elif avg >= 70:
     print('Your grade is: C')
elif avg >= 60:
      print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this




