#    Afişaţi următoarele patternuri:                                  
#           # # # # # # #                               
#             #                           
#               #                           
#                 #                     
#                   #                  
#                     #                    
#           # # # # # # # 

n = 7  # Numărul de linii
for i in range(n):
    for j in range(n):
        if i == 0 or j == i or i == n - 1:
            print("# ", end="")
        else:
            print("  ", end="")
    print()