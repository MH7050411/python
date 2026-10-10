# ## ============if条件判断=================
# ## 条件判断：如果我的分数超过680，我就去清华读书
#
# score = 680
# if score >= 680:
#     print("欢迎来清华读书！！！")
#     print("开始大学生活")
# print("--------------------------")
#
# ## 登录案例
# # 1. 接受用户输入的账号和密码
# ok_account = "123456"
# ok_password = "666888"
# account = input("请输入您的b站账号：")
# passwprd = input("请输入您的b站密码：")
# ## 2. 判断账号密码是不是全部正确，如果正确，则登录成功进入B站
# if account == ok_account and passwprd == ok_password:
#     print("登录成功")
#     print("进入B站首页~")
# ## 3. 判断账号是否错误，如果错误，则登录失败
# if account != ok_account or passwprd != ok_password:
#     print("登录失败") ##在任意位置换到新的一行的快捷键：shift + enter
#     print("账号或密码错误")
#     # if account != ok_account and passwprd != ok_password:
#     #     print()
#
# ## 登录案例 else 优化
# # 1. 接受用户输入的账号和密码
# ok_account = "123456"
# ok_password = "666888"
# account = input("请输入您的b站账号：")
# passwprd = input("请输入您的b站密码：")
# ## 2. 判断账号密码是不是全部正确，如果正确，则登录成功进入B站
# if account == ok_account and passwprd == ok_password:
#     print("登录成功")
#     print("进入B站首页~")
# else:
#     ## 3. 判断账号是否错误，如果错误，则登录失败
#     print("登录失败") ##在任意位置换到新的一行的快捷键：shift + enter
#     print("账号或密码错误")

#
# ## 判断闰年平年的案例
# year = int(input("请输入一个年份："))
# # 非整百年，能被4整除
# # 整百年(1922,2000)，必须能被400整除
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")
#
# ## if...elif...else结构
# ## 判断数字是否为正数还是负数还是0
# num = int(input("请输入一个数字："))
# if num > 0:
#     print(f"{num}是一个正数")
# elif num < 0:
#     print(f"{num}是一个负数")
# else:
#     print(f"{num}为0")

# ## 判断三角形类型的案例
# # 1. 接收用户输入的三角形的三条边
# a = int(input("请输入第一个边长a："))
# b = int(input("请输入第二个边长b："))
# c = int(input("请输入第三个边长c："))
# #2. 判断三角形的类型
# if a + b > c and b + c > a and c + a > b:
#     if a == b == c:
#         print(f"{a}、{b}、{c}三条边构成等边三角形")
#     elif a == b or b == c or c == a:
#         print(f"{a}、{b}、{c}三条边构成等腰三角形")
#     else:
#         print(f"{a}、{b}、{c}三条边构成普通三角形")
# else:
#     print(f"{a}、{b}、{c}三条边无法构成三角形")




# #### =================match...case结构=======================
# # 1. 接收用户输入的两个数
# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))
# # 2. 接收运算符
# op = input("请输入运算符（+，-，*，/）：")
#
# # 3. 使用match...case去匹配
# match op:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/" if num2 != 0: ## Python 3.10版本后支持case的if 和 |(或操作)
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("操作不支持!!!!!")




# ## ========================循环===========================
# ## =================while循环======================
# # 打印10遍"人生苦短，我用Python"
# i = 0
# while i < 10:
#     print("人生苦短，我用Python")
#     i = i + 1
# else:
#     print("循环结束")
#
# # print("循环结束")


# ## while循环的案例
# # 计算1-100间所有偶数之和
# ## 代码调试debug  断点（Pdb）
# total = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         total = total + i
#     i = i + 1
#
# print(f"1-100之间所有的偶数之和为{total}")


# 死循环
# while True:
#     print("hello python")





# for(int i = 0;i <= 100;i++){
#
# }

## ======================for循环========================
## for循环遍历用户所输入的字符串
# msg = input("请输入一个字符串：")
# for i in msg:
#     print(f"元素：{i}")
# else:
#     print("遍历完成")

## for循环中range()的使用
# l = range(0,100,1)
# ##第一个参数为start,表示从哪个数字开始；第二个参数是end,表示到哪里结束；第三个参数为step，表示序列的间隔
## range的范围是包含start，不包含end的
# print(type(l))
## 生成1-100所有奇数的和
total = 0
# for i in range(1,101,1):## range()会返回一个容器里面装的是start--------(end - 1)这些数字
#     if i % 2 == 1:
#         total += i
#     else:
#         print(f"1-100所有奇数的和为{total}")
#     ## 优化方案
# for i in range(1, 101, 2):  ## range()会返回一个容器里面装的是start--------(end - 1)这些数字
#     total += i
# else:
#     print(f"1-100所有奇数的和为{total}")
#
#
#
# ### ===================嵌套循环====================
# for i in range(3): ## 0-2
#     for j in range(3): ## 0-2
#         print(f"i - {i},j - {j}")



# ## 打印长为m，宽为n的一个矩形
# m = int(input("请输入长度m："))
# n = int(input("请输入宽度n："))
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ") ### print()使用end参数来控制结尾字符
#     print()

## 打印99乘法表
# for i in range(1,10): # 5
#     for j in range(1,i + 1):
#         print(f"{j} * {i} = {j * i}",end = "\t")
#     print()

### =======================循环案例==================================
# ● 需求：根据输入的用户名密码执行登录操作，具体要求如下：
# 1. 正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
# 2. 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
# 3. 输入的用户名和密码不能为空！
# 4. 登录成功：输出 "登录成功，进入B站首页~"
# 5. 登录失败：输出 "用户名或密码错误，请重新输入!"


## break -- 直接退出整个循环
## continue -- 退出当次循环，回到循环开头，继续下次循环

while True:
    # 1. 接收用户的输入
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 2， 校验：输入的用户名和密码不能为空
    if username == "" or password == "":
        print("输入的用户名和密码不能为空，请重新输入！！！！！！！！")
        continue

    # 3. 判断用户名密码是否正确
    if username == "admin" and password == "666888":
        print("登录成功，欢迎来到B站~")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功，欢迎来到B站~")
        break
    elif username == "whl" and password == "888666":
        print("登录成功，欢迎来到B站~")
        break
    else:
        print("用户名密码有误，请重新输入")

