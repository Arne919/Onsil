# ws_4_a
# 모듈~


# ws_4_b
food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

for food in food_list:
    if food['이름'] == '토마토':
        food['종류'] = '과일'
    elif food['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(f"{food['이름']} 은/는 {food['종류']}(이)다.")
while True:
    print(f'{food_list}')
    break


# ws_4_c
matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
matrix_len = 0
for each in matrix:
    matrix_len += 1
print(matrix_len)
for number in matrix:
    temporary_len = 0
    for each in number:
        temporary_len += 1
    if temporary_len <= 4:
        print(f'{number}리스트는 {temporary_len}개만큼 요소를 가지고 있습니다.')
for x, each in enumerate(matrix):
    for y in range(0, len(each)):
        print(f'matrix의 {x},{y}번째 요소의 값은 {matrix[x][y]}입니다.')
        

# ws_4_1
import requests
from pprint import pprint as print
API_URL = 'https://jsonplaceholder.typicode.com/users/1'
response = requests.get(API_URL)
parsed_data = response.json()
print(response)
print(parsed_data)
print(type(parsed_data))
print([parsed_data['name']])
print([parsed_data['username']])
print([parsed_data['company']['name']])


# ws_4_2
import requests
from pprint import pprint as print
API_URL = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(API_URL)
parsed_data = response.json()
dummy_data = []
for user in parsed_data[:10]:
    dummy_data.append(user['name'])
print(dummy_data)


# ws_4_3
import requests
from pprint import pprint as print
API_URL = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(API_URL)
parsed_data = response.json()
dummy_data = []
for user in parsed_data[:10]:
    lat = float(user['address']['geo']['lat'])
    lng = float(user['address']['geo']['lng'])
    if -80 < lat < 80 and -80 < lng < 80:
        user_data = {
            'company': user['company']['name'],
            'lat': lat,
            'lng': lng,
            'name': user['name']
        }
        dummy_data.append(user_data)
print(dummy_data)


# hw_4_2
#보유 중인 도서 리스트
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]
#대여 예정 도서 리스트
rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]
flag = False
for book in rental_list:
    if book not in list_of_book:
        print(f'{book}은/는 보유하고 있지 않습니다.')
        flag = True
        break
if not flag:
    print(f'모든 도서가 대여 가능한 상태입니다.')


# hw_4_4
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]
rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]
missing_list = [book for book in rental_book if book not in list_of_book]
flag = False
for book in rental_book:
    if book not in list_of_book:
        print(f'{book}을/를 보충하여야 합니다.')
        flag = True
        continue
if not flag:
    print(f'모든 도서가 대여 가능한 상태입니다.')