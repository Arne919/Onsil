import json
from pprint import pprint


def books_info(books, categories):
    # 여기에 코드를 작성합니다.
    all_list = []
    # new_list = []
    for book in books: # books의 인덱스(반복)
        new_list = []  # 재할당
        for id in book['categoryId']: # [151128, 50919]의 인덱스 (반복)
            for cat_id in categories: # 카테고리의 딕셔너리 인덱스 (반복)
                if id == cat_id['id']: # 첫번째 for 인덱스와 카테고리 딕셔너리 인덱스 비교
                    new_list.append(cat_id['name']) # 원하는 값을 새 리스트에다가 추가한다.
        data = {
        'author': book['author'],
        'categoryName': new_list, # 요소가 아니라 리스트라서
        'cover': book['cover'],
        'description': book['description'],
        'id': book['id'],
        'priceSales': book['priceSales'],
        'title': book['title']
        }
        all_list.append(data) # book 반복해서 쌓음

    return all_list

print(books_info)




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
