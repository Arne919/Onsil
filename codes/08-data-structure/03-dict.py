# D.clear()
# (딕셔너리 D의 모든 키/값 쌍을 제거)
# person = {'name': 'Alice', 'age': 25}
# person.clear()
# print(person) # {}

# D.get(key[,default])
# (키 k에 연결된 값을 반환; 키가 없으면 None을 반환)
# 키가 없으면 기본 값으로 [default]로 반환
# person = {'name': 'Alice', 'age': 25}
# print(person.get('name')) # Alice
# print(person.get('country')) # None
# print(person.get('country','Unknown')) # Unknown
# print(person['country']) # KeyError: 'country'

# D.keys() 
# 딕셔너리 D의 키를 모은 객체를 반환
# person = {'name': 'Alice', 'age': 25}
# print(person.keys()) # dict_keys(['name', 'age'])
# for item in person.keys():
#     print(item)
# '''
# name
# age
# '''

# D.values()
# 딕셔너리 D의 값를 모은 객체를 반환
# person = {'name': 'Alice', 'age': 25}
# print(person.values()) # dict_values(['Alice', 25])
# for item in person.values():
#     print(item)
# '''
# Alice
# 25
# '''

# D.items()
# 딕셔너리 키/값 쌍을 모은 객체를 반환
# person = {'name': 'Alice', 'age': 25}
# print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])
# for key, value in person.items():
#     print(key)
#     print(value)
# '''
# name
# Alice
# age
# 25
# '''

# D.pop(k)
# 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환(없으면 에러나 default를 반환)
# person = {'name': 'Alice', 'age': 25}
# print(person.pop('age')) # 25
# print(person) # {'name': 'Alice'}
# print(person.pop('country', None)) # None
# print(person.pop('country')) #KeyError: 'country'

# D.setdefault(key[, default])
# 딕셔너리 D에서 키 k와 연결된 값을 반환
# (k가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 v를 반환)
# setdefault 메서드 쓰면 if조건문 생략가능
# person = {'name': 'Alice', 'age': 25}
# print(person.setdefault('country', 'KOREA')) #KOREA
# print(person) #{'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# D.update(other)
# other가 제공하는 키/값 쌍으로 딕셔너리를 갱신
# 기존 키는 덮어씀
# person = {'name': 'Alice', 'age': 25}
# other_person = {'name': 'Jane', 'gender': 'Female'}
# person.update(other_person)
# print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}
# person.update(age=50, country='KOREA')
# print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}


# a = {}
# b = {'name': 'Alice', 'age': 25}
# a.update(b)
# print(a)
# b['name']='Harry'
# print(a)
# print(b)