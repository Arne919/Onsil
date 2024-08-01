#240723test


# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
# def count_blood_types(blood_types):
#     blood = {}
#     for b in blood_types:
#         if b in blood:
#             blood[b] += 1
#         else:
#             blood[b] = 1
#     return blood

# print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}

def count_blood_types(blood_types):
    blood = {}
    for b in blood_types:
        if b not in blood:
            blood[b] = 1
        else:
            blood[b] += 1
    return blood

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
# def count_blood_types(blood_types):
#     blood = {}
#     for b in blood_types:
#         blood[b] = blood.get(b, 0) + 1
#     return blood
# print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기


# 1. [] 표기법을 사용한 방법
# def dict_invert(input_dict):
#     new_dict = {}
#     for key, value in input_dict.items():
#         if value not in new_dict:
#             new_dict[value] = [key]
#         else:
#             new_dict[value].append(key)
#     return new_dict


# 2. get 메서드를 사용한 방법
# def dict_invert(input_dict):
#     new_dict = {}
#     for key, value in input_dict.items():
#         new_dict[value] = new_dict.get(value, []) + [key]
#     return new_dict


# # 3. setdefault 메서드를 사용한 방법
# def dict_invert(input_dict):
#     new_dict = {}
#     for key, value in input_dict.items():
#         new_dict.setdefault(value, []).append(key)
#     return new_dict


# print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
# print(
#     dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
# )  # {10: [1], 20: [2], 30: [3, 4]}
# print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}


#ws_6_a
# my_set = {'가', '나', (0, 0)}
# my_dict = {
#         '가': 1, 
#         (0, 0): '튜플도 키값으로 사용가능'
#     }

# # 아래에 코드를 작성하시오.
# for key in my_set:
#     print(my_dict.get(key, 'None'))
# my_dict[(1,2,3,'A')]='변수로도 키 설정 가능'
# print(my_dict)


#ws_6_b
# data = {
#     '이름': '키위',
#     '종류': '새',
#     '원산지': '호주' 
# }

# plus_data = {
#     '종류': '과일',
#     '가격': 30000
# }
# # 1. data가 가진 모든 키와 벨류 목록을 출력한다.
# print(data.items())
# # 2. data가 가진 벨류 목록들만 모아서 출력한다.
# print(data.values())
# # 3. data에서 'without' 키가 가진 value를 출력한다.
#     # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
# print(data.pop('without', 'unknown'))
# # 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
# data.update(plus_data)
# # 5. 변경된 data를 출력한다.
# print(data)


#ws_6_c
# data = [
#     {
#         'name': 'galxy flip',
#         'company': 'samsung',
#         'is_collapsible': True,
#     },
#     {
#         'name': 'ipad',
#         'is_collapsible': False
#     },
#     {
#         'name': 'galxy fold',
#         'company': 'samsung',
#         'is_collapsible': True
#     },
#     {
#         'name': 'galxy note',
#         'company': 'samsung',
#         'is_collapsible': False
#     },
#     {
#         'name': 'optimus',
#         'is_collapsible': False
#     },
# ]

# key_list = ['name', 'company', 'is_collapsible']

# # 아래에 코드를 작성하시오.
# for d in data: #dict
#     for k in key_list: #str
#         value = d.get(k, 'unknown')
#         # d.setdefault(k, 'unknown')
#         print(f'{k}은/는 {value}입니다.')
#     print()


# hw_6_2 ??
# 아래 함수를 수정하시오.
# def remove_duplicates_to_set(list):
#     new_list = []
#     for num in list:
#         if num not in new_list:
#             new_list.append(num)
#     return set(new_list)


# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)


# hw_6_4
# 아래 함수를 수정하시오.
# def add_item_to_dict(dictionary, key, value):
#     new_dict = dictionary.copy()
#     new_dict[key] = value
#     return new_dict

# my_dict = {'name': 'Alice', 'age': 25}
# result = add_item_to_dict(my_dict, 'country', 'USA')
# print(result)


# ws_6_1
# 아래 함수를 수정하시오.
# def union_sets(set1, set2): 
#     return set1.union(set2)

# result = union_sets({1, 2, 3}, {3, 4, 5})
# print(result)


# ws_6_2
# 아래 함수를 수정하시오.
# def get_value_from_dict(d, k):
#     return d[k]


# my_dict = {'name': 'Alice', 'age': 25}
# result = get_value_from_dict(my_dict, 'name')
# print(result)  # Alice


# ws_6_3
# 아래 함수를 수정하시오.
# def intersection_sets(set1, set2):
#     return set1.intersection(set2)

# result = intersection_sets({1, 2, 3}, {3, 4, 5})
# print(result)


# ws_6_4
# 아래 함수를 수정하시오.
# def get_keys_from_dict(d):
#     return list(d.keys())


# my_dict = {'name': 'Alice', 'age': 25}
# result = get_keys_from_dict(my_dict)
# print(result)  # ['name', 'age']


# ws_6_5
# 아래 함수를 수정하시오.
# def difference_sets(set1, set2):
#     return set1.difference(set2)

# result = difference_sets({1, 2, 3}, {3, 4, 5})
# print(result)

