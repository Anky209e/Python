# file io basic
# modes to open file
# read mode "r" -->open file for reading
# write mode "w" -->open for writing file
# create file "x" --> create new file
# append file "a"--> add something in end of file
# text mode "t"--> text files
# plus mode "+" --> read and write both(update)
# opening file
# --------------------------------------------------
f = open("ankit.txt", "r+")
a = f.write("ankit loves hacking")
print(a)

f.close()
