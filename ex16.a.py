#    Afişaţi următoarele patternuri:                                  
#           #                                
#           # #                            
#           # # #                           
#           # # # #                     
#           # # # # #                  
#           # # # # # #                    
#           # # # # # # # 
#           # # # # # # # #

n = 8  # Numărul de linii
for i in range(1, n + 1):
    for j in range(i):
        print("# ", end="")
    print()