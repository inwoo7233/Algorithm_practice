def max_profit(price_list, count):
    list = [price_list[0], price_list[1]]

    i = 2
    while i <= count:
        j = 1
        profit = 0
        if i < len(price_list):
            profit = price_list[i]
        while j < i // 2 + 1:
            try_num = list[j] + list[i - j]
            profit = max(profit, try_num)
            j += 1
        list.append(profit)
        i += 1

    return list[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))