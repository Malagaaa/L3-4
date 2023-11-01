#    Afişaţi următoarele patternuri:                                  
#           # # # # # # #                                
#             # # # # # #                             
#               # # # # #                           
#                 # # # #                     
#                   # # #                  
#                     # #                       
#                       # 

n = 8  # Numărul de linii
for i in range(n):
    for j in range(n):
        if j >= i + 1:
            print("# ", end="")
        else:
            print("  ", end="")
    print()