def consecutive_sum(start, end):
    if start == end:
        return start
    # BASE_CASE

    mid = int((start + end) / 2)
    # DIVIDE

    case1 = consecutive_sum(start, mid)
    case2 = consecutive_sum(mid + 1, end)
    # CONQUER : 재귀적 수행

    return case1 + case2
    # COMBINE

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))