#Challenge: 
#test = "iiiLikePythonLikeILikeIcecream"
#print(test.index('Like'))
#print(test.rindex('Like'))
#cod care afișează poziția Like-ului median

test = "iiiLikePythonLikeILikeIcecream"
cuvant_cautat = "Like"

index_primului = test.find(cuvant_cautat)
index_urmator = test.find(cuvant_cautat, index_primului + 1)

if index_urmator != -1:
    print("Indexul celui de-al doilea cuvant 'Like' este:", index_urmator)
else:
    print("Nu exista un al doilea cuvant 'Like' in sir.")