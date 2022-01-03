# Tvoření seznamu (34)
lst = ["casserole", "book", "knife", "water bottle", "fishing rod"]

with open ("hello.txt", "w", encoding="ASCII") as f:
    for i, w in zip(range(len(lst)), lst):
        f.write(str(i + 1) + '\t' + w + '\n')
