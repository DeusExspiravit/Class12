def pattern(n):
    for i in range(n):
        for j in range((n-1-i)*2):
            print(' ', end='')
        print('#',end='')
        if i >= 1:
            for k in range(i*2+1):
                print(' ', end='')
        if i >= 2:
            for l in range((i-1)*2):
                print(' ', end='')
        if i >= 1:
            print('#', end='')

        print()
pattern(5)
