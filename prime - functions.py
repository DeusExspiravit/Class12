def prime(l):
    p = []
    for i in l:
        b = 0
        for n in range(1, i+1):
            if i%n == 0:
                b += 1
        if b <= 2:
            p.append(i)
    return p
ch = 'y'
list = []
while ch != 'n':
    i = int(input('Enter any number '))
    list.append(i)
    ch = input('do you want to continue?(y/n) ')
print(prime(list))
