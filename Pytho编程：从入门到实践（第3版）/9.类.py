from models import Dog

dog = Dog('Wolf', 3)
print(dog.name)

dog.sit()

dog.roll_over()

# 方法更新属性
dog.update_age(5)

# 直接修改属性
dog.age += 28

dog.get_age()

dog.get_count()



# 继承
from models import Car, ElectricCar

my_gas_car = Car('audi', 'a4', 2019)
print(my_gas_car.get_descriptive_name())
my_gas_car.fill_gas_tank(20)
my_gas_car.fill_gas_tank(50)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()

# 跑了100英里
my_tesla.update_odometer(100)

my_tesla.read_odometer()


# 标准库（不用安装第三方，本身支持的）
from random import randint, choice
num = randint(1, 10)

players = ['a', 'b', 'c', 'd', 'e']
player = choice(players)

# 练习题
from models.cap9.die import Die
die = Die(6)
die.repeat_roll(10)

die = Die(10)
die.repeat_roll(10)

die = Die(20)
die.repeat_roll(10)

# class的编写风格
## 类名驼峰，首字母大写，不带下划线；
## 类定义后面紧跟一个文档字符串；
## 方法名使用小写，多个单词用下划线连接，方法名第一个单词通常为 self；
## 方法之间一个空行分割，模块中，两个空行分割类；