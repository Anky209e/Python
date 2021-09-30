dic = {"ankit":"hacker","capti":"language","silver":"singer","dingo":"gamer"}
print(dic["capti"])
dic["ankit"] = "kali linux exp"
print(dic["ankit"])
d2 = dic
del dic["ankit"]
print(d2)
print(d2.update({"ankit":"hackerman"}))
print(d2)