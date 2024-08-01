# study

# print('Hello World')

# number = 10
# double = 2 * number
# print(double) # 20

# number = 5
# print(double) # 20

# print(0b10)
# print(0o10)
# print(0x10)

# a = 3.2 - 3.1
# b = 1.2 - 1.1
# print(a)
# print(b)
# print(a==b)

# from decimal import Decimal #모듈
# a = Decimal('3.2') - Decimal('3.1')
# b = Decimal('1.2') - Decimal('1.1')
# print(a)
# print(b)
# print(a==b)

# number = 314e-2
# print(number) #3.14
# print(type(number)) # <class 'float'>
# print(type('number')) # <class 'str'>

# print('Hello World!') # Hello World!
# print(type('Hello World!')) #<class 'str'>

# print("문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.") # 문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.
# print('문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.') # 문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.

# print('철수야 \'안녕\'')
# print('이 다음은 엔터\n입니다.')

# bugs = 'roaches'
# counts = 13
# area = 'living room'
# print(f'Debugging {bugs} {counts} {area}') # Debugging roaches 13 living room

# my_str = 'hello'
# print(my_str[1]) # e
# print(my_str[2:4]) #ll
# print(len(my_str)) #5
# print(my_str[5:0:-3]) #oe

# my_list_1 = []
# my_list_2 = [1, 'a', 3, 'b', 5]
# my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
# print(my_list_3[4][0][0])
# print(my_list_3[4][0][::-1])
# print(len(my_list_3[4]))
# my_list = [1,2,3]
# my_list[0] = 100
# print(my_list) #[100, 2, 3]

# my_tuple_1 = ()
# my_tuple_2 = (1,)
# my_tuple_3 = (1, 'a', 3, 'b', 5)
# print(my_tuple_1)
# print(my_tuple_2)
# print(my_tuple_3)
# my_tuble = (1, 'a', 3, 'b', 5)
# print(my_tuble[1]) #a
# print(my_tuble[2:4]) #(3, 'b')
# print(my_tuble[:3]) #(1, 'a', 3)
# print(my_tuble[0:5:2]) #(1, 3, 5)
# print(my_tuble[::-1]) #(5, 'b', 3, 'a', 1)
# print(len(my_tuple))  # 5
# x,y = (10, 20)
# print(x) #10
# print(y) #20

# my_range_1 = range(5)
# my_range_2 = range(1,10)
# print(my_range_1) #range(0, 5)
# print(my_range_2) #range(1, 10)
# print(list(range(5))) #[0, 1, 2, 3, 4]
# print(list(my_range_1)) #[0, 1, 2, 3, 4]
# print(list(my_range_2)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(1,10):
#     print(i)
# for i in range(1,10,2):
#     print(i)

# my_dict_1 = {}
# my_dict_2 = {'key': 'value'}
# my_dict_3 = {'apple': 12, 'list': [1,2,3]}
# print(my_dict_1)
# print(my_dict_2)
# print(my_dict_3)
# print(my_dict_3['list'])
# my_dict_3['banana'] = 50
# print(my_dict_3)
# my_dict_3['banana'] = 1000
# print(my_dict_3)
# print(len(my_dict_3))

# my_set_1 = set()
# my_set_2 = {1,2,3}
# my_set_3 = {1,1,1}
# print(my_set_1)
# print(my_set_2)
# print(my_set_3)

# my_set_1 = {1,2,3}
# my_set_2 = {3,6,9}
# print(my_set_1 | my_set_2) # 합
# print(my_set_1 - my_set_2) # 차
# print(my_set_1 & my_set_2) # 교

# variable = None
# print(variable) #None

# bool_1 = True
# bool_2 = False
# print(bool_1) #True
# print(bool_2) #False
# print(3<1) #False
# print('3'!= 3) #True

# print(3+5.0) #8.0
# print(True +3) #4
# print(True+False) #1
# print(True) #True
# print(False) #False

# print(int('1')) #1
# print(int(3.5)) #3
# print(int('3.5')) #실행안됨
# print(float('3.5')) #3.5
# print(str(1)+'등') #1등

# y=10
# y-=4
# print(y) #6

# z=7
# z*=2
# print(z) #14

# w=15
# w/=4
# print(w) #3.75

# q=20
# q//=3
# print(q) #6

# print(3>6) #False
# print(2.0 == 2) #True
# print(2 != 2) #False
# print('HI' == 'hi') #False
# print(1==True) #True (암시적 형변환)
# print(1 is True) #False (==는 값(데이터)를 비교하는것이고, is는 레퍼런스(주소)를 비교하는것)
# print(2 is 2.0) #False
# print(1==True)
# print(2==2.0)
# print(1==None)

# print(True and False) #False
# print(True or False) #True
# print(not True) #False
# print(not 0) #False

# num = 15
# result = (num>10) and (num%2==0) #False
# print(result)

# name = 'Alice'
# age = 25
# result = (name == 'Alice') or (age == 30)
# print(result) #True

# vowels = 'aeiou'

# print(('a' and 'b') in vowels) #'a'는 문자열 True -> 'b' in vowels False => False
# print(('b' and 'a') in vowels) #'b'는 문자열 True -> 'a' in vowels True => True
# print(3 and 5) #5(둘다 True)
# print(5 and 3) #3(둘다 True)
# print(0 and 3) #0(첫번째부터 False기때문에 단축평가)
# print(0 and 0) #0(첫번째부터 False기때문에 단축평가)

# print(5 or 3) #5(첫번째부터 True기때문에 단축)
# print(3 or 0) #3(첫번째부터 True기때문에 단축)
# print(0 or 3) #3(첫번째 False라서 두번째까지 갔는데 True기때문에 True출력)
# print(0 or 0) #0(1,2번째 둘다 False기때문에 False)

# word = 'hello'
# numbers = [1,2,3,4,5]
# print('h' in word) #True
# print('z' in word) #False
# print(4 not in numbers) #False
# print(6 not in numbers) #True

# print('Gildong' + 'Hong') #GildongHong
# print('hi' * 5) #hihihihihi
# print([1,2] + ['a','b']) #[1, 2, 'a', 'b']
# print([1,2] * 2) #[1, 2, 1, 2]
