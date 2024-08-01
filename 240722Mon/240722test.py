# 240722test


# N = 9
# data_1 = '123456789'
# arr_1 = []
# # 아래에 코드를 작성하시오.
# for i in data_1:
#     arr_1.append(i)
# print(arr_1)


# M = 15
# data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# # 아래에 코드를 작성하시오.
# arr_2 = []
# arr_2 = data_2.split(' ')

# for i in arr_2:
#     if (int(i)+2)%2 == 1:
#         print(i)


# data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
# '''
# 예시코드
# arr = [1, 2, 3, 4, 5]
# for num in arr:
#     print(num, end='')
# 출력결과 : 12345
# '''
# # 아래에 코드를 작성하시오.
# result = '' #빈문자열 초기화
# for char in data_1:
#     # 대문자이거나 공백인 경우
#     if char.isupper() or char == ' ':
#         result += char
# print(result)


# data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
# arr = []
# # 아래에 코드를 작성하시오.
# tired = ['내','힘','들','다']
# for i in tired:
#     arr.append(data_2.find(i))
# print(arr)


# arr.sort()
# print(arr)


# result = ''
# for char in arr:
#     result += data_2[char]
# print(result)



# data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
# '''
# 예시코드
# arr = [1, 2, 3, 4, 5]
# for num in arr:
#     print(num, end='')
# 출력결과 : 12345
# '''
# # 아래에 코드를 작성하시오.
# for char in data_1:
#     # 대문자이거나 공백인 경우
#     if char.isupper() or char == ' ':
#         print(char, end='')
# print()


# data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
# arr = []
# # 아래에 코드를 작성하시오.
# word ='내힘들다'
# # word = ['내','힘','들','다']
# for i in word:
#     arr.append(data_2.find(i))
# print(arr)


# arr.sort()
# print(arr)


# for char in arr:
#     print(data_2[char], end='')


# def restructure_word(word, arr):
#     # pass
#     for char in word: #word 를 한글자씩
#         if char.isdecimal(): #word 속 숫자일때
#             for i in range(int(char)): #숫자를 정수로 바꾸고 해당숫자만큼 반복
#                 arr.pop() #()공백일때 맨뒤부터 없앰
#         else: #word 속 숫자아닐때
#             if char in arr:
#                 arr.remove(char)
#     return arr

# original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
# word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
# arr = []

# for char in original_word:
#     arr.extend(char)
# print(arr)

# result = restructure_word(word,arr)
# print(result)

# text = ''.join(result)
# print(text)


# 아래 함수를 수정하시오.
# def count_character(input_string, find_string):
#     count = 0
#     for char in input_string:
#         if char == find_string:
#             count += 1
#     return count

    
# result = count_character("Hello, World!", "o")
# print(result)  # 2


# 아래 함수를 수정하시오.
# def find_min_max(_list):
#     _list.sort()
#     return _list[0],_list[len(_list)-1]

# result = find_min_max([3, 1, 7, 2, 5])
# print(result)  # (1, 7)


# 아래 함수를 수정하시오.
# def reverse_string(char):
#     _char = list(char)
#     _char.reverse()
#     char2 = ''.join(_char)
#     return char2

# result = reverse_string("Hello, World!")
# print(result)  # !dlroW ,olleH



# 아래 함수를 수정하시오.
# def remove_duplicates(list):
#     new_lst = []
#     for num in list:
#         if num not in new_lst:
#             new_lst.append(num)
#     return new_lst


# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)


# 아래 함수를 수정하시오.
# def sort_tuple(num):
#     new_tuple = tuple(sorted(num))
#     return new_tuple

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)


# 아래 함수를 수정하시오.
# def capitalize_words(char):
#     words = char.split()
#     text = []
#     for word in words:
#         cha = word.capitalize()
#         text.append(cha)
#     return ' '.join(text)
    
# result = capitalize_words("hello, world!")
# print(result) # Hello, World!


# 아래 함수를 수정하시오.
def even_elements(my_list):
    arr = []
    for i in my_list:
        if (int(i)+2)%2 ==0:
            arr.append(i)
    return arr

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

# pop(i) 리스트에서 지정한 인덱스의 항목을 제거하고 반환
# 작성하지 않을 경우 마지막 항목을 제거
# my_list = [1, 2, 3, 4, 5]
# item1 = my_list.pop()
# item2 = my_list.pop(0)
# print(item1) # 5
# print(item2) # 1
# print(my_list) # [2, 3, 4]

# extend(iterable) 리스트에 다른 반복 가능한 객체의 모든 항목을 추가
# my_list = [1, 2, 3]
# my_list.extend([4,5,6])
# print(my_list) #[1, 2, 3, 4, 5, 6]


# arr_2 = []
# arr_2 = data_2.split(' ')

# for i in arr_2:
#     if (int(i)+2)%2 == 1:
#         print(i)
# for i in data_1:
#     arr_1.append(i)
# print(arr_1)