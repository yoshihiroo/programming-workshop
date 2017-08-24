'''
【演習】リストの値を合計する関数を作る（sum関数と同等）
'''

#↓↓↓↓↓↓↓この関数の中身を完成させる
def mySum(alist):


#関数を呼び出す

list1 = [1, -3, 4, 10, -7]

#Pythonにもともと組み込まれている関数
print(sum(list1))

#今回の自作の関数
print(mySum(list1))

#
#
#
#
#
#
#
#
#
#
'''
ANSWER
def mySum(alist):
    s = 0
    for i in alist:
        s = s + i
    return s
'''
