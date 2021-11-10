# Exercie on page 12 (Seznamy)

names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef','Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal', 'Lenka', 'Katerina']
name = input('Type your name ')

if  (name in names_list) == True:
    print('Indetification passed')
else:
    print('Indetification failed')
