# python 是解释性语言不需要经过编译
# python 可以调用 C/C++ 代码 ， C/C++ 程序也可以嵌入 python 代码


# 标识符大小写敏感

# python 保留字
import keyword
print(keyword.kwlist)

# 根据缩进的空格数判断代码块


# 多行语句  使用 \ 换行
str = 'i am '+ \
    'boy'
print(str)


# print 输出默认换行
print('hello world', end=' ')
print('不换行')