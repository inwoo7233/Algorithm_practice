def min_fee(pages_to_print):
    sorted_list = sorted(pages_to_print)
    pay = 0
    i = 0
    while i < len(sorted_list):
        pay += sorted_list[i] * (len(sorted_list) - i)
        i += 1

    return pay


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))