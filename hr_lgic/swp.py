def permutations(chars, st = 0):
    if st == len(chars):
        
        print ("".join(chars))
    for i in range(st, len(chars)):
        
        chars_c = [c for c in chars]
         
        chars_c[st], chars_c[i] =chars_c[i], chars_c[st]
        
        permutations(chars_c, st + 1)

print (permutations ('abc'))