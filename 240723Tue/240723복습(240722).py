#240723복습(240722)

# print(help(str))

#1. string
# #find
# text = 'banana'
# print(text.find('a')) # 1
# print('banana'.find('z')) # -1
# print('banana'.find('na')) # 2

# #index
# print(text.index('a')) # 1
# print(text.index('z')) # error

# # isupper/islower
# string1 = 'HELLO'
# string2 = 'Hello'
# print(string1.isupper()) # T
# print(string2.isupper()) # F
# print(string1.islower()) # F
# print(string2.islower()) # F

# # isalpha
# string3 = 'Hello'
# string4 = '123'
# print(string3.isalpha()) # T
# print(string4.isalpha()) # F

# # replace(old, new[,count])
# text = 'Hello, world'
# new_text = text.replace('world', 'python')
# print(new_text) # Hello, python
# text = 'Hello, world! world! world!'
# new_text = text.replace('world', 'python', 1)
# print(new_text) # Hello, python! world! world!

# #strip[(char)]
# text = '    Hello, world!   '
# new_text = text.strip()
# print(new_text) # Hello, world!

# # split(sep=None, maxsplit=-1)
# # separameter 기본값
# text = 'Hello, world!'
# words = text.split(',')
# words2 = text.split()
# print(words) # ['Hello', ' world!']
# print(words2) # ['Hello,', 'world!']

# # join interable의 문자열을 연결한 문자열을 반환
# words = ['Hello', 'world!']
# text = '-'.join(words)
# print(text) # Hello-world!

# # capitalize
# text = 'heLLo, woRld!'
# new_text1 = text.capitalize()
# print(new_text1) # Hello, world!

# # title
# new_text2 = text.title()
# print(new_text2) # Hello, World!

# # upper
# new_text3 = text.upper()
# print(new_text3) # HELLO, WORLD!

# # lower
# new_text4 = text.lower()
# print(new_text4) # hello, world!

# # swapcase
# new_text5 = text.swapcase()
# print(new_text5) #HEllO, WOrLD!

# # 메서드 이어서 사용하기(chaining)
# text = 'heLLo, woRld!'
# new_text0 = text.swapcase().replace('l', 'z')
# print(new_text0) # HEzzO, WOrLD!
# new_text0 = text.swapcase().replace('L', 'z')
# print(new_text0) # HEllO, WOrzD!


#2. list
# # append
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list) # [1, 2, 3, 4]
# print(my_list.append(4)) # None

# # extend
# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list) # [1, 2, 3, 4, 5, 6]
# my_list.extend([5])
# print(my_list) # [1, 2, 3, 4, 5, 6, 5]
# my_list.append([9, 9, 9])
# print(my_list) # [1, 2, 3, 4, 5, 6, 5, [9, 9, 9]]

# # insert
# my_list = [1, 2, 3]
# my_list.insert(1,5)
# print(my_list) # [1, 5, 2, 3]

# # remove
# my_list = [1, 2, 3]
# my_list.remove(2)
# print(my_list) # [1, 3]

# # pop
# my_list = [1, 2, 3, 4, 5]
# item1 = my_list.pop()
# item2 = my_list.pop(0)
# print(item1) # 5
# print(item2) # 1
# print(my_list) # [2, 3, 4]

# # clear
# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list) # []

# # index
# my_list = [1, 2, 3]
# index = my_list.index(2)
# print(index) # 1

# # count
# my_list = [1, 2, 2, 3, 3, 3]
# count = my_list.count(3)
# print(count) # 3

# # reverse
# my_list = [1, 3, 2, 8, 1, 9]
# my_list.reverse()
# print(my_list) # [9, 1, 8, 2, 3, 1]

# # sort
# my_list = [3, 2, 100, 1]
# my_list.sort()
# print(my_list) # [1, 2, 3, 100]

# # sort(내림차순 정렬)
# my_list.sort(reverse=True)
# print(my_list) # [100, 3, 2, 1]



#99. copy
# # 할당 (객체 참조를 복사하기 때문이다.)
# # 가변 데이터
# a = [1, 2, 3, 4]
# b = a
# b[0] = 100

# print(a)
# print(b)
'''
[100, 2, 3, 4]
[100, 2, 3, 4]
'''

# # 불변 데이터
# a = 20
# b = a
# b = 10

# print(a)
# print(b)
'''
20
10
'''

# # 얕은 복사
# a = [1, 2, 3]
# b = a[:]

# b[0] = 100
# print(a)
# print(b)
'''
[1, 2, 3]
[100, 2, 3]
'''
# a = [1, 2, 3]
# b = a[:]
# c = a.copy()

# b[0] = 100
# c[0] = 999
# print(a)
# print(b)
# print(c)
'''
[1, 2, 3]
[100, 2, 3]
[999, 2, 3]
'''

# # 얕은 복사의 한계
# a = [1, 2, [3, 4, 5]]
# b = a[:]
# b[2][1] = 100
# print(a)
# print(b)
'''
[1, 2, [3, 100, 5]]
[1, 2, [3, 100, 5]]
'''

# a = [1, 2, [3, 4, 5]]
# b = a[:]
# b[0] = 999
# b[2][1] = 100
# print(a)
# print(b)
'''
[1, 2, [3, 100, 5]]
[999, 2, [3, 100, 5]]
'''
# -> a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨


# # 깊은 복사 (내장모듈 활용) 원본을 훼손하면 안될때
import copy
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)
b[2][1] = 100
print(a)
print(b)
'''
[1, 2, [3, 4, 5]]
[1, 2, [3, 100, 5]]
'''