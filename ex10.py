#Scrieți un program care va cere utilizatorului să introducă o parolă pentru a merge mai departe!

parola_corecta = "parola123"  # Setați aici parola corectă

while True:
    parola = input("Introduceți parola: ")
    if parola == parola_corecta:
        print("Parola este corectă. Puteți merge mai departe.")
        break
    else:
        print("Parola este incorectă. Încercați din nou.")