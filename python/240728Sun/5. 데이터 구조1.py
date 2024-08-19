# ws_5_a
N = 9
data_1 = '123456789'
arr_1 = []
for i in data_1:
    arr_1.append(i)
print(arr_1)
M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
arr_2 = []
arr_2 = data_2.split(' ')
for i in arr_2:
    if (int(i)+2)%2 == 1:
        print(i)


# ws_5_b
data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
for char in data_1:
    if char.isupper() or char == ' ':
        print(char, end='')
print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
word = '내힘들다'
for i in word:
    arr.append(data_2.find(i))
print(arr)
arr.sort()
print(arr)
for char in arr:
    print(data_2[char], end='')


# ws_5_c
def restructure_word(word, arr):
    for char in word:
        if char.isdecimal():
            for i in range(int(char)):
                arr.pop()
        else:
            if arr in arr:
                arr.remove(char)
    return arr
original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

for char in original_word:
    arr.extend(char)
print(arr)
result = restructure_word(word, arr)
print(result)
text = ''.join(result)
print(text)


# ws_5_1
def reverse_string(char):
    char1 = list(char)
    char1.reverse()
    char2 = ''.join(char1)
    return char2
result = reverse_string('Hello World!')
print(result)


# ws_5_2
def remove_duplicates(list):
    new_1st = []
    for num in list:
        if num not in new_1st:
            new_1st.append(num)
    return new_1st
result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)


# ws_5_3
def sort_tuple(num):
    new_tuple = tuple(sorted(num))
    return new_tuple
result = sort_tuple((5, 2, 8, 1, 3))
print(result)


# ws_5_4
def capitalize_words(char):
    words = char.split()
    text = []
    for word in words:
        cha = word.capitalize()
        text.append(cha)
    return ' '.join(text)

result = capitalize_words("hello world!")
print(result)


# ws_5_5
def even_elements(my_list):
    arr = []
    for i in my_list:
        arr.extend([i])
        if i % 2 != 0:
            arr.pop()
    return arr

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)


# hw_5_2
def count_character(input_string, find_string):
    count = 0
    for char in input_string:
        if char == find_string:
            count += 1
    return count
result = count_character("Hello, world!", "o")
print(result)


# hw_5_4
def find_min_max(list):
    list.sort()
    return list[0], list[len(list)-1]
result = find_min_max([3, 1, 7, 2, 5])
print(result)