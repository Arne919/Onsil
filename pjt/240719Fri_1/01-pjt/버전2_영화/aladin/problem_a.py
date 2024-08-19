import json
from pprint import pprint

# A. 제공되는 도서 데이터의 주요내용 수집
def book_info(book):
    # 여기에 코드를 작성합니다.
    data = {
        'author': book['author'],
        'categoryId': book['categoryId'],
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

    pprint(book_info(book))
