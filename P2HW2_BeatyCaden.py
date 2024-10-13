##Caden Beaty
##10/13/2024
##P2HW2
##Creating a set and getting specific values from it.

m1 = float(input('Enter grade for Module 1: '))
m2 = float(input('Enter grade for Module 2: '))
m3 = float(input('Enter grade for Module 3: '))
m4 = float(input('Enter grade for Module 4: '))
m5 = float(input('Enter grade for Module 5: '))
m6 = float(input('Enter grade for Module 6: '))
nums = set([m1, m2, m3, m4, m5, m6])

print()
print('------------Results-----------')
print(f'{"Lowest Grade:":<15} {min(nums)}')
print(f'{"Highest Grade:":<15} {max(nums)}')
print(f'{"Sum of Grades:":<15} {sum(nums)}')
print(f'{"Average:":<15} {sum(nums)/6:.2f}')
print('-------------------------------')

##Pseudocode:
##Defining variables m1-m6 with user inputs
##Putting variables m1-m6 in a set
##Take the lowest value from the set and format the value left by 15 characters
##Take the higest value from the set and format the value left by 15 characters
##Add up the entire set and print the value and format the sum left by 15 characters
##Take the average of the set and round it by two decimal places then format the average left by 15 characters
