dic = {"Impossible": "Never done", "Immune": "power to fight disease",
       "Invincible": "Never died", "Aurdino": "Elecrtic device used for circuits"}
user = str(input("Enter word:\n"))
if user == "Impossible":
    print(dic["Impossible"])
elif user == "Immune":
    print(dic["Immune"])
elif user == "Invincible":
    print(dic["Invincible"])
elif user == "Aurdino":
    print(dic["Aurdino"])
else:
    print("Error 0x53349 Invalid input")
