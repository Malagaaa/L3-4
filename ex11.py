#Scrieți un program care va afișa doar consoanele dintr-un text citit din consolă.

text = input("Introduceți un text: ")
consoane = ""

for caracter in text:
    if caracter.isalpha() and caracter.lower() not in "aeiou":
        consoane += caracter

print("Consoanele din text sunt:", consoane)