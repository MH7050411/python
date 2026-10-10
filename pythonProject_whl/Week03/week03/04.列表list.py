# ## list
# # 定义
# s = [56,23,1.2,'a',"abc",True,[1,2]]
# print(s)
# print(type(s)) # <class 'list'>
#
# # 获取元素
# print(s[0])
# print(s[-2])
# # print(s[9]) # IndexError: list index out of range
# # 修改元素
# s[0] = "hello"
# print(s)
#
# #删除元素
# del s[1]
# print(s)
#
# # 遍历
# for item in s:
#     print(item)
# ##-------------------------list切片----------------------------
# s = ["a","b","c","d","e","f"]
# # [开始:结束:步长] 切片是永远从左到右的顺序截取元素
# print(s[1:3])
# print(type(s[1:3]))
# print(s[1:-3])

# ##--------------------list 常见方法-----------------------------
# s = ["a","b","c","d","e","f"]
# # append()
# s.append("100")
# print(s)
#
# # insert()
# s.insert(1,"101")
# print(s)
#
# # remove()
# s.remove("101")
# print(s)
#
# # pop() del
# # s.pop(0)
# print(s)
# s.pop(100)
#
# # sort()
# s.sort(reverse=True)
# print(s)
#
# # reverse() 反转
# s.reverse()
# print(s)
#
# # 输入3个数，存储到列表，并将数字进行排序，
#
# # 1. 定义列表
# num_list = []
# # 2. 接受用户输入
# for i in range(3):
#     num = input("请输入一个数字：")
#     num_list.append(num)
# print("接收的列表为：",num_list)
# # 3. 排序
# num_list.sort()
# print("排序后的列表为：", num_list)
#
# # 4. 输出要求的值
# print(f"列表的最大值为：{max(num_list)}")
# print(f"列表的最小值为：{min(num_list)}")
# print(f"列表的评价值为：{sum(num_list)/len(num_list)}")

# # ---------------------list 案例2-------------------------
# # 合并两个列表的元素，合并并去重
# num_list1 = [1,2,3,4,5]
# num_list2 = [4,5,6,7,8]
# # print(5  in num_list1)
# # 1. 合并两个列表
# # for i in num_list1:
# #     num_list1.append(i)
#
# # 合并列表的简单方法
# num_list3 = num_list1 + num_list2
#
# # 2. 去掉重复的值
# num_list = []
# for i in num_list3:
#     if i not in num_list:
#         num_list.append(i)
#
# # 3. 去重后的结果
# print(num_list)

# ---------------------list 列表生成式-------------------------

# 生成 1-20 的平方列表
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
# print(num_list)
## 列表生成式 ---> 按照一定的规则快速生成一个列表的语法方式
num_list2 = [i**2 for i in range(1,21)]
print(num_list2)

# 从下面数字列表中提取所有偶数，并计算平方数，组成新列表
num_list = [19,23,54,64,87,20,109,123,232,43]
num_list3 = [i**2 for i in num_list if i % 2 == 0]
print(num_list3)

