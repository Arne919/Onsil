#240723복습(240718)

#1. if문
# a = 3
# if a > 3:
#     print('3 초과')
# else:
#     print('3 이하')
# print(a)
'''
3 이하
3
'''

# dust = 480
# if dust > 150:
#     print('매우 나쁨')
#     if dust > 300:
#         print('위험해요!')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# else:
#     print('좋음')
'''
매우 나쁨
위험해요!
'''

#2. for문
# items = ['apple', 'banana', 'coconut']
# for item in items:
#     print(item)
'''
apple
banana
coconut
'''

# country = 'Korea'
# for char in country:
#     print(char)
'''
K
o
r
e
a
'''

# for i in range(5):
#     print(i)
'''
0
1
2
3
4
'''

# my_dict = {
#     'x': 10,
#     'y': 20,
#     'z': 30
# }
# for key in my_dict:
#     print(key)
#     print(my_dict[key])
'''
x
10
y
20
z
30
'''

# numbers = [4, 6, 10, -8, 5]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
# print(numbers)
'''
[8, 12, 20, -16, 10]
'''

# outers = ['A', 'B']
# inners = ['c', 'd']
# for outer in outers:
#     for inner in inners:
#         print(outer, inner)
'''
A c
A d
B c
B d
'''

# elements = [
#     ['A', 'B'],
#     ['c', 'd']
# ]
# for elem in elements:
#     for item in elem:
#         print(item)
'''
A
B
c
d
'''

#3. while문
# a = 0
# while a < 3:
#     print(a)
#     a += 1
# print('끝')
'''
0
1
2
끝
'''

# number = int(input('양의 정수를 입력해주세요.: '))
# while number <= 0:
#     if number < 0:
#         print('음수를 입력했습니다.')
#     else:
#         print('0은 양의 정수가 아닙니다.')
#     number = int(input('양의 정수를 입력해주세요.: '))
# print('잘했습니다.')
'''
양의 정수를 입력해주세요.: -1
음수를 입력했습니다.
양의 정수를 입력해주세요.: 0
0은 양의 정수가 아닙니다.
양의 정수를 입력해주세요.: 1
잘했습니다.
'''

#break
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
'''
0
1
2
3
4
'''

#continue
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
'''
1
3
5
7
9
'''

#pass
# for i in range(10):
#     pass

# def my_func(a):
#     pass

#break ex1) - '프로그램 종료 조건 만들기'
# number = int(input('양의 정수를 입력해주세요.: '))
# while number <= 0:
#     if number == -9999:
#         print('프로그램을 종료합니다.')
#         break
#     if number < 0:
#         print('음수를 입력했습니다.')
#     else:
#         print('0은 양의 정수가 아닙니다.')
#     number = int(input('양의 정수를 입력해주세요.: '))
# print('잘했습니다!')

#break ex2) - '리스트에서 첫번째 짝수만 찾은 후 반복 종료하기'
# numbers = [1, 3, 5, 6, 7, 9, 10, 11]
# fount_even = False # flag variable
# for number in numbers:
#     if number % 2 == 0:
#         print(f'첫번째 짝수 {number}를 찾았습니다.')
#         found_even = True
#         break
# if found_even == False:
#     print('짝수를 찾지 못함')

#continue ex) = '리스트에서 홀수만 출력하기'
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     if number % 2 == 0:
#         continue
#     print(number)
'''
1
3
5
7
9
'''


#5. list comprehension
#사용 전
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = []

# for num in numbers:
#     squared_numbers.append(num**2)

# print(squared_numbers)
'''
[1, 4, 9, 16, 25]
'''

#사용 후
# numbers = [1, 2, 3, 4, 5]

# squared_numbers2 = [num**2 for num in numbers]
# squared_numbers2 = list(num**2 for num in numbers)
# print(squared_numbers2)
'''
[1, 4, 9, 16, 25]
'''

# list comprehension 활용 예시 - '2차원 배열 생성 시(인접행렬 생성 시)'
# data1 = [[0] * (5) for _ in range(5)]
# print(data1)
# #또는
# data2 = [[0 for _ in range(5)] for _ in range(5)]
# print(data2)
'''
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''


#99. make list
#1. loop
# result1 = []
# for i in range(10):
#     result1.append(i)

# #2. list comprehension
# result2 = [i for i in range(10)]
# #result2 = list(i for i in range(10))

# #3. map
# result3 = list(map(lambda i: i, range(10)))

# print(result1)
# print(result2)
# print(result3)
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''


'''
성능 비교
1. list comprehension
    대부분의 경우 가장 빠르고 파이썬스로운(Pythonic) 방법
2. map
 -  특정 상황(예: 기존 함수를 사용할 때)에서 리스트 컴프리핸션과 비슷하거나 약간 더 빠를 수 있음
3. loop
 -  일반 적으로 가장 느리다고 알려져 있지만,
    python 버전이 올라가면서 다른 방식과 비슷하거나 때로는 더 나은 결과를 보이기도 함
 -  복잡한 로직이 필요한 경우에는 여전히 유용하게 사용 될 수 있음

결론
-   성능 차이는 대부분의 경우 미미하므로,
    코드의 가독성과 유지보수성을 고려하여 사오항에 맞는 적절한 방법을 선택하는 것을 권장
'''

#99.enumerate
# fruits = ['apple', 'banana', 'cherry']

# for index, fruit in enumerate(fruits):
#     print(f'인덱스 {index}: {fruit}')
'''
인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
'''
# for index, fruit in enumerate(fruits):
#     print(index, fruit)
# for index, fruit in enumerate(fruits, 3):
#     print(index, fruit)
'''
0 apple
1 banana
2 cherry
3 apple
4 banana
5 cherry
'''