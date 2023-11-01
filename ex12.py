#Scrieți un program care va modifica toate vocalele în majuscule.

text = input("Introduceți un text: ")
text_modificat = ""

for caracter in text:
    if caracter.lower() in "aeiou":
        text_modificat += caracter.upper()
    else:
        text_modificat += caracter

print("Textul modificat cu vocalele în majuscule este:", text_modificat)