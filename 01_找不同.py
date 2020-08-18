# 找出一段文字中的不同字
str= "啊啊啊啊啊啊啊啊啊啊a啊a啊啊b啊啊"

def tj(str):
    l = {}
    for a in str:
        if a not in l:
            l[a]= str.count(a)
    if len(l.keys()) == 0:
        print('这段内容为空')
    elif len(l.keys()) == 1:
        print('这段内容只有1种字是：' + str(l.keys()))
    elif len(l.keys()) == 2:
        print('这段内容只有2种字是：' + str(l.keys()))
    else :
        for key, values in l.items():
            if values == min(l.values()):
                min_key = key
    return min_key

print(tj(str))


