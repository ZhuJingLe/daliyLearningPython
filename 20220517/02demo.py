# 数据类型
# 不可变数据类型：Number 数字、String 字符串、Tuple 元组
# 可变数据类型：List 列表、Dictionary 字典、Set 集合
# 1、数字 Number -> int 整数、bool 布尔、float 浮点数、complex 复数

# 2、字符串
str = 'helloworld'
print(str[0:1])
print('hello\nworld')
print(r'hello\nworld')
print(str[0:-1])
print('hello'*3)
str2 = '''
hello world aaa
'''
print(str2)

# 3、布尔是 int 的子类
print(issubclass(bool, int))
class A:
    pass

class B(A):
    pass
print(isinstance(B(),A))
print(1==True,0==False)

# 4、列表 List
li = [2022, 'hello', 'python', 5]
li2 = ['hello python']
print(li[0])
print(li + li2)
print(li[0:2])
print(li[-1::-1])

# 5、元组 Tuple  和列表类似 但是元组是不能修改的
tup = (10,)
print(tup)

# 6、Set 集合
'''
使用 set 删除重复数据
创建集合 {} 或 set() ，创建空集合只能使用 set()
'''
se = {'python','vue','javascript','python'}
print(se)
se2 = set(('java','vue','vue','react'))
print(se2)

# 7、字典
'''
键值对，键只能是不可变类型，键必须是惟一的
'''
dic = {'name':'zhu','age':18}
dic2 = dict([('name','zhu'),('age',18)])
print(dic)
print(dic2)
print(dic.keys())

print(repr(2022))
a='hello009'