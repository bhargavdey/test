phrase = "Giraffe Academy"
#index-   0123456789
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0] + phrase[2])
print(phrase.index("i"))
print(phrase.index("G") + phrase.index("r"))
print(phrase.index("Acad")) # this will print starting point of Acad
print(phrase.replace("Giraffe", "Elephant"))
print(phrase)