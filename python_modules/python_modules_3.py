# Vytvořit skript na počítání písmen (25)
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("substring", help="substring in string")
parser.add_argument("string", help="main string")
args = parser.parse_args()

occur = args.string.count(args.substring)

print("String", args.substring, "occurred", occur, "times in string", args.string)


