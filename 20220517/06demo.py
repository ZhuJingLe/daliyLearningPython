# 运算符
# 1、算术运算符
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
print('-------------')

# 2、比较运算符
c = 10
d = 100
print(c==d)
print(c!=d)
print(c>=d)
print(c<=d)
print(c>d)
print(c<d)
print('-------------')

# 3、赋值运算符
e = 100
f = 0
f += e
print(f)
print('------------')

# 4、逻辑运算符
print(10 and 20)
print(10 or 20)
print(not True)
print(not 10)
print('-------------')

# 5、成员运算符
li = [20,30,80,100]
print(a in li)
print(a not in li)
print('------------')

# 6、身份运算符  比较两个对象的存储单元
print(a is b)
print(a is not b)
print(id(a),id(b))
print('-------------')

# 7、位運算
a = 60
print(a<<2)
