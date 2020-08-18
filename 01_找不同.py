# 找出一段文字中的不同字
str= "啊啊啊啊啊啊啊啊啊啊aab"

def tj(str):
    l = {}
    for a in str:
        if a not in l:
            l[a]= str.count(a)

    if len(l.keys()) == 0:
        return print('这段内容为空')
    if len(l.keys()) == 1:
        for key in l:
            return print('这段内容只有1种字是：' + key)
    if len(l.keys()) == 2:
        for key in l:
            return print('这段内容只有2种字是：' + key)
    if len(l.keys()) > 2:
        for key, values in l.items():
            if values == min(l.values()):
                min_key = key
        return print(min_key)


tj(str)


