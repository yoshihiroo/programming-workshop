'''
【総合演習】打ち込んで動かしてみる。なぜその表示結果になるか、机上で動きを理解する
'''

def xyz(alist):
    length = len(alist)
    for i in range(length):
        for j in range(length-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

data = [3, 1, 4, 5, 2]

xyz(data)
print(data)
