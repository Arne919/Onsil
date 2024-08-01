# 아래 함수를 수정하시오.
def capitalize_words(char):
    words = char.split()
    text = []
    for word in words:
        cha = word.capitalize()
        text.append(cha)
    return ' '.join(text)
    
result = capitalize_words("hello, world!")
print(result) # Hello, World!
