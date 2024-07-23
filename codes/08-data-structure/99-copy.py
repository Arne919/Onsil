# 할당
# original_list = [1,2,3]
# copy_list = original_list
# print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]
# copy_list[0] = 'hi'
# print(original_list, copy_list) # ['hi', 2, 3] ['hi', 2, 3]


# 얕은 복사
# a = [1, 2, 3]
# b = a[:]
# print(a, b) # [1, 2, 3] [1, 2, 3]
# b[0] = 100
# print(a, b) # [1, 2, 3] [100, 2, 3]


# 얕은 복사의 한계
# a = [1, 2, [3, 4, 5]]
# b = a[:]
# b[2][1] = 100
# print(a) # [1, 2, [3, 100, 5]]
# print(b) # [1, 2, [3, 100, 5]]
# a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨


# 깊은 복사 (내장모듈 활용)
# import copy
# a = [1, 2, [3, 4, 5]]
# b = copy.deepcopy(a)
# b[2][1] = 100
# print(a) # [1, 2, [3, 4, 5]]
# print(b) # [1, 2, [3, 100, 5]]
