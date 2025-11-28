# --- --- --- --- --- --- 第4章 操作列表 --- --- --- --- --- ---


magicians = ['alice', 'david', 'carolina']

# 注意冒号，注意缩进
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

# 包含start，不包含end
nums = range(1, 10)
print(nums)
for value in nums:
    print(value)

# 才是列表
numbers = list(range(1, 10))
print(numbers)

even_nums = list(range(2, 11, 2))

# test
squares = []
for value in range(1, 11):
    square = value * 2
    squares.append(square)

print(squares)

# 针对数值列表
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# 推导式
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# slice
my_foods = ['pizza', 'falafel', 'carrot cake']
# 获取前2个
print(my_foods[:2])
# 获取中间2个
print(my_foods[1:])
# 获取最后2个
print(my_foods[-2:])

# 复制，start和end都省略
my_foods_copy = my_foods[:]
# 添加 append，不是push
my_foods_copy.append('ice cream')
print(my_foods)
print(my_foods_copy)

# --- --- tuple 元祖 不可修改的元素,不可变的【列表】
# 圆括号 而不是 方括号 来标识
# 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰
dimensions = (200, 50)

# 本质上还是列表
print(dimensions[0])
print(dimensions[1])

# 同样可以遍历
for dimension in dimensions:
    print(dimension)