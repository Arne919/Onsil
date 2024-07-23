# 아래의 예시코드를 작성 가능해야함


# append(x) 리스트 마지막에 항목 x를 추가
my_list = ['a', 'b', 'c']
my_list.append('d')
print(my_list) #['a', 'b', 'c', 'd']
print(my_list.append(4)) #None
print(my_list[3]) #d
print(my_list[4]) #4 print(my_list.append(4)) 에서 출력도 요청하지만 추가도 함

# extend(iterable) 리스트에 다른 반복 가능한 객체의 모든 항목을 추가
# my_list = [1, 2, 3]
# my_list.extend([4,5,6])
# print(my_list) #[1, 2, 3, 4, 5, 6]

# insert(i,x) 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입(추가)
# my_list = [1, 2, 3]
# my_list.insert(1,5)
# print(my_list) [1, 5, 2, 3]

# remove(x) 리스트에서 첫번째로 일치하는 항목 삭제
# my_list = [1, 2, 3]
# my_list.remove(2)
# print(my_list) # [1, 3]

# pop(i) 리스트에서 지정한 인덱스의 항목을 제거하고 반환
# 작성하지 않을 경우 마지막 항목을 제거
# my_list = [1, 2, 3, 4, 5]
# item1 = my_list.pop()
# item2 = my_list.pop(0)
# print(item1) # 5
# print(item2) # 1
# print(my_list) # [2, 3, 4]

# clear() 리스트의 모든 항목을 삭제
# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list) # []

# index(x) 리스트에서 첫번째로 일치하는 항목 x의 인덱스를 반환
# my_list = [1, 2, 3]
# index = my_list.index(2)
# print(index) # 1

# count(x) 리스트에서 항목 x의 개수를 반환
# my_list = [1, 2, 2, 3, 3, 3]
# count = my_list.count(3)
# print(count) # 3

# reverse() 리스트의 순서를 역순으로 변경(정렬 X)
# my_list = [1, 3, 2, 8, 1, 9]
# my_list.reverse()
# print(my_list) #[9, 1, 8, 2, 3, 1]

# sort() 원본 리스트를 오름차순으로 정렬
# my_list = [3, 2, 100, 1]
# my_list.sort() #오름차순
# print(my_list) #[1, 2, 3, 100]

# sort(내림차순 정렬)
# my_list.sort(reverse=True)
# print(my_list) #[100, 3, 2, 1]