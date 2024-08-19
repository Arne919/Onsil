import requests
from pprint import pprint

# aladin api 를 활용하는 예시



# def get_author_other_books(title):
#     # 여기에 코드를 작성합니다.
#     try:
#         params = {
#             'ttbkey': 'ttbghgghg961120001',
#             'Query': title,
#             'QueryType': 'Title',
#             'MaxResults': 6,
#             'start': 1,
#             'SearchTarget': 'Book',
#             'output': 'js',
#             'Version': 20131101,
#         }
#         response = requests.get(url, params=params).json()
#         author = response['item'][0]['author'].index(' (지은이)')
#     except IndexError:
#         return None
#     main_author = response['item'][0]['author'][:author]
  

#     params = {
#         'ttbkey': 'ttbghgghg961120001',
#         'Query': main_author,
#         'QueryType': 'Author',
#         'MaxResults': 6,
#         'start': 1,
#         'SearchTarget': 'Book',
#         'output': 'js',
#         'Version': 20131101,
#     }

#     response = requests.get(url, params=params).json()
#     other_books = []
#     for books in response['item']:
#         other_books.append(books['title'])
#     result = {f'"{title}"의 저자 "{main_author}"의 다른 도서 목록':other_books}
#     return result


def get_users_books(title):
    # 여기에 코드를 작성합니다.
    url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    try:
        params = {
            'ttbkey': 'ttbghgghg961120001',
            'Query': title,
            'QueryType': 'Title',
            'MaxResults': 1,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': 20131101,
        }
        response = requests.get(url, params=params).json()
    except IndexError:
        return None
    
    url = 'http://www.aladin.co.kr/ttb/api/ItemOffStoreList.aspx'
    # params = {
    #     'ttbkey': 'ttbghgghg961120001',
    #     'Query': main_author,
    #     'QueryType': 'Author',
    #     'MaxResults': 5,
    #     'start': 1,
    #     'SearchTarget': 'Book',
    #     'output': 'js',
    #     'Version': 20131101,
    # }

    # response = requests.get(url, params=params).json()
    # other_books = []
    # for books in response['item']:
    #     other_books.append(books['title'])
    # result = {f'"{title}"의 저자 "{main_author}"의 다른 도서 목록':other_books}
    # return result
    return response

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_users_books('죄와 벌'))
    # pprint(get_users_books('로미오와 줄리엣'))
    # pprint(get_users_books('*'))
