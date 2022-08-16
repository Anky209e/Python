a = [2,6]
b = [24,36]


def thefuckening(a, b):
    count = 0
    do_divide = True
    for i in range(a[-1], b[0]+1):
        for j in a:
            if i%j != 0:
                do_divide = False
                break
        if do_divide:
            for j in b:
                if j%i != 0:
                    do_divide = False
                    break 
        if do_divide:
            count += 1
        do_divide = True    
    return count

print(thefuckening(a,b))