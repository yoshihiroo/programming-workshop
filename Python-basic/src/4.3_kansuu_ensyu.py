'''
【演習】リストの値のうち、正の数のみを合計する関数を作る
'''

#↓↓↓↓↓↓↓この関数の中身を完成させる
def myPosSum(alist):


#関数を呼び出す

list1 = [1, -3, 4, 10, -7]

print(myPosSum(list1))

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
def myPosSum(alist):
    s = 0
    for i in alist:
        if i > 0:
            s = s + i
    return s
'''
