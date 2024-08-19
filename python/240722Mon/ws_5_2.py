# 아래 함수를 수정하시오.
def remove_duplicates(list):
    new_lst = []
    for num in list:
        if num not in new_lst:
            new_lst.append(num)
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
