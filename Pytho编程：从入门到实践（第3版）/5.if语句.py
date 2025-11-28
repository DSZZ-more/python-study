cars = ['audi', 'bmw', 'subaru', 'toyota']
  
for car in cars:
    if car == 'bmw':
      print(f"i find you: {car.upper()}")
    else:
      print(f"not: {car.title()}")

# list 判空
if cars:
   print(f"(we have {len(cars)} cars)")

# 字符串
car = "Audi"
print('audi' == car)
print('audi' != car)
print('audi' == car.lower())

# 数 条件语句标识的前后加一个空格
age = 18
print(age == 18)
# 不等
print(age != 18)
print(age >= 18)
print(age < 18)

# 多个条件 and or
result = age > 16 and age < 20

result = age > 16 or age < 20

# 集合 in not in
isIn = 'audi' in cars
isNotIn = 'audi' not in cars

# boolean
active = True
inactive = False

age = 12
if age < 6:
   print("Sorry, you are too young to play.")
elif age < 18:
   print("You can play, but you'll need a parent.")
else:
   print("Welcome to the game!")

# 列表非空
data = []
if data:
   print("列表非空")

