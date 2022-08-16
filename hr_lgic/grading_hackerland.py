

grades = [98,23,12]

for i in range(len(grades)):
    if 100 > grades[i] >= 38 :
        print(grades[i])
        next_multi = [i for i in range(grades[i],101) if i%5==0][0]
        if next_multi-grades[i] < 3:
            grades[i] = next_multi

print(grades)
            