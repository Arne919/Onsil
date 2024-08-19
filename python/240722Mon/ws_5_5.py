# 아래 함수를 수정하시오.
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


# def even_elements(my_list):
#     arr = []
#     for i in my_list:
#         if int(i) % 2 ==0:
#             arr.append(i)
#     return arr

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)
