#Ghicește numărul!
#Scrieți un program care va genera un număr aleatoriu (google it ;) ) și va cere utilizatorului să ghicească numărul! Programul se va termina când numărul va fi ghicit.
#contorizați numărul de încercări 
#adăugați mesaje ajutătoare ("prea mic" sau "prea mare")
#adăugați mesaj care să indice intervalul curent în care se află numărul, conform încercărilor utilizatorului

import random

numar_aleatoriu = random.randint(1, 100)  # Generați un număr aleatoriu între 1 și 100
numar_incercari = 0

print("Bun venit la jocul de ghicit numere!")

while True:
    ghicire = int(input("Ghiciți numărul: "))
    numar_incercari += 1

    if ghicire < numar_aleatoriu:
        print("Prea mic! Încercați din nou.")
    elif ghicire > numar_aleatoriu:
        print("Prea mare! Încercați din nou.")
    else:
        print(f"Bravo! Ați ghicit numărul {numar_aleatoriu} în {numar_incercari} încercări.")
        break