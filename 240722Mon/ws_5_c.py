def restructure_word(word, arr):
    # pass
    for char in word: #word 를 한글자씩
        if char.isdecimal(): #word 속 숫자일때
            for i in range(int(char)): #숫자를 정수로 바꾸고 해당숫자만큼 반복
                arr.pop() #()공백일때 맨뒤부터 없앰
        else: #word 속 숫자아닐때
            if char in arr:
                arr.remove(char)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

for char in original_word:
    arr.extend(char)
print(arr)

result = restructure_word(word,arr)
print(result)

text = ''.join(result)
print(text)
