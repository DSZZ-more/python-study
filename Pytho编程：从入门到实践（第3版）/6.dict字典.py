# --- --- --- dictionary 字典：--- --- --- 
'''
在Python中，字典(dictionary)是一系列键值对。
每个键都与一个值关联，可以使用键来访问与之关联的值。
与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任意Python对象用作字典中的值

VS Object
不就是JS的对象吗？
'''


alien_0 = {'color': 'green', 'points': 10}
    
print(alien_0['color'])
print(alien_0['points'])

# 会按添加的顺序保存、遍历
alien_0['y_position'] = 10
alien_0['x_position'] = 10

print(alien_0)

del alien_0['points']

# get 访问不会报错，而键的方式获取，如果指定的键不存在，会报错
alien_0.get('points', 'default value') # 默认值就是 None

# 遍历 items() 是键值对
for key, value in alien_0.items():
    print(f"{key}: {value}")

# 之前学的列表推导，变量赋值
a1, a2 = [1, 2]
print(a1, a2)

# keys() 只有键
for key in alien_0.keys():
    print(key)
# 遍历键，不需要加 keys()
for key in alien_0:
    print(f"键：{key}")

# 结合 sorted() 函数
for key in sorted(alien_0.keys()):
    print(key)

# values() 只有值
for value in alien_0.values():
    print(value)

# set() 函数,去重
uniques = set(alien_0.values())
for value in uniques:
    print(f"set: {value}")

# 集合
print(uniques)
# 没有键值对，也是花括号
set_nums = {1, 2, 3}

print("嵌套")
# 嵌套 - 字典，列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# 列表 存储 字典
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

# range() 创建30个字典
print(range(30)) # range(0, 30)
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print(aliens)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'] # 列表
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

for topping in pizza.get('toppings', []):
    print(f"\t{topping}")

# 6.5.3.3. 创建字典
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    print(f"\tFull name: {full_name}")
    for key, value in user_info.items():
        if key == 'location':
            print(f"\tLocation: {value}")