# 控制台提示你输入内容，然后才会继续执行
# 输入的内容赋值给 name，input入参是 prompt 提示信息
# name = input("Please enter your name: ")
# print(f"Hello, {name}")


# # 内容始终是字符串
# age = input("Please enter your age: ")
# # 转换为数字
# age = int(age)
# print(f"{name} is {age} years old")
# is_adult = age >= 18
# print(f"{name} is an adult: {is_adult}")


# # % 运算符
# number = input('Enter a number: ')
# number = int(number)
# if number % 10 == 0:
#     print(f"{number} is a multiple of 10")
# else:
#     print(f"{number} is not a multiple of 10")


# # 关键：避免死循环，一定要有符合条件的退出条件
# cur_number = 1
# while cur_number <= 5:
#     print(cur_number)
#     cur_number += 1

# cur_number = 5
# while cur_number >= 1:
#     print(cur_number)
#     cur_number -= 1

# # flag 作为退出条件
# business = [1,2,3,4,5,6,7,8,9,10]
# flag = True
# while flag:
#     print("营业项目个数：", len(business))
#     business.pop()
#     if len(business) == 0:
#         flag = False
#         print("结束营业")

# # break 退出
# prompt = input("请输入命令：")
# while True:
#     if prompt == "quit":
#         print("成功退出")
#         break
#     else:
#         print("成功输入: ", prompt)
#         # 必须有，不然一直死循环
#         prompt = input("请重新输入命令：")

# continue




# while循环与列表和字典结合起来使用
unconfirmed_lists = ['alpha', 'beta', 'gamma']
confirmed_lists = []

while unconfirmed_lists:
    current_list = unconfirmed_lists.pop() # 弹出列表末尾的元素 vs shift() unshift()
    print(f"正在处理：{current_list.title()}")
    confirmed_lists.append(current_list)

print("\n处理完成：")
print(unconfirmed_lists)
print(confirmed_lists)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# 循环删除
while 'cat' in pets:
    pets.remove('cat')

print(pets)

# 补充：for 不要改列表，while 改列表
