# 2 cviceni na zaklady funkci(8); exercise 1
def division():
    div = 22/7
    return div
print(division())
# exercise 2
def lst_sum():
    '''I had to look for tips on how to get input separated by spaces. I chose the string split () method.'''
    lst_num = [int(elements) for elements in input('Type list of numbers separated by space: ').split()]
    total = 0
    for num in lst_num:
        total += num
    print(total)
lst_sum()

# Lambda funkce (12)
compare_list = (lambda lst: print('small list') if len(lst) <= 5 else print('big list'))
compare_list([int(nmbrs) for nmbrs in input('Type list of numbers separated by space ').split()])
