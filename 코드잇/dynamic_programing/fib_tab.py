def fib_tab(n):
    table = {}
    i = 1
    while i <= n:
        if i < 3:
            table[i] = 1
        else:
            table[i] = table[i - 1] + table[i - 2]
        i += 1

    return table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))