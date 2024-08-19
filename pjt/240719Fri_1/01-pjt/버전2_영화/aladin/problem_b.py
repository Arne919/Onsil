import json
from pprint import pprint


# B. 제공되는 도서 데이터의 주요내용 수정
def book_info(book, categories):
    # 여기에 코드를 작성합니다.
    new_list = []
    for id in book['categoryId']: # [151128, 50919]의 인덱스 (반복)
        for cat_id in categories: # 카테고리의 딕셔너리 인덱스 (반복)
            if id == cat_id['id']: # 첫번째 for 인덱스와 카테고리 딕셔너리 인덱스 비교
                new_list.append(cat_id['name']) # 비교해서 뽑은것을 새 리스트에다가 추가한다.

    data = {
    'author': book['author'],
    'categoryName': new_list, # 요소가 아니라 리스트라서
    'cover': book['cover'],
    'description': book['description'],
    'id': book['id'],
    'priceSales': book['priceSales'],
    'title': book['title']
    }        
    return data


print(book_info)



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
