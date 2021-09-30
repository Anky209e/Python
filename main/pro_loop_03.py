#You have to guess a no and enter it its guess game using while loop.
num = 23
numgs = 0
print("Welcome to Guess game Guess a no in 5 Chances\n")
while (numgs<6):
    numgs=numgs+1
    user = int(input("Enter your no:\n"))
    if user ==num:
        print("Succeded")
        break
    elif user>num:
        print("chances Taken",numgs)
        print("Enter some less no\n")
        continue
    elif user<num:
        print("chances Taken",numgs)
        print("Enter a greater no")
        continue
    elif numgs==5:
        print("game over")
        