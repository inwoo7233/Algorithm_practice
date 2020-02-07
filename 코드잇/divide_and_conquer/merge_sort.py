def merge(list1, list2):
    merged_list = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    if i == len(list1):
        merged_list += list2[j:]
    if j == len(list2):
        merged_list += list1[i:]

    return merged_list

# 합병 정렬
def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    # base-case

    mid = len(my_list) // 2
    # divide
    case1 = merge_sort(my_list[:mid])
    case2 = merge_sort(my_list[mid:])
    # conquer : 재귀적 conquer

    return merge(case1,case2)
    # combine


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))