# Exercise Oprava kódu (6) 
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[3])


# Exercise Oprava kódu (7)
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = 'a'
        print(message)
    else:
        message = "b"
        print(message)


# Exercise Dělení čísel (13)
def div_two_int(a):
  while True:
    try:
      a = int(a)
      break
    except ValueError:
      a = input('The value must be an integer, try again: ')

  b = input('Enter the second integer value: ')
  sec_value(a, b)

def sec_value(a, b):
  while True:
    try:
      b = int(b)
      break
    except ValueError:
      b = input('The value must be an integer, try again: ')

  try:
    print('The result = ', a/b)
  except ZeroDivisionError:
    b = input('Division by zero is not possible, try again: ')
    sec_value(a, b)


div_two_int(input('Enter the first integer value: '))


# Exercise Debugování (16)
year = int(input("Greetings! What is your year of origin? "))
if year <= 1900:
  print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
  print("That's totally the present!")
else:
  print("Far out, that's the future!")

# Exercise Dotaz na uživatelské jméno (12)
import re

name = input('Type your name: ')

if re.findall(r'\d+', name):
    raise Exception("Digits")
if re.findall(r'\s+', name):
    raise Exception("Spaces")
if re.findall(r'\b[a-z]\w+\b', name):
    raise Exception("Not capitalized")
print('Approved')
