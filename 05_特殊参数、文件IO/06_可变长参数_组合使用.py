def milk_tea_shop(kind, *arguments, **keywords):
    print(f"-- 老板，给我来一杯：{kind}!")
    print(f"-- 对不起，我们的 {kind} 已经能够卖完了！")
    for arg in arguments:
        print(arg)
    print("-" * 50)
    for key in keywords:
        print(f"{key}: {keywords[key]}")


milk_tea_shop(
    "QQ咩咩好喝到爆的咩噗茶",
    "加糖", "少冰", "加奶", "加珍珠", "加茅台",
    price="10元", address="北京市朝阳区望京SOHO",
    phone="010-12345678"
)