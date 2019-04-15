编写函数的几个原则

原则 1：函数设计要尽量短小，嵌套层次不宜过深。最好能控制在 3 层以内。
原则 2：函数申明应该做到合理、简单、易于使用。参数个数不宜太多。
原则 3：函数参数设计应该考虑向下兼容。比如相同功能的函数不同版本的实现，唯一不同的是在更高级的版本中添加了参数导致程序中函数调用的接口发生了改变。这并不是最佳设计，更好的方法是通过加入默认参数来避免这种退化，做到向下兼容。
原则 4：一个函数只做一件事，尽量保证函数语句粒度的一致性。
原则 5：不要在函数中定义可变对象作为默认值
原则 6：使用异常替换返回错误
原则 7：保证通过单元测试

判断一个值是否在字典中

data = {'name': 'codingcat', 'age': 25}

print('name' in data.keys())
可能有一部分同学会像上面👆这样加个keys, 那么这样做有什么影响呢？

官方推荐直接in就可以了 'name' in data, 这样还更简介 加上keys 会影响性能

变量交换

a = 10
b = 5
tmp = a
a = b
b = tmp
在其他语言中两个变量交换值的做法会像上面这样
但Python中可以有一种更方便的方法

a = 10
b = 5
a, b = b, a


使用**而不是pow
%time -n 20000 c = 2 ** 20
%time -n 20000 c = pow(2, 20)

使用**快10倍以上！


使用级联比较 a < b < c

Bad

a, b, c = 1, 2, 3
if a < b and b < c:
    pass
Good

a, b, c = 1, 2, 3
if a < b < c:
    pass
    
    
    
检查变量是否等于常量

Bad

if attr == True:
    print('True!')

if attr == None:
    print('attr is None!')
Good

# Just check the value
if attr:
    print('attr is truthy!')

# or check for the opposite
if not attr:
    print('attr is falsey!')

# or, since None is considered false, explicitly check for it
if attr is None:
    print('attr is None!')

使用 with 读取文件

Bad

f = open('file.txt')
a = f.read()
print a
f.close()
Good

with open('file.txt') as f:
    for line in f:
        print line