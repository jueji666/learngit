"""
一、输出以下内容
m = input("请输入姓名:")
n = input("请输入年龄:")
t = input("请输入性别:")
print("*"*18)
print("姓名:"+m)
print("年龄:"+n)
print("性别:"+t)
print("*"*18)
"""

"""
二、输出以下内容, 判断是否为偶数
m= int(input("请输入一个数值："))
def os(m):
    if m%2 == 0:
        return print(True)
    else:
        return print(False)
os(m)
"""

"""
三、列表li= ["hello",  "scb11",  "!"]转换成字符串'hello python18 !'
li= ["hello", "scb11", "!"]
li[1]= "python18"
m = " ".join(li)
print(m)
"""

"""
四、str1 = 'python hello aaa 123123aabb'
1）统计str1中有多少个a
2) 找出str1中"123"下标的起始位置
3) 请分别判断 "o a" "he" "ab"是否是str1中的成员
str1 = 'python hello aaa 123123aabb'
print(str1.count("a"))
print(str1.find("123"))
m = ["o a", "he", "ab"]
def exit(m):
    for x in m:
        if x in str1:
            print(x+"是str1中的成员")
        else:
            print(x+"不是str1中的成员")
exit(m)
"""

"""
五、将给定的字符串中的PHP替换为Python
best_language = "PHP is the best programming language in the world!"
m = best_language.replace("PHP", "Python")
print(m)
"""

"""
六、编写代码, 提示用户输入1-7个数字, 分别代表周一到周日, 数字是6或7代表周末, 打印出来今天是周几
num = input("请输入数字1-7：")
def week(num):
    day = ["1", "2", "3", "4", "5", "6", "7"]
    today = ["一", "二", "三", "四", "五", "末", "末"]
    if num in day:
        print("今天是周"+today[day.index(num)])
    else:
        print("输入不合法")

week(num)
"""

"""
七、现在有一个列表 li2=[1, 2, 3, 4, 5], 
第一步：请通过相关的操作改成li2 = [0, 1, 2, 3, 66, 4, 5, 11, 22, 33]
第二步：对li2进行排序处理 
li2 = [1,  2,  3,  4,  5]
li2.insert(0, 0)
li2.append(11)
li2.append(22)
li2.append(33)
li2.insert(5, 66)
print(li2)
li2.sort()
print(li2)
"""

"""
八、切片
1、li = [1, 2, 3, 4, 5, 6, 7, 8, 9] 请通过切片得出结果 [3, 6, 9] 
2、s = 'python java php', 通过切片获取: ‘java’ 
3、tu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 通过切片获取 [‘g’, ‘b’] 
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])
s = 'python java php'
print(s[7:11:1])
tu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
m = tu[1:2:1]+tu[6:7:1]
print(m)
print(m[::-1])
"""

"""
1. 某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
2、数据存储完了，然后输出个人介绍，格式如下:  我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
4. 平台为了保护你的隐私，需要你删除你的联系方式；
5. 你为了取得更好的成绩， 你添加了自己的擅长技能，至少需要 3 项。
yonghu = {}
def geren():
    name = input("请输入你的姓名：")
    sex = input("请输入你的性别：")
    age = input("请输入你的年龄：")
    yonghu["name"] = name
    yonghu["sex"] = sex
    yonghu["age"] = age


def jieshao():
    print("个人介绍：")
    print("我的名字%s，今年%s岁，性别%s，喜欢敲代码" %(yonghu["name"], yonghu["age"], yonghu["sex"]))

def buchong():
    high = input("请输入你的身高：")
    mobile = input("请输入你的联系方式：")
    yonghu["high"] = high
    yonghu["mobile"] = mobile

def delete():
    yonghu.pop("mobile")

def add():
    jineng = input("请输入你的至少三个技能(用，隔开)")
    if jineng.count("，")<2:
        jineng = input("请重新输入你的三个技能")
    yonghu["jineng"] = jineng

geren()
jieshao()
buchong()
delete()
add()
"""

"""
10. 
一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣
如果购买金额大于100元会给20%折扣
编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格

buyprice = float(input("你的购买价格为："))
if buyprice >100:
    youhui = 0.2
    print("你的购买价格%f, 折扣为%f%%, 最终价格为%f" %(buyprice, youhui*100, buyprice*youhui))
elif buyprice >=50:
    youhui = 0.1
    print("你的购买价格%.2f, 折扣为%.2f%%, 最终价格为%.2f" %(buyprice, youhui*100, buyprice*youhui))
else:
    pass
"""

"""
11.
一个 5 位数，判断它是不是回文数。例如： 12321 是回文数，个位与万位相同，十位与千位相同。 
根据判断打印出相关信息
num = input("请输入一个5位数：")
def panduan(num):
    if num[0] == num[4] and num[1] == num[3]:
        print("%s是一个回文数" % num)
    else:
        print("%s不是一个回文数" % num)
panduan(num)
"""
"""
12.
现有一个字典： 
dict = {'name':'小明,
        'age':18,
        'occup':'students',
        'teacher': {'语文':'李老师','数学':'王老师','英语':'张老师'}
        }
请获取到小明同学的名字；然后再获取到小明的数学老师
dict = {'name':"小明",
        'age':18,
        'occup':'students',
        'teacher': {'语文':'李老师','数学':'王老师','英语':'张老师'}
        }

print(dict["name"])
print(dict['teacher']["数学"])

"""

"""
13.
设计一个函数，获取一个100以内偶数的纯数字序列，并存到列表里， 然后求这些偶数数字的和
def numsum():
    li = list(range(2, 101, 2))
    print(li)
    sum = 0
    for i in li:
        sum += i
    print(sum)

numsum()
"""

"""
14.
输出99乘法表
row = 1
while row <=9:
    col = 1
    while col <=row:
        print("%d * %d = %d" % (row, col, col * row), end="\t")
        col += 1
    print("")
    row+=1

t = [1,2,3,4,5,6,7,8,9]
for i in t:
    for j in t:
        if j <=i:
            print("%d * %d = %d" %(i, j, j*i), end="\t")
            j += 1
    print("")
    i += 1

"""
"""
15.
有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
t = ["1", "2", "3", "4"]
s = 0
for i in t:
    for j in t:
        if j != i:
            for e in t:
                if e != j and e != i:
                    print(i+j+e)
                    s += 1
print("总共%d种无重复数字的不同三位数" %s )

"""
"""
通过函数实现一个计算器，
运行程序分别提示用户输入数字1，数字2，
然后再提示用户选择 ： 加【1】  减【2】 乘【3】 除【4】，
每个方法使用一个函数来实现， 选择后调用对应的函数，然后返回结果。
"""



