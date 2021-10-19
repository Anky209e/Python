grade = 73
for i in range(grade,100):
    if i % 5 ==0:
        if grade >= 38:
            if i - grade < 3: 
                grade = i
                print(grade)
                break
            elif i-grade >= 3 :
                print(grade)
                break       
        else:
            print("fail",grade)
            break
        