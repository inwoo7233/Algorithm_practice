def max_profit_memo(price_list, count, cache):
#     count보다 작은 값들의 최적값을 활용한다.
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    if count in cache:
        return cache[count]

    max = 0
    if count < len(price_list):
        max = price_list[count]

    i = 1
    while i < count // 2 + 1:
        try_num = max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache)
        if try_num > max:
            max = try_num
        i += 1
    cache[count] = max

    return cache[count]

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))