# 形参
def greet_user(username):
  print(f"Hello, {username}!")

  return username.title()

# 实参
print(greet_user("Mike"))


# 关键字实参，不用考虑传递顺序
def describe_pet(pet_name, animal_type="cat", age = 0):
  print(f"I have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")
  result = {  "name": pet_name, "type": animal_type}
  if age:
    print(f"It's {age} years old.")
    result["age"] = age
  return result

describe_pet(animal_type="dog", pet_name="WangWang")
describe_pet(pet_name="WangWang", animal_type="dog")
describe_pet("WangWang", "dog")
print(describe_pet("MiMi"))
print(describe_pet("AHuang", "dog", age=3))

def greet_users(users):
  for user in users:
    print(f"Hello, {user.title()}!")

greet_users(["Huang", "Wang", "Zhang"])

# 函数内部直接修改list
def print_models(unprinted_designs, completed_models):
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

# 如果不修改list，传递是浅拷贝
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

def print_models(unprinted_designs):
  completed_models = []
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

  return completed_models

# 浅拷贝 切片表示法
## 非必要都传入原始列表，避免额外的拷贝开销
completed_models = print_models(unprinted_designs[:])
print(completed_models)
print(unprinted_designs)



# *args 不定长参数
def make_helper(*toppings):
  """打印顾客点的所有配料"""
  # tuple 元祖
  print(toppings)
  for topping in toppings:
    print(f"- {topping}")

make_helper('pepperoni')
make_helper('pepperoni', 'mushrooms', 'cheese')


def make_helper_width_size(size, *toppings):
  """打印顾客点的所有配料"""
  # tuple 元祖
  print(f"Making a {size}-inch helper with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

make_helper_width_size(16, 'pepperoni', 'mushrooms')


# **kwargs 关键字实参
def build_profile(first, last, **user_info):
  """创建一个字典，其中包含我们知道的用户信息"""
  profile = {}
  profile['first_name'] = first
  profile['last_name'] = last
  for key, value in user_info.items():
    profile[key] = value
  return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

## 总结
# 混合使用位置实参、关键字实参和任意数量的实参



# 函数放入模块中，另一个模块中导入函数
# from utils.helper
# from utils.helper import make_pi, make_pi_width_size
from utils import helper

helper.make_pi('cheese1')
helper.make_pi_width_size(10, 'cheese2')

# as 别名
from utils.helper import make_pi as mp
mp('cheese3')

# 全部导入并解构名称，明显没有显式引入好
from utils.helper import *
make_pi_width_size(10, 'cheese4')

