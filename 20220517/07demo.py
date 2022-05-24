print('我叫%s，今年%d歲'%('小明',18))
name = '張三'
age = 19
print(f'我叫{name},今年{age}岁')

# 斐波那契数
a,b = 0,1
while b<100:
    print(b,end=' ')
    a,b = b,a+b