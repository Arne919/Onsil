# s.add(x)
# 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.add(4)
# print(my_set) #{'a', 1, 2, 3, 4, 'b', 'c'}

# s.clear()
# 세트의 모든 항목을 제거
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.clear()
# print(my_set) # set()

# s.remove(x)
# 세트에서 항목 x를 제거
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.remove(2)
# print(my_set) #{1, 3, 'a', 'b', 'c'}
# my_set.remove(10)
# print(my_set) # KeyError: 10

# .pop()
# 세트에서 임의의 요소를 제거하고 반환
# my_set = {'a', 'b', 'c', 1, 2, 3}
# element = my_set.pop()
# print(element)
# print(my_set)

# .discard()
# 세트 s에서 항목 x를 제거. remove와 달리 에러 없음
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.discard(2)
# print(my_set) # {1, 'c', 3, 'b', 'a'}
# my_set.discard(10)
# print(my_set) # {1, 'c', 3, 'b', 'a'} ;아무일도일어나지않음

# .update(iterable) 
# 세트에 다른 iterable 요소를 추가 (iterable는 list를 말한다.)
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.update([1, 4, 5])
# print(my_set) # {'b', 1, 2, 3, 'a', 4, 5, 'c'}

# 집합 메서드
# set1 = {0, 1, 2, 3, 4}
# set2 = {1, 3, 5, 7, 9}
# set3 = {0, 1}

# print(set1.difference(set2)) # {0, 2, 4}
# print(set1.intersection(set2)) # {1, 3}
# print(set1.issubset(set2)) # False
# print(set3.issubset(set1)) # True 
# print(set1.issuperset(set2)) # False
# print(set1.issuperset(set3)) # True 
# print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}