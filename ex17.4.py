numar = int(input("Introduceti un numar!"))
strat=1
while numar >= strat:
      numar = numar - strat
      strat = strat + 1 
else:
     print("Piramida are", strat-1, "nivele.")