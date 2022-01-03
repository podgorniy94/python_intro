def divide_two_numbers():
  while True:
    try:
      a = int(input('Enter the first integer value: '))
      break
    except ValueError:
      a = print('The value must be an integer, try again.')

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
