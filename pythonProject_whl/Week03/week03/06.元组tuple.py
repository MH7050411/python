# ## --------------------tuple----------------------
# # 使用 () 来定义元组
# t = (1,2,3,4,5,'a')
# # l = []
# t1 = ()
# l = [1]
# t2 = (1,)
# print(t2)
# print(type(t2)) #t2 = (1) <class 'int'>
#
# print(t[0])
# print(t[1])
# print(t[::-1])
# # t[0] = 10 #'tuple' object does not support item assignment
#
# for i in t:
#     print(i)
# ## --------------------tuple常见方法-------------------------
# # count() ----> int
# print(t.count(1))
# ## index() ----> int
# print(t.index('a'))

# ## --------------------组包、解包-----------------------
# t = (1,2,3,4,5)
# # 组包
# t1 = 1,2,3,4,5
# print(t1)
# print(type(t1)) #<class 'tuple'>
# # 解包
# a,b,c,d,e = t
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
#
# a, *y, b = t
# print(a)
# print(y)
# print(b)

# # ---------------再理解交换变量-----------------
# a = 100
# b = 200
# c = 300
# d = 400
# # 原地交换变量的值，背后原理就是组包解包
# a, b, c, d= b, a, d, c
# print(a)
# print(b)

## -------------------案例----------------------
# students = (("S001","王林",85,92,78),())
"""
    根据如下提供的学生成绩单，完成如下需求：
        1. 计算每个学生的总分、各科平均分，然后一并输出出来。
        2. 统计各科成绩的最低分、最高分、平均分，并输出。
        3. 查找成绩优秀（平均分大于90）的学生，并输出。
"""
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

# 1. 计算每个学生的总分、各科平均分，然后一并输出出来。
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 5
#     print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{total}\t{avg:.1f}")

## for循环时，如果每个循环元素时容器，可以直接在for这里解包，增强代码的可读性
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id}\t{name}\t{chinese}\t{math}\t{english}\t{total}\t{avg:.1f}")

# 2. 统计各科成绩的最低分、最高分、平均分，并输出。
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print(f"语文成绩最低分{min(chinese_scores)},最高分：{max(chinese_scores)},平均分：{sum(chinese_scores)/len(chinese_scores)}")

# 3. 查找成绩优秀（平均分大于90）的学生，并输出。
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    if avg >= 90:
        print(f"{name}是优秀学生，平均分{avg:.1f}")





