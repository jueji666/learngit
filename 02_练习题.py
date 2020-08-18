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
