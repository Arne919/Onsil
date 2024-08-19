import requests
from pprint import pprint

def get_author_books():
    # 여기에 코드를 작성합니다.
    url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'ttbkey': 'ttbghgghg961120001',
        'Query': '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': 20131101,

    }
    response = requests.get(url, params=params).json()
    book_titles= []
    for book in response['item']:
        book_titles.append(book['title'])
    return book_titles

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_books())




