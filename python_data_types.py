# task on page 10
print (1256983%28) 

# task on page 16
print (12**52/15>8 or 3**5>100) # exercise 1
print (not(5*3**3==900/75)) # exercise 2

# task on page 21
print('[[]]'[:2] + 'PYTHON' + '[[]]'[2:]) # exercise 1
print ('Python'[4::1]*3) # exercise 2
print ('Perl'[2]*6) # exercise 3

# task on page 24
up = 'python' # exercise 1
print (up[:3].upper()+up[3:])
'python'[0]*len('python') # exercise 2

# task on page 27
print(7+3*2) # The multiplication is performed first, and then the addition.
print('7' + str(3*2)) # Product in brackets converted into a string and concatenated with another string.
print('7' + '3*2') # Adding strings because they aren't numbers.
# print('7' + 3*2) A string can only concatenate to a string but not an integer.

# task on page 31
hobby = 'fitness' # exercise 1
'My hobby is {}.'.format(hobby)
import datetime # exercise 2
date = datetime.datetime(2018, 11, 1) 
print ('{:%m/%d}'.format(date))

# task on page 37
my_hobbies = ['fitness', 'tea', 'driving', 'running']
print (my_hobbies[0])
print (my_hobbies[-1])
del my_hobbies[-1]

# task on page 38
cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
cities.sort()
'*'.join(cities)

# task on page 49
alphabet = set ('abcdefghijklmnopqrstuvwxyz')
zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
print (alphabet.difference(zen))

# task on page 50
d = {'payton':'An interpreted, object-oriented programming language'} # exercise 1
d['python'] = d['payton']
del d['payton']
print (d)
contacts = {('Ryan', 'Gosling'):'+1-257-530-202'} # exercise 2

# task on page 51
info = {('Name', 'Surname'):('John', 'Doe')}
print(info['Name','Surname'][0] + '_' + info['Name','Surname'][1])
