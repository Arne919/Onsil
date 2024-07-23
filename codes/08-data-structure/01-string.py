# find(x) x의 첫번째 위치를 반환. 없으면 -1을 반환
# text = 'banana'
# print(text.find('a')) # 1
# print('banana'.find('z')) # -1
# print('banana'.find('na')) # 2

# index(x) x의 첫번째 위치를 반환. 없으면 오류 발생
# print(text.index('a')) # 1
# print(text.index('z')) # ValueError: substring not found

# isupper(x)/islower(x) 문자열이 모두 대문자/소문자로 이루어져 있는지 확인
# string1 = 'HELLO'
# string2 = 'Hello'
# print(string1.isupper()) # T
# print(string2.isupper()) # F
# print(string1.islower()) # F
# print(string2.islower()) # F

# isalpha(x) 문자열이 알파벳으로만 이루어져 있는지 확인
# string3 = 'Hello'
# string4 = '123'
# print(string3.isalpha()) # T
# print(string4.isalpha()) # F

# replace(old, new[,count]) 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
# text = 'Hello, world!'
# new_text = text.replace('world', 'Python')
# print(new_text) #Hello, Python!

# strip([chars]) 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
# text = '  Hello, world!   '
# new_text = text.strip()
# print(new_text) # Hello, world!


# split(sep=None, maxsplit=-1) 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환
# text = 'Hello, world!'
# words = text.split(',')
# words2 = text.split()
# print(words) # ['Hello', 'words!']
# print(words) # ['Hello,', 'world!']


# join  iterable 의 문자열을 연결한 문자열을 반환
# words = ['Hello', 'world!']
# text = '-'.join(words)
# print(text) #Hello-world!

# capitalize 첫번째단어를 대문자로 반환
# text = 'heLLo, woRld!'
# new_text1 = text.capitalize()
# print(new_text1) #Hello, world!

# title 각 문자열의 첫번째 단어를 대문자로 반환
# new_text2 = text.title()
# print(new_text2) #Hello, World!

# upper 모두 대문자로 반환
# new_text3 = text.upper()
# print(new_text3) #HELLO, WORLD!

# lower 모두 소문자로 반환
# new_text4 = text.lower()
# print(new_text4) #hello, world!

# swapcase 대문자<->소문자 변경 후 반환
# new_text5 = text.swapcase()
# print(new_text5) #HEllO, WOrLD!

#메서드 이어서 사용하기(모든 메서드는 이어서 사용가능)
# text = 'heLLo, woRld!'
# new_text0 = text.swapcase().replace('l', 'z')
# print(new_text0) #HEzzO, WOrLD!
# new_text0 = text.swapcase().replace('L', 'z')
# print(new_text0) #HEllO, WOrzD!

# # 참고
# # isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
# print("isdecimal() 메서드 예시:") #isdecimal() 메서드 예시:
# print("'12345'.isdecimal():", '12345'.isdecimal()) #'12345'.isdecimal(): True
# print("'123.45'.isdecimal():", '123.45'.isdecimal()) #'123.45'.isdecimal(): False
# print("'-123'.isdecimal():", '-123'.isdecimal()) #'-123'.isdecimal(): False
# print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal()) #'Ⅳ'.isdecimal(): False
# print("'½'.isdecimal():", '½'.isdecimal()) #'½'.isdecimal(): False
# print("'²'.isdecimal():", '²'.isdecimal()) #'²'.isdecimal(): False
# print() #\n

# # isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
# print("isdigit() 메서드 예시:") #isdigit() 메서드 예시:
# print("'12345'.isdigit():", '12345'.isdigit()) #'12345'.isdigit(): True
# print("'123.45'.isdigit():", '123.45'.isdigit()) #'123.45'.isdigit(): False
# print("'-123'.isdigit():", '-123'.isdigit()) #'-123'.isdigit(): False
# print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit()) #'Ⅳ'.isdigit(): False
# print("'½'.isdigit():", '½'.isdigit()) #'½'.isdigit(): False
# print("'²'.isdigit():", '²'.isdigit()) #'²'.isdigit(): True
# print() #\n

# # isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
# print("isnumeric() 메서드 예시:") #isnumeric() 메서드 예시:
# print("'12345'.isnumeric():", '12345'.isnumeric()) #'12345'.isdigit(): True
# print("'123.45'.isnumeric():", '123.45'.isnumeric()) #'123.45'.isdigit(): False
# print("'-123'.isnumeric():", '-123'.isnumeric()) #'-123'.isdigit(): False
# print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric()) #'Ⅳ'.isdigit(): True
# print("'½'.isnumeric():", '½'.isnumeric()) #'½'.isdigit(): True
# print("'²'.isnumeric():", '²'.isnumeric()) #'²'.isdigit(): True
