# 아래 함수를 수정하시오.
def remove_duplicates_to_set(list):
    new_list = []
    for num in list:
        if num not in new_list:
            new_list.append(num)
    return set(new_list)


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
