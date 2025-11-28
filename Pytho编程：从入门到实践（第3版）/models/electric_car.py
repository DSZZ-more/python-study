class Car:
  '''
  汽车类
  '''
  def __init__(self, make, model, year):
    '''初始化汽车属性'''
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
    self.full_gas_tank = 65
    self.gas_tank = 20

  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")

  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def increment_odometer(self, miles):
    self.odometer_reading += miles

  def fill_gas_tank(self, gas=None):
    # 已经加满
    if gas is not None and gas > self.full_gas_tank:
      print("The gas tank is full.")
      return

    # 加满
    if gas is None:
      gas = self.gas_tank
      return

    # 加一部分
    self.gas_tank += gas

    if self.gas_tank >= self.full_gas_tank:
      print(f"The gas tank is full. only add {self.full_gas_tank - self.gas_tank} gas to the tank.")
    else:
      print(f"Add {gas} gas to the tank.")


# composition 组合 - 属性和方法太多了，把一部分提取出来
class Battery:
  '''电瓶的独特之处'''
  def __init__(self, battery_size=75):
    '''初始化电瓶的属性'''
    self.battery_size = battery_size

  def describe_battery(self):
    '''打印一条描述电瓶容量的消息'''
    print(f"This car has a {self.battery_size}-kWh battery.")

# defining a child class
class ElectricCar(Car):
  '''电动汽车的独特之处'''
  def __init__(self, make, model, year):
    '''初始化父类的属性'''
    super().__init__(make, model, year)
    # 新的属性
    self.battery_size = 75

  def get_range(self):
    '''打印一条消息，指出电瓶的续航里程'''
    if self.battery_size == 75:
      range = 260
    elif self.battery_size == 100:
      range = 315
    else:
      range = 0
    print(f"This car can go approximately {range} miles on a full charge.")

  def describe_battery(self):
    '''打印一条描述电瓶容量的消息'''
    print(f"This car has a {self.battery_size}-kWh battery.")

  def fill_gas_tank(self):
    print("This car doesn't need a gas tank!")