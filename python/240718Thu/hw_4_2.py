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

# print([book for book in rental_list if book not in list_of_book])

flag = False

for book in rental_list: #대여예정책 반복
    if book not in list_of_book: #대여예정책이 보유중이지 않으면
        print(f'{book}은/는 보유하고 있지 않습니다.')
        flag = True
        break
if not flag:
    print(f'모든 도서가 대여 가능한 상태입니다.')
    





