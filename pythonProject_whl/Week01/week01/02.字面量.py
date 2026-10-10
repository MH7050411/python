# ## 字面量的写法
# # print(100) #整型字面量
# # print(3.14) #浮点型字面量
# # print(True) #bool类型字面量
# # print(False)
# # print(True)
# # print(True - 1)
# # print(False - 1)
# # print("hello") #字符串类型字面量
# # print(None) #空值字面量
#
# ## 变量 -- python 动态类型的语言，一个变量是可以存储不同类型的数据的
# # （在开发项目中，推荐变量只存储一种类型的数据）
#
# num = 1114.4
# # num = "hello"
# print(num)
# print(num + 1)
#
# msg = "hello"
# print(msg)
#
# a = True
# b = False
# print(a)
# print(b)
#
# ## 变量的案例
# base = 2298 #基础播放量
# incr = 200
# print("未来两个月的播放量为：",base + incr + incr) #输出未来两个月的播放量
#
# # a,b,c = 1,2,3
#
# ## 标识符
# # 6num = 10
# # str = 1
# ## 变量我们通常使用小写字母的标识符
# ## 常量我们通常使用全大写字母的标识符
#
# name = "whl"
# # name = "qwe"
# PI = 3.1415926
# MAX_LENGTH = 100
#
# ## 在python里面如何交换两个变量的值
# # a = 100
# # b = 100
# # print(a)
# # print(b)
# # c = a
# # a = b
# # b = c
# # print(a)
# # print(b)
# #
# # a,b = 100,200
# # print(a)
# # print(b)
# # a,b = b,c
# # print(a)
# # print(b)
#
# a,b,c = 100,200,300 ##a 300,b 100,c 200 in-place操作
# print(a,b,c)
# a,b,c = c,b,a
# print(a,b,c)



## python数据类型：五大数据类型

# print("hello")
# print(type("hello")) # <class 'str'>
# print(type(10)) # <class 'int'>
# print(type(10.1)) # <class 'float'>
# print(type(None)) # <class 'NoneType'>
# print(type(True)) # <class 'bool'>
#
#
# print(isinstance(True, str)) # isinstance() -->返回值是bool类型
# print(isinstance(10, int))






# ## 字符串
# s1 = "hello"
# s2 = 'hello'
# s3 = """
# hello:
#     你好，欢迎来上python课，
#     很高兴认识大家
# """
# print(s1)
# print(s2)
# print(s3)
#
# ## 转义字符 \' \" \n \t
# s4 = 'it\'s a good day'
# s5 = "hello的意思是\"您好\""
#
# s6 = "hello的意思\t是\"您好\""
# s7 = "hello的意思\n是\"您好\""
#
# print(s4)
# print(s5)
# print(s6)
# print(s7)
#
#
# ## 字符串拼接
# s8 = "hello" + "world"
# print(s8)
#
# print("字符串拼接示例：" + s8 + s7)
#
# ## 其他类型转换字符串
# age = 18
# name = "whl"
# print(name + str(age))
#
#
# ## 字符串格式化
# name = "王慧琳"
# age = 18
# print(f"大家好，我是{name},我的年龄是{age}")



### python 的输入()input和输出(print)
# name = input("请输入您的姓名：") ## input()函数，返回值一定是字符串类型
# print(name)

# num = input("请输入一个数字：")
# print(num)
# print(type(num))
# print(int(num))
# print(type(int(num)))

## 案例：银行取款
# ## 1. 总金额
# total = 10000
# ## 2. 输入用户密码
# password = input("请输入您的密码：")
# print(f"密码正确，您输入的密码为{password}")
# ## 3. 输入取款金额
# num = int(input("请输入您的取款金额："))
# ##4. 计算金额并输出
# print(f"取款后您账户余额为：{total - num}")



## 运算符
# 算数运算符
print(10 + 3)
print(10 - 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 2)
# 赋值运算符

#比较运算符
print(3 > 1)
print(type(3 > 1))
#逻辑运算符

a = 21
print(10 <= a <= 20)

print(a <= 10 or a >= 20)

print(not(10 <= a <= 20))