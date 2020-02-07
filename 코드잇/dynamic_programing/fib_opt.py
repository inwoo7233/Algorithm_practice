def fib_optimized(n):
    current = 1
    previous = 0
    i = 1
    while i < n:
        temp = current
        current = current + previous
        previous = temp
        i += 1

    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))