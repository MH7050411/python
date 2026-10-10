## -------------数据容器角度-字符串--------------
s = "hello-world"
print(s[0])
print(s[-1])
# s[0] = 'H' # 'str' object does not support item assignment
print(s[::2])
print(s[::-1])  # 步长为负数表示从后往前输出
for i in s:
    print(i)
## -------------------------str的常见方法----------------------------
s = "    ******Hello-World-Hello-Python    "
# find()
index = s.find("_")
print(index)

# count()
num = s.count("-")
print(num)

# upper()
s1 = s.upper()
print(s1)
print(s)

# lower()
s2 = s.lower()
print(s2)

# split()/join()
l = s.split('-')
print(l)

# strip()
s4 = s.strip("*")

# replace()
s5 = s.replace("-","_")

# startwith()/endwith()
print(s.startswith(" "))

## ----------------------------------------------------
# 邮箱验证：用户输入邮箱，
# 验证格式是否正确（包含@和至少一个.）
# 正确输出正确
# 正则表达式：编程领域专门负责字符串匹配

s = "123456@."
# if s.count("@") == 1 and s.count(".") >= 1:
if s.count("@") == 1 and "." in s:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")


