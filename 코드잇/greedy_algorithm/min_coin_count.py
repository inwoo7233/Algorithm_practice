def min_coin_count(value, coin_list):
    sorted_coin_list = sorted(coin_list, reverse=True)

    i = 0
    count = 0
    while i < len(sorted_coin_list):
        count += value // sorted_coin_list[i]
        value = value % sorted_coin_list[i]
        i += 1

    return count

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))