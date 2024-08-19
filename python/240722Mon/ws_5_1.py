# 아래 함수를 수정하시오.
def reverse_string(char):
    _char = list(char)
    _char.reverse()
    char2 = ''.join(_char)
    return char2


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

