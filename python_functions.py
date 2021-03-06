# 2 cviceni na zaklady funkci(8) 
# exercise 1
def division(a, b):
    return a/b

print(division(27, 7))

# exercise 2
def lst_sum():
    '''I had to look for tips on how to get input separated by spaces. I chose the string .split() method.'''
    lst_num = [int(elements) for elements in input('Type list of numbers separated by space: ').split()]
    total = 0
    for num in lst_num:
        total += num
    return total


print(lst_sum())

# Lambda funkce (12)
compare_list = (lambda lst: print('small list') if len(lst) <= 5 else print('big list'))
compare_list([int(nmbrs) for nmbrs in input('Type list of numbers separated by space: ').split()])

# Funkce s jednim parametrem (21)
s = '''Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers, where’s the peck of pickled peppers Peter Piper picked?'''

def string_upper_lower(s):
    low = 0
    up = 0
    for symbol in s:
        if symbol.islower():
            low += 1
        elif symbol.isupper():
            up += 1
    low = '\nLowercase letters: ' + str(low)
    up = '\nUppercase letters: ' + str(up)
    return print(s, low, up)


string_upper_lower(s)

# Funkce s dvema parametry (22)
def meal_vouchers(l_cost, v_value):
    if v_value == False:
        print('Impossible value of voucher')
    else:
        pay_cash = print('Pay in cash: ' + str(l_cost % v_value))
        pay_voucher = print('Pay in meal vouchers: ' + str(l_cost // v_value) + ' pcs, ' + str(v_value) + ' CZK each')
        return pay_cash, pay_voucher


meal_vouchers(int(input('Lunch cost: ')), int(input('Meal voucher value: ')))

# Rekurzivni funkce (24)
def compute_factorial(n):
  if n < 0:
    s = 'The factorial is only defined for non-negative integers.'
    return s
  elif n == 0:
    return 1
  return n * compute_factorial(n-1)


print(compute_factorial(int(input('Factorial of a number: '))))
