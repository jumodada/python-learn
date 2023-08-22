"""
有一个变量叫hero_equip是列表，代表英雄所穿的装备，
当我们把hero_equip传入到一个计算装备属性的函数calc_equip_properties中，
这个函数可以返回对应的装备属性。

最后通过代码实现把这些装备的属性全部放入到一个列表中

"""

# 代表英雄现在所穿的装备
hero_equip = [
"红莲斗篷",
"辉月",
"破军",
"魔女斗篷",
"影刃之足"
]

def calc_equip_properties(equip):
    if "红莲斗篷"==equip:
        return "防御+120"
    elif "辉月"==equip:
        return "无敌1.5秒"
    elif "破军"==equip:
        return "物理攻击+180"
    elif "魔女斗篷"==equip:
        return "魔法防御+360"
    elif "影刃之足"==equip:
        return "移动速度+60"
    
p = map(calc_equip_properties, hero_equip)
print(list(p))