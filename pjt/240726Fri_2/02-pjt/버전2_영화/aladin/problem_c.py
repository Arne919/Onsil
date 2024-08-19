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
