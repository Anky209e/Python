def col_sum(s):
    c = 0
    d = 0
    f = 0
    for i in s:
        c+=i[0]
        d+=i[1]
        f+=i[2]
    return c,d,f

def diagonal_sum(s):
    x = s[0][0]+s[1][1]+s[2][2]
    y = s[0][2]+s[1][1]+s[2][0]
    
    return x,y

def is_unique(s):
    temp = []
    for i in s:
        for j in i:
            temp.append(j)
    if len(set(temp)) == len(temp):
        return True
    return False

def is_magic_sqaure(s):
    c,d,f = col_sum(s)
    x,y = diagonal_sum(s)
    if x == y == c == d == f == sum(s[0]) == sum(s[1]) == sum(s[2]) and is_unique(s):
        return True
    return False

def get_all_magig_squares():
    evens = [2,4,6,8]
    odds = [1,3,5,7,9]
    for i in evens:
        for j in odds:
            for k in evens:
                for a in odds:
                        for c in odds:
                            for p in evens:
                                for q in odds:
                                    for r in evens:
                                        sqaure = [[i,j,k],[a,5,c],[p,q,r]]
                                        if is_magic_sqaure(sqaure):
                                            print(sqaure)
                                    




def get_min_cost(s):
    all_squares =     [
                        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
                        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],

                        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],

                        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],

                        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                        [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
                        
                    ]

    sum_store = []
    for square in all_squares:
        val_store = abs(s[0][0] - square[0][0]) + abs(s[0][1] - square[0][1]) + abs(s[0][2]-square[0][2]) + abs(s[1][0]-square[1][0]) + abs(s[1][1]-square[1][1]) + abs(s[1][2]-square[1][2]) + abs(s[2][0]-square[2][0]) + abs(s[2][1]-square[2][1]) + abs(s[2][2]-square[2][2])
        sum_store.append(val_store)

    print(min(sum_store))
    return min(sum_store)


if __name__=="__main__":
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]] 
    get_min_cost(s)