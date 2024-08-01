#240723복습(240723)

#3. dict
# # clear
# person = {'name': 'Alice', 'age': 25}
# person.clear()
# print(person) # {}

# # get
# person = {'name': 'Alice', 'age': 25}
# print(person.get('name')) # Alice
# print(person.get('country')) # None
# print(person.get('country','Unknown')) # Unknown
# print(person['country']) # Error

# # keys
# person = {'name': 'Alice', 'age': 25}
# print(person.keys())
# for item in person.keys():
#     print(item)
'''
dict_keys(['name', 'age'])
name
age
'''

# # values
# person = {'name': 'Alice', 'age': 25}
# print(person.values())
# for item in person.values():
#     print(item)
'''
dict_values(['Alice', 25])
Alice
25
'''

# # items
# person = {'name': 'Alice', 'age': 25}
# print(person.items())
# for key, value in person.items():
#     print(key)
#     print(value)
'''
dict_items([('name', 'Alice'), ('age', 25)])
name
Alice
age
25
'''

# # pop
# person = {'name': 'Alice', 'age': 25}
# print(person.pop('age'))
# print(person)
# print(person.pop('country', None))
# print(person.pop('country'))
'''
25
{'name': 'Alice'}
None
Error
'''

# # setdefault(key[,default])
# person = {'name': 'Alice', 'age': 25}
# print(person.setdefault('country', 'KOREA'))
# print(person)
'''
KOREA
{'name': 'Alice', 'age': 25, 'country': 'KOREA'}
'''

# # update <보통 딕셔너리 복사할 때
# person = {'name': 'Alice', 'age': 25}
# other_person = {'name': 'Jane', 'gender': 'Female'}
# person.update(other_person)
# print(person)
# person.update(age=50, country='KOREA')
# print(person)
'''
{'name': 'Jane', 'age': 25, 'gender': 'Female'}
{'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}
'''


#4. set
# # add
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.add(4)
# print(my_set)
'''
{'c', 1, 2, 3, 4, 'a', 'b'}
'''

# # clear
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.clear()
# print(my_set)
'''
set()
'''

# # remove
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.remove(2)
# print(my_set)
# my_set.remove(10)
# print(my_set)
'''
{1, 3, 'b', 'a', 'c'}
Error
'''

# # pop
# my_set = {'a', 'b', 'c', 1, 2, 3}
# element = my_set.pop()
# print(element)
# print(my_set)
'''
a
{1, 2, 3, 'b', 'c'}
***임의의 랜덤한 요소가 제거됨
'''

# # discard
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.discard(2)
# print(my_set)
# my_set.discard(10)
# print(my_set)
'''
{1, 3, 'a', 'c', 'b'}
{1, 3, 'a', 'c', 'b'};아무일도일어나지않음
'''

# # update
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.update([1, 4, 5])
# print(my_set)
'''
{'c', 1, 'a', 3, 2, 4, 5, 'b'}
'''

# # 집합 메서드
# set1 = {0, 1, 2, 3, 4}
# set2 = {1, 3, 5, 7, 9}
# set3 = {0, 1}
# print(set1.difference(set2))
# print(set1.intersection(set2))
# print(set1.issubset(set2))
# print(set3.issubset(set1))
# print(set1.issuperset(set2))
# print(set1.issuperset(set3))
# print(set1.union(set2))
'''
{0, 2, 4}
{1, 3}
False
True
False
True
{0, 1, 2, 3, 4, 5, 7, 9}
'''

### sort 와 sorted 차이
'''
sorted() 내장함수
list.sort() 리스트 메서드< 사용제한적
'''


# python_ws_6_c
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

# 아래에 코드를 작성하시오.
for d in data: #dict
    for k in key_list: #str
        if d.get(k) == None:
            d.setdefault(k, 'unKnown')
        print(f'{k}은/는 {d.get(k)}입니다.')
        #1 # value = d.get(k, 'unknown')
        #2 # d.setdefault(k, 'unknown')
        #1,2 # print(f'{k}은/는 {value}입니다.')
    print()
