def cal_new(n):
    n = str(n)
    n1 = n[:2]
    n2 = n[2:]
    n1 = int(n1)
    n2 = int(n2)
    n = n1**2 + n2**2
    return n
a = 7649
print(cal_new(a))