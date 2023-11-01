#Scrieți un program care va număra "Mississippi" - way!
#Va afișa numerele însoțite de cuvântul Mississippi.
#hint:
#import time
#time.sleep(1)

import time

import time

n = int(input("Introduceți un număr: "))

for i in range(1, n + 1):
    print(i)
    time.sleep(1)  # Aștept 1 secundă între afișarea numărului
    print("Mississippi")
    time.sleep(1)  # Aștept 1 secundă între afișarea "Mississippi"