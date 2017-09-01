#if文

a = [-10, -3, 0, 5, 10]
print(a)

for i in a:
    if i > 0:
        print(i, "is lager than zero")
    elif i == 0:
        print(i, "is zero")
    else:
        print(i, "is less than zero")
