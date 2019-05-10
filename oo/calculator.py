
#类定义
class calculator:
    # # # 定义基本属性
    # num11 = 5
    # num22 = 6
    # # # 定义私有属性,私有属性在类外部无法直接进行访问
    # __weight = 0
    # 定义构造方法
    def __init__(self, x = 3, y = 4):
        self.num1 = x
        self.num2 = y

    def add(self):

        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2


    def mul(self):
        return self.num1 * self.num2


    def div(self):
        return self.num1 / self.num2



# 实例化类

# c = calculator(2,5)
#
# print(c.div())

