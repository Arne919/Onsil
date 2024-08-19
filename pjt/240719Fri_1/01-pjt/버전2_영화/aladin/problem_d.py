import json
import os

file_path = 'C:/Users/SSAFY/Desktop/01-pjt/버전2_영화/aladin/data/books/'
file_names = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
print(file_names)

# for file in file_list:
#     if file.count(".") == 1: 
#         name = file.split('.')[0]
#         file_name.append(name)
#     else:
#         for k in range(len(file)-1,0,-1):
#             if file[k]=='.':
#                 file_name.append(file[:k])
#                 break         
# filename

                

def best_book(books):
    # 여기에 코드를 작성합니다.
    pass




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
