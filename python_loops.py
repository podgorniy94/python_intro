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

# Exercise on page 25 (Nákupní seznam)
items = ['Diapers', 'Peanuts','Butter', 'Cheese', 'Milk', 'Yogurt', 'Eggs','Bread', 'Shrimp', 'Coffee']
item = input('What item do you need? ')
item = item.capitalize()

for i, search in enumerate(items):
    if search == item:
        print(item + ' is already on the list')
        break
    if i == len(items) - 1:
        items.append(item)
        print(items)
        break

# Exercise on page 28 (List comprehension)
numbers = range(5,10)
exp = [x*x for x in numbers]
fav = [str(x) + ' is my favorite number!' for x in numbers]
print(exp), print(fav)

# Exercise on page 29 (GATTACA)
seq = 'ACTGCTCAAG'
inlist = [i for i, x in enumerate(seq) if x == 'A']
print(inlist)
# The second solution
seq = 'ACTGCTCAAG'
no_enum = [i for i in range(len(seq)) if seq[i] == 'A']
print(no_enum)

# Exercise on page 31 (Slovníky)
scores = {'John' : 10, 'Emily' : 35, 'Matthew' : 50}
new_scores = {name: value*3 for (name, value) in scores.items()}
print(new_scores)
