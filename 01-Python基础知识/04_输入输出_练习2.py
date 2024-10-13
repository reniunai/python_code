"""
超市买苹果计算金额
需求:	
●  收银员输入苹果的价格price，单位：元/斤
●  收银员输入用户购买苹果的重量weight, 单位：斤
●   计算并输出付款金额:xxx元
"""

price = input("苹果的价格: ")

weight = input("苹果的重量: ")

price = float(price)
weight = float(weight)

print("付款金额: %.2f 元" % (price * weight))
