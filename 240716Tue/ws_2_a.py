# [0]
zero_list = [0]
print(zero_list)

# 숫자 0을 25만개 가지고 있는 리스트 할당
# 리스트와 곱셈 연산자를 활용하여 할당
# 250000
many_zero_list = [0]
print(len((many_zero_list)*250000))

# numbers 변수에 range를 활용하여 1~10수를 가진 리스트 할당
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = range(1, 11)
print(list(numbers))

# numbers의 3번째(index)부터 마지막 요소까지 출력
# [4, 5, 6, 7, 8, 9, 10]
print(list(numbers[3:]))
