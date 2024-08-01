# ws_2_a
zero_list = [0]
print(zero_list)
many_zero_list = [0]
print(len((many_zero_list)*250000))
numbers = range(1,11)
print(list(numbers))
print(list(numbers[3:]))


# ws_2_b
title = '딕셔너리 활용하기'
data = {
    '과목': 'Python',
    '구분': '실습',
    '단계': 2,
    '문제번호': 3251,
    '이름': None,
    '일차': 22,
}
print(data)
data['단계'] = '2단계'
data['이름'] = title
data['일차'] -= 20
print(data)


# ws_2_c
data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False,
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C',
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
                                     'type': 'multi_select'},
                              '구분': {'id': '%40%3EmR',
                                     'select': {'color': 'purple',
                                                'name': '실습'},
                                     'type': 'select'},
                              '단계': {'id': 'T%7B%7BP',
                                     'select': {'color': 'default',
                                                'name': '3'},
                                     'type': 'select'},
                              '문제번호': {'id': 'uEBt',
                                       'number': 1431,
                                       'type': 'number'},
                              '제목': {'id': 'title',
                                     'title': [{'annotations': {'bold': False,
                                                                'code': False,
                                                                'color': 'default',
                                                                'italic': False,
                                                                'strikethrough': False,
                                                                'underline': False},
                                                'href': None,
                                                'plain_text': '복잡한 자료구조',
                                                'text': {'content': '복잡한 자료구조',
                                                         'link': None},
                                                'type': 'text'}],
                                     'type': 'title'},
                              '일차': {'id': 'nWnH',
                                     'number': '2',
                                     'type': 'number'},
                              '커리큘럼': {'id': 'T%3AR_',
                                       'multi_select': [{'color': 'default',
                                                         'name': 'fundamentals-of-python'}],
                                       'type': 'multi_select'}},
               'public_url': None
            }],
  'type': 'page_or_database'}]
title_content = data[0]['results'][0]['properties']['제목']['title'][0]['text']['content']
day_number = int(data[0]['results'][0]['properties']['일차']['number'])
step_nubmer = str(int(data[0]['results'][0]['properties']['단계']['select']['name']))+'단계'
subject_name = data[0]['results'][0]['properties']['과목']['multi_select'][0]['name']
first_data = {'제목': title_content, '일차': day_number, '단계': step_nubmer,'과목': subject_name}
print(first_data)


# ws_2_1
'''
다음은 이형기 시인의 "낙화"의 한 구절이다.
- 1연
	가야할 때 언제인가를
	분명히 알고 가는 이의
	뒷모습은 얼마나 아름다운가.

나는 이 시를 보며 '나는 내가 가야할 때가 언제일까?' 를 생각해 보았다.
'''
print('다음은 이형기 시인의 "낙화"의 한 구절이다.\n- 1연\n\t가야할 때 언제인가를\n\t분명히 알고 가는 이의\n\t뒷모습은 얼마나 아름다운가.\n\n나는 이 시를 보며 \'나는 내가 가야할 때가 언제일까?\' 를 생각해 보았다.')


# ws_2_2
# 책 한 권당 print문을 한 번씩만 사용한다.
author_1 = '권필'
author_2 = '허균'
book_1 = '주생전'
book_2 = '홍길동전'
print(f'{book_1}의 작가는 {author_1}이고,\n{author_2}은 {book_2}을 집필하였다.')


# ws_2_3
books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
authors = ['작자 미상', '허균', '박지원', '이항복', '임제']
print(f'{authors[1]}: {books[3]}\n{authors[3]} : {books[1]}\n{authors[0]} : {books[2]}\n{authors[2]} : {books[0]}\n{authors[4]} : {books[4]}')


# hw_2_2
book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
print(guide)
print(int(book) * total)
changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
print(changes)
print(int(total - rental))


# hw_2_4
# 중복된 값 제거 후, 작가 목록 출력
authors = [
    '작자 미상',
    '이항복',
    '임제',
    '임제',
    '조성기',
    '조성기',
    '조성기',
    '임제',
    '허균',
    '허균',
    '허균',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '박지원',
    '이항복',
    '남영로',
    '남영로',
    '남영로',
    '이항복',
    '임제',
    '임제',
]
set1 = list(set(authors))
print(set1)