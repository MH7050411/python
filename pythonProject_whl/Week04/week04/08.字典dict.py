# ## 字典 dictionary
# # 定义
# dict1 = {}
# # key必须为不可变类型（str, int, float, tuple）
# dict2 = {"张三":670, "李四":580, (1,2,3):790}
# print(dict2)
# print(type(dict2))  # <class 'dict'>

# ## 基础操作
dict1 = {"张三":600, "张四":620, "张五":580}
# print(dict1)
#
# # 添加
# dict1["李四"] = 700
# print(dict)
#
# # 修改
# dict1["李四"] = 500
# print(dict1)
#
# # 查询
# print(dict1["李四"])
# print(type(dict1["李四"])) # <class 'int'>
# print(dict1["张三"])
#
# # print(dict1["1"])
# print(dict1.get("1") is None)
# # print(dict1.get("李四"))
#
# ## 删除
# v = dict1.pop("李四")
# print(v)
# print(type(v)) # <class 'int'>
# print(dict1)

# # 获取所有的 key
# keys = dict1.keys()
# print(keys)
# print(list(keys))
# print(type(keys)) # <class 'dict_keys'>
#
# # 获取所有的 value
# values = dict1.values()
# print(values)
# print(list(values))
# print(type(values)) #<class 'dict_values'>
# # 获取所有的键值对 item
# items = dict1.items()
# print(items)
# print(list(items))
# print(type(items)) #<class 'dict_items'>
#
#
# # 遍历字典
# # 遍历key
# for k in dict1.keys():
#     print(f"{k}所对应的value为{dict1.get(k)}")
# # 遍历value
# for v in dict1.values():
#     print(v)
# # 遍历item
# for k,v in dict1.items():
#     # print(item)
#     # print(f"key - {item[0]}; value - {item[1]}")
#     print(f"key - {k}; value - {v}")



# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商
# 品数据，通过控制台菜单与用户交互。具体功能如下：
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该
# 商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量:
# xxx"。
# 5. 退出购物车

# 0.规划的数据结构

# 1.初始化相关信息（购物车字典，用户交互菜单）
shopping_cart = {}
menu = """
############ 购物车系统 #############
           1. 添加购物车
           2. 修改购物车
           3. 删除购物车
           4. 查询购物车
           5. 退出系统
######## 购物车系统 #########
结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}

"""

# print(menu)

# 2.执行具体的操作
while True:
    print(menu)
    choice = input("请选择要执行的操作（1-5）：")

    match choice:
        case "1":
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))
            # 如果商品存在，则不执行添加操作
            if goods_name in shopping_cart:
                print("该商品已存在，如需修改请重新修改。")
            else:
                shopping_cart[goods_name] = {"price":goods_price, "num":goods_num}
                print("商品添加成功！！！")
        case "2":
            goods_name = input("请输入要修改的商品名称：")
            # 如果商品不存在，则提示错误信息并重新选择
            if goods_name not in shopping_cart:
                print("商品不存在，请重新选择")
            # else:
                continue
            goods_price = float(input("请输入商品新的价格："))
            goods_num = int(input("请输入商品新的数量："))
            shopping_cart[goods_name] = {"price" : goods_price,"num":goods_num}
            print("修改成功！！！！")
        case "3":
            goods_name = input("请输入要删除的商品：")
            # 如果商品不存在，则提示错误信息并重新选择
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择。")
            else:
                v = shopping_cart.pop(goods_name)
                print("商品删除成功！！！")
        case "4":
            for name,good_info in shopping_cart.items():
                print(f"商品名称：{name}, 商品价格："
                      f"{good_info["price"]}, 商品数量：{good_info["num"]}")
        case "5":
            print("欢迎下次光临。bye~")
            break
        case _:
            print("您输出的操作不支持，请重新输入。")













