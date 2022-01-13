'''
Exercise Nahrazení v textu (13)
(\w)\w+( \w+)
\1.\2

Exercise Zen of Python (18)
[ao]\.       # Lines where there is letter a or o before . (dot)
\w           # Alphanumeric symbols
[Tt]{2}      # T letter (uppercase and lowercase) is repeated two times
[Tt]{1,2}    # T (uppercase and lowercase) letter is repeated 1 to 2 times
'''

# Exercise Name function (26)
import re

def type_name(name):
  cap_match = re.findall(r'\b([A-Z]\w*)\b', name)
  let_match = re.findall(r'[A-Za-z]+', name)

  if not cap_match:
      type_name(input('Try again, the name must start only with a capital letter:\n'))
  if not let_match:
      type_name(input('Try again, the name can contain only letters:\n'))
  if not cap_match and not let_match:
    return(print('Identification passed'))


type_name(input('Enter your name: '))


# Exercise 4 Ponechání pouze čísel (29)
import re

def only_digits(st):
  digits = re.sub(r'[\D]', '', st)
  if digits:
    print(digits)
    return
  else:
    print('There are no digits, length = ', len(digits))
    return


only_digits(input('Enter digits: '))
