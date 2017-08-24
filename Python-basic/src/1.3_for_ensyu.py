'''
【演習】どんな数字の並びが表示されるか机上でやってみる
'''

a = 0
b = 1

for i in range(5):
    print(b, end=" ")
    c = a + b
    a = b
    b = c
