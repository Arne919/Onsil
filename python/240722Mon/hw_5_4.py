# 아래 함수를 수정하시오.
def find_min_max(_list):
    _list.sort()
    return _list[0],_list[len(_list)-1]

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
