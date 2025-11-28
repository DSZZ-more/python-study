class Dog:
    # 跟 constructor 类似，创建时自动执行一次
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 内置
        self.type = "Dog"
        self.count = 0
    
    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

    def update_age(self, age):
        self.age = age
        self.count += 1

    def get_age(self):
        print(f"{self.name} is {self.age} years old.")
        return self.age
    
    def get_count(self):
        print(f"{self.name} has been updated {self.count} times.")
        return self.count