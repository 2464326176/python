# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方
# 反向运算符重载：

# __radd__: 加运算
# __rsub__: 减运算
# __rmul__: 乘运算
# __rdiv__: 除运算
# __rmod__: 求余运算
# __rpow__: 乘方
# 复合重载运算符：
#
# __iadd__: 加运算
# __isub__: 减运算
# __imul__: 乘运算
# __idiv__: 除运算
# __imod__: 求余运算
# __ipow__: 乘方


'''
关于__naem__ 自己运行时__main__
别人调用自己就是 文件名字
'''
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)