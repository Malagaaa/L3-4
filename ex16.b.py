#    Afişaţi următoarele patternuri:                                  
#           # # # # # # #                                
#           # # # # # #                             
#           # # # # #                           
#           # # # #                     
#           # # #                  
#           # #                       
#           #

n = 8  # Numărul de linii
for i in range(n, 0, -1):
    for j in range(i):
        print("# ", end="")
    print()