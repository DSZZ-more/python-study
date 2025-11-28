def make_pi(*toppings):
  """打印顾客点的所有配料"""
  # tuple 元祖
  # print(toppings)
  for topping in toppings:
    print(f"helper - {topping}")

def make_pi_width_size(size, *toppings):
  """打印顾客点的所有配料"""
  # tuple 元祖
  for topping in toppings:
    print(f"helper - size: {size} type: {topping}")

