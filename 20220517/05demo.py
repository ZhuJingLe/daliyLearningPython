# 推导式

# 1、列表推导式
li = [1,9,34,34,45,67,90,100,300,400]
res = [item for item in li if item>45]
print(res)

# 2. 字典推导式
li2 = ['python','vue','java','react','php','go']
dic = {item:len(item) for item in li2}
print(dic)

# 3、集合推导式
li3 = ['nodejs','vue','react','python']
se = {item for item in li3}
print(se)

# 4、元组推导式
li4 = ['java','python','javascript','php']
tup = (item for item in li4)
print(tuple(tup))