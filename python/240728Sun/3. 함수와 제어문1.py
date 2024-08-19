# ws_3_a
def my_multi(number1, number2):
    return number1 * number2
result_1 = my_multi(2, 3)
print(result_1)

def is_negative(number):
    if number <= 0:
        return True
    else:
        return False
number = 3
result_2 = is_negative(number)
print(result_2)

def default_arg_func(default = '기본 값'):
    return default
result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')
print(result_3)
print(result_4)


# ws_3_b
pro_num = 1000
def increase_num():
    global pro_num
    pro_num += 1
    return pro_num
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}
def create_data(subject, day, title=None):
    data = {
        '과목': subject,
        '일차': day,
        '제목': title,
        '문제 번호': increase_num()
    }
    return data
result_1 = create_data('python', 3)
result_2 = create_data('web', 1, 'web 연습하기')
result_3 = create_data(**global_data)
print(result_1)
print(result_2)
print(result_3)


# ws_3_c
def recur_example(number):
    if number == 1:
        return 1
    else:
        return number + recur_example(number - 1)
result_1 = recur_example(5)
print(result_1)
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
result_2 = power(2, 3)
print(result_2)
def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number//10)
result_3 = sum_of_digits(321)
print(result_3)


# ws_3_1
number_of_people = 0
def increase_user():
    global number_of_people
    number_of_people += 1
increase_user()
print(f'현재 가입 된 유저 수: {number_of_people}')


# ws_3_2
number_of_people = 0
def increase_user():
    global number_of_people
    print(f'현재 가입 된 유저 수: {number_of_people}')
    number_of_people += 1
def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    return user_info
print(create_user('홍길동', 30, '서울'))
increase_user()


# ws_3_3
def rental_book(name, number):
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')
number_of_book = 100
def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수: {number_of_book}')
rental_book('홍길동', 3)


# ws_3_2
def add_number(num1, num2):
    return num1 + num2
result = add_number(3, 5)
print('3과 5를 인자로 넘긴 경우,')
print(result)


# ws_3_4
negative = -3
print(abs(negative))
empty_list = []
print(bool(empty_list))
my_list = [1, 2, 3, 4, 5]
print(sum(my_list))
unsorted_list = ['하', '교', '캅', '의', '지', '가']
print(sorted(unsorted_list))