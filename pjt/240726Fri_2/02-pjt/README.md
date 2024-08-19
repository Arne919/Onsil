버전2_영화_aladin


>>>problem.a.py
----------------------------------------------------------------------------
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
 ----------------------------------------------------------------------------

>>학습한 내용
    api를 활용하여 원하는 데이터를 호출할 수 있으며,
    데이터중 요구하는 정보만을 반환하였습니다.

>>어려웠던 부분
    첫 문제인 만큼 어떻게 접근해야하는지 고민을 하느라 시간을 많이 소모하였습니다.

>>새로 배운 것들 및 느낀 점
    저는 ver2.example_2.aladin.api.py 를 참고하여 함수 get_data를 추가하였습니다.
    주변 친구들 코드를 보고 get_data안의 내용들을 get_author_books에 포함하여,
    굳이 2개의 함수로 나눌 필요가 없음을 깨달았습니다.





>>>problem.b.py
----------------------------------------------------------------------------
import requests
from pprint import pprint

def get_best_review_books():
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

    book_reviews = []
    for book in response['item']:
        if book['customerReviewRank'] >=9:
            book_reviews.append(book)
    return book_reviews


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_best_review_books())
----------------------------------------------------------------------------
>>학습한 내용
    problem.a를 활용하여 제목 호출 부분을 제거하고,
    고객리뷰랭크점수가 9점 이상인것으로 조건문을 걸어서,
    책의 정보를 추가하였습니다.

>>어려웠던 부분
    a문제와 다르게 책 제목만 리스트로 뽑아내는 것이 아니라 
    책정보를 모두 뽑아내는 것이라서 헷갈렸습니다.

>>새로 배운 것들 및 느낀 점
    api를 활용하여 정처리 하는 과정이 꼭 필요하다고 느꼈습니다.
    내가 썼던 모든 편리한 기능은 누군가의 정처리를 거친 것이라고 느꼈습니다.





>>>problem.c.py
----------------------------------------------------------------------------
import requests
from pprint import pprint


def get_bestseller_books():
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
    bestseller_books = []

    # 판매지수를 기준으로 내림차순으로 정렬 후 상위 5개 베스트셀러 책 추출
    sorted_books = sorted(response['item'], key=lambda point: point['salesPoint'], reverse=True)
    top_5_books = sorted_books[:5]
    
    # 제목과 판매지수를 딕셔너리로 저장
    for book in top_5_books:
        bestseller_books.append({'제목': book['title'], '판매지수': book['salesPoint']})
   
    return bestseller_books


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_bestseller_books())
----------------------------------------------------------------------------
>>학습한 내용
    원하는 조건의 책 데이터를 뽑아내어 판매지수를 기준으로 내림차순으로 정렬 후 
    상위 5개 베스트셀러 책을 추출하였습니다.

>>어려웠던 부분
    sorted 함수를 쓸 때 문법이 기억나지 않아 검색을 하였습니다.
    key 값을 입력 할 때 lambda도 써야하는 지 몰랐는데,
    구글링 하다가 알게되었습니다.

>>새로 배운 것들 및 느낀 점
    sorted 문법을 다시금 복기하였고,
    lambda 문법을 쓰며 이럴 때 이용한다는 것을 알게 되었습니다.



>>>problem.d.py
----------------------------------------------------------------------------
import requests
from pprint import pprint


def get_author_other_books(title):
    # 여기에 코드를 작성합니다.
    url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    try:
        params = {
            'ttbkey': 'ttbghgghg961120001',
            'Query': title,
            'QueryType': 'Title',
            'MaxResults': 20,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': 20131101,
        }
        response = requests.get(url, params=params).json()
        author = response['item'][0]['author'].index(' (지은이)')
    except IndexError:
        return None
    main_author = response['item'][0]['author'][:author]
  

    params = {
        'ttbkey': 'ttbghgghg961120001',
        'Query': main_author,
        'QueryType': 'Author',
        'MaxResults': 5,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': 20131101,
    }

    response = requests.get(url, params=params).json()
    other_books = []
    for books in response['item']:
        other_books.append(books['title'])
    result = {f'"{title}"의 저자 "{main_author}"의 다른 도서 목록':other_books}
    return result


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_other_books('베니스의 상인'), width=120)
    pprint(get_author_other_books('죄와 벌'), width=120)
    pprint(get_author_other_books('*'), width=120)
----------------------------------------------------------------------------
>>학습한 내용
    title로 url을 검색하여 뽑은 책 한 권의 작가의 다른 책 5권을 리스트로 출력하였습니다.

>>어려웠던 부분
    작가가 지은이, 옮긴이, 그림 등등 이름만 나오는 것이 아닌 책을 만드는데에 힘쓴 사람이 모두 적혀 있어서 작가로 재검색하는데 어려움을 겪었습니다.

>>새로 배운 것들 및 느낀점
    작가 중 공통적 부분인 (지은이) 앞을 인덱스로 이후는 슬라이스 하여 작가를 재지정하여 다른 책 검색을 진행하였습니다.
    그리고 검색하려는 책에 오류가 있을경우 None으로 출력해야 하는 것은 본래 if문을 쓰려고 했는데 제가 코드를 잘못 짰는지 오류가 떠서 try 예외처리로 진행하였습니다.



>>>problem.e.py
----------------------------------------------------------------------------
import requests
from pprint import pprint


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
----------------------------------------------------------------------------
>>학습한 내용
    문제이해는 하였지만 이것을 코딩으로 기입하는데에 어려움을 겪고있습니다.
    해당 문제는 다음주 과목평가/월말평가를 친 이후에 작성해보도록 하겠습니다.