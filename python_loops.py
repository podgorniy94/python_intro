# Exercie on page 12 (Seznamy)

names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef','Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal', 'Lenka', 'Katerina']
name = input('Type your name ')

if  (name in names_list) == True:
    print('Indetification passed')
else:
    print('Indetification failed')

# Exercie on page 20 (Smyčky)
d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'}

name = input('Tape your name: ')
name = name.lower()

for letters in name:
    print(letters + ' = ' + d[letters])

# Exercise on page 21 (Trasnponovaná matice)
# new_list = [expression for member in iterable]
matrix = [[1,2,3], [4,5,6], [7,8,9]]

transpose = [[row[i] for row in matrix] for i in range(len(matrix))]
for lst in transpose:
        print(lst)
