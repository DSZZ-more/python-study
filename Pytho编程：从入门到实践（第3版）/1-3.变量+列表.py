# 变量
message = "hello python world!"
print(message)


# string 字符串
print(message.title())
print(message.upper())
print(message.lower())

first_name = "ada"
last_name = "lovelace"
# 使用 f{} 在字符串中插入变量 format() 的意思
full_name = f"{first_name} {last_name}"

print(full_name)
print(f"Hello, {full_name.title()}!")

# 删除前后空格
message = " Python "
print(message.lstrip())
print(message.rstrip())
print(message.strip())

# 删除前后字符串
url = 'https://nostarch.com'
print(url.removeprefix('https://'))
print(url.removesuffix('.com'))
print(url.removesuffix('.com').removeprefix('https://'))


# number 数
## integer 整数
num1 = 2
num2 = 3

plus = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2
mod = num1 % num2
exponent = num1 ** num2
print(exponent)

## float 浮点数
float1 = 0.1
float2 = 0.2

plus = float1 + float2
print(plus)

x, y, z = 1, 2, 3
print(x, y, z)


# constant 常量
PI = 3.14


# import this
'''
liang@leaf pictures % python3
Python 3.9.6 (default, Aug 11 2023, 19:44:50) 
[Clang 15.0.0 (clang-1500.0.40.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''


# list 列表
names = ['liang', 'zhang', 'wang']
print(names)
print(names[0])
print(names[0].title())
# 倒数 第一个，即为最后一个
print(names[-1])

names[0] = 'jiang'

names.append('zhou')

names.insert(0, 'xie')

del names[0]

# 弹出列表末尾的元素
popped_name = names.pop()
print(popped_name)

# 弹出列表指定位置的元素
popped_name = names.pop(1)

# 移除列表中指定的元素
names.remove('wang')

cities = ['beijing', 'shanghai', 'guangzhou']
cities.sort()
cities.sort(reverse=True)
print(cities)
# 临时排序，不改变 cities
print(sorted(cities))

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# 反转列表元素的排列顺序
cars.reverse()
print(cars)

# len() length 长度
print(len(cars))

# 获取不存在的下标会报错
# IndexError: list index out of range
print(cities[4])
