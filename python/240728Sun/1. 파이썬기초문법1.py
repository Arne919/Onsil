# ws_1_a
print('안녕하세요')


# ws_1_b
korean = '한글'
english = 'english'
number = 3
print(f'{korean}과 {english}')
print(korean * 3)


# ws_1_c
password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
first_char = password[28:35]
second_word = password[113:118]
third_word = password[68:65:-1]
fourth_word = password[325:321:-1]
fifth_word = password[365:371]
print(f'{first_char} {second_word} {third_word} {fourth_word} \"{fifth_word}\".')


# ws_1_1
name = '홍길동'
age = 20
s = '이름 : '
s2 = '나이 : '
s3 = '학생 정보를 출력합니다.'
s4 = '각각의 정보는 다음과 같습니다'
s5 = '출력 완료'
print(s3)
print(s4)
print(s, name)
print(s2, age)
print(s5)


# ws_1_2
#주어진 각 데이터들의 data type을 출력하여 결과를 확인하시오.
string = '문자열'
integer = 10
floating_point = 3.14
a_list = [1, 2, 3, 4, 5]
dictionary = {'name': '홍길동', 'age': 20}
a_set = {1, 2, 3, 4, 5}
a_range = range(11)
a_tuple = (1, 2, 3)
boolean = True
print(type(string))
print(type(integer))
print(type(floating_point))
print(type(a_list))
print(type(dictionary))
print(type(a_set))
print(type(a_range))
print(type(a_tuple))
print(type(boolean))


# ws_1_3
# 주어진 문자열들을 적절한 변수에 할당하여 예시 화면과 동일하게 출력 될 수 있도록 코드를 작성하시오.
a1 = '반짝 반짝'
b1 = '에서도'
a2 = '작은 별'
a3 = '아름답게 비치네'
b2 = '동쪽 하늘'
b3 = '서쪽 하늘'
print(f'{a1} {a2} {a3}')
print(f'{b2}{b1} {b3}{b1}')
print(f'{a1} {a2} {a3}')


# hw_1_2
word = 'Hello, World!'
print(word)


# hw_1_4
# 사과는 영어로 apple
# 바나나는 영어로 banana
# 키위는 영어로 kiwi
a1 = '사과는'
a2 = 'apple'
b1 = '바나나는'
b2 = 'banana'
k1 = '키위는'
k2 = 'kiwi'
english = '영어로'
print(f'{a1} {english} {a2}')
print(f'{b1} {english} {b2}')
print(f'{k1} {english} {k2}')
