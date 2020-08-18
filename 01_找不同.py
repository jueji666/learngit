# 找出一段文字中的不同字
str= "啊啊啊啊啊啊啊啊啊啊aa"

def tj(str):
    l = {}
    for a in str:
        if a not in l:
            l[a]= str.count(a)

    if len(l.keys()) == 0:
        print('这段内容为空')
    elif len(l.keys()) == 1:
        for key in l:
            print('这段内容只有1种字是：' + key)
    else:
        for key, values in l.items():
            if values == min(l.values()):
                print(key)
    return


tj(str)


