x = 1
y = 3
z = 2

cat_a_dis = (z-x) **2
cat_b_dis = (z-y) **2

print(cat_a_dis,cat_b_dis)
if cat_a_dis>cat_b_dis:
    print("Cat B")
elif cat_b_dis > cat_a_dis:
    print("Cat A")
elif cat_a_dis == cat_b_dis:
    print("Mouse C")