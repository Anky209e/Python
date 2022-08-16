s = "12:23:01PM"


data = s.split(":")

if data[2].endswith("AM"):
    if data[0] == '12':
        data[0] = '00'

elif data[2].endswith("PM"):
        if int(data[0]) >= 1 and int(data[0]) < 12:
            data[0] = str(int(data[0])+12)
        elif data[0] == '12':
            data[0] = '12'   
    
ans = ":".join(data)
print(ans[:-2])


