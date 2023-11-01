#    Afişaţi următoarele patternuri:                                  
#           # # # # # # #                               
#           # #       # #                          
#           #   #   #   #                        
#           #     #     #                
#           #   #   #   #            
#           # #       # #            
#           # # # # # # # 

n = 7  # Numărul de linii
for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1 or i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("# ", end="")
        else:
            print("  ", end="")
    print()