# ## 集合 set 无序，不可重复，可修改
# # 定义
# s1 = {1,2,3,4,5,'a','abc'}
# print(s1)
# print(type(s1)) #<class 'set'>
# # 定义空集合
# s2 = set()
# print(s2)
#
# # 基本操作(常见方法)
# # add()
# s3 = {1,2,3}
# print(s3)
# s3.add(4)
# print(s3)
#
# # remove() 删除
# s3.remove(4)
# print(s3)
#
# # pop() 不放回的抽签（弹出）
# e = s3.pop()
# print(e)
# print(s3)
#
# # 清空 clear()
# s3.clear()
# print(s3)

# # 交集
# s4 = {1,2,3,4,5}
# s5 = {3,4,5,6,7}
# print(s4.intersection(s5))
# print(s5.intersection(s4))
# print(type(s4.intersection(s5)))
#
# # 并集
# print(s4.union(s5))
# print(s5.union(s4))
#
# # 差集
# print(s4.difference(s5))
# print(s5.difference(s4))


## 集合的综合案例
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 根据提供的班级学生的选课情况，完成如下需求：
# 1．找出同时选修了法语和艺术的学生
# s1 = french_set.intersection(art_set)
# print(s1)
s1 = french_set & art_set
print(s1)
# 2．找出同时选修了所有四门课程的学生
s2 = football_set & basketball_set & french_set & art_set
print(s2)
# 3．找出选修了足球，但是没有选修篮球的学生
# s3 = football_set.difference(basketball_set)
# s3 = football_set - basketball_set
s3 = {s for s in football_set if s not in basketball_set}
print(s3)
# 4．统计每一个学生选修的课程数量
# 获取所有学生姓名
# all_stu = football_set.union(basketball_set).union(art_set).union(french_set).union(s1)
all_stu = football_set | basketball_set | art_set | french_set
print(all_stu)
# 获取每个学生选项的课程数量
all_list = [*football_set, *basketball_set, *art_set, *french_set]
for i in all_stu:
    print(f"{i}选修了{all_list.count(i)}门课程")


