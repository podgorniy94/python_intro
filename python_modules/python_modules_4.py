# Vytvořit skript na odstraňování písmen (26)
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("string", help="main string")
parser.add_argument("letter", help="specified letter")
args = parser.parse_args()

word = ''

for i in args.string:
    if i != args.letter:
        word += i

print(word)
