# Použití Argparse (23) 
import argparse
import string
parser = argparse.ArgumentParser()

parser.add_argument('string', help='The string in which letters are supposed to be counted')
parser.add_argument('-v', '--vowels', help='to count only vowels', action='store_true')
parser.add_argument('-c', '--consonants', help='count only consonants', action='store_true')
args = parser.parse_args()

alphabet = string.ascii_letters
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
lst  = list(args.string)

up_vowels = []
for i in range(len(vowels)):
    up_vowels.append(vowels[i].upper())

consonants = []
for i in alphabet:
    if i not in vowels and i not in up_vowels:
        consonants.append(i)

def count_letters(var):
    for i in var:
        if i in lst:
            print(i, ' ',  lst.count(i))
    return

if args.vowels:
    count_letters(vowels)
elif args.consonants:
    count_letters(consonants)
else:
    count_letters(alphabet)


