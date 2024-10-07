##Caden Beaty
##10/06/2024
##P2LAB2
##Using variables in a library

Car = {
  "Camaro": 18.21,
  "Prius": 52.36,
  "Model S": 110,
  "Silverado": 26
}
keys = Car.keys()
print(keys)
print()
model = input('Enter a vehicle to see its mpg: ')
print()
mpg = Car[model]
print(f'The {model} gets {mpg} mpg.')
print()
mile = float(input(f'How many miles will you drive the {model}? '))
print()
gallons = mile / mpg
print(f'{gallons:.2f} gallon(s) of gas are needed to drive the {model} {mile} miles.')
