# ws_6_a
my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }
for key in my_set:
    print(my_dict.get(key, 'None'))
my_dict[(1,2,3,'A')]='변수로도 키 설정 가능'
print(my_dict)


# ws_6_b
data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}
# 1. data가 가진 모든 키와 벨류 목록을 출력한다.
print(data.items())
# 2. data가 가진 벨류 목록들만 모아서 출력한다.
print(data.values())
# 3. data에서 'without' 키가 가진 value를 출력한다.
# 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
print(data.pop('without', 'unknown'))
# 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
data.update(plus_data)
print(data)


# ws_6_c
data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']
for d in data:
    for k in key_list:
        if d.get(k) == None:
            d.setdefault(k, 'unKnown')
        print(f'{k}은/는 {d.get(k)}입니다.')
    print()


# ws_6_1
def union_sets(set1, set2):
    return set1.union(set2)
result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)


# ws_6_2
def get_value_from_dict(d, k):
    return d[k]
my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)


# ws_6_3
def intersection_sets(set1, set2):
    return set1.intersection(set2)
result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)


# ws_6_4
def get_keys_from_dict(d):
    return list(d.keys())
my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)


# ws_6_5
def difference_sets(set1, set2):
    return set1.difference(set2)
result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)


# hw_6_2
def remove_duplicates_to_set(list):
    new_list = []
    for num in list:
        if num not in new_list:
            new_list.append(num)
    return set(new_list)

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)


# hw_6_4
def add_item_to_dict(dictionary, key, value):
    new_dict = dictionary.copy()
    new_dict[key] = value
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)