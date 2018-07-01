a = 0
sum = 0
while a <= 100:
    if a % 2 == 0:
        sum += a
    if a == 88:
        break
    a = a + 1
print("sum:%d" % sum)

# 99乘法表
raw = 1
while raw <= 9:
    col = 1
    while col <= raw:
        if col != raw:
            print("%s*%s=%s\t" % (raw, col, raw * col), end="")
        else:
            print("%s*%s=%s" % (raw, col, raw * col))
        col += 1
    raw += 1
