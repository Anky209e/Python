s = '1:00:1'
format = "PM"
arr = s.split(':')
int_arr = [int(a) for a in arr]
fnl_time = []
if format == 'PM':
    if int_arr[0] == 12:
        int_arr[0] = "12"
        fnl_time.append(int_arr[0])
    else :
        int_arr[0] = str(12 + int_arr[0])
        fnl_time.append(int_arr[0])

elif format == 'AM':
    if int_arr[0] == 12:
        int_arr[0] = "00"
        fnl_time.append(int_arr[0])
    else:
        fnl_time.append(str(int_arr[0]))

fnl_time.append(arr[1])
fnl_time.append(arr[2])
fnl_time.append(format)
print(':'.join(fnl_time))