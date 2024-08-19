import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'

# API 요청
response = requests.get(API_URL)

# JSON -> dict 데이터 변환
parsed_data = response.json()

# 이름을 저장할 리스트
dummy_data = []

# 10명의 유저이름 dummy_data 리스트에 추가
for user in parsed_data[:10]:
    lat = float(user['address']['geo']['lat'])
    lng = float(user['address']['geo']['lng'])
    if -80 < lat < 80 and -80 < lng < 80: # &는 비트 연산자이기때문에 논리연산에 사용할 수 없음
        user_data = {
            'company': user['company']['name'],
            'lat': lat,
            'lng': lng,
            'name': user['name'],    
        }
        dummy_data.append(user_data) #dummy_data 리스트에 사용자 정보 추가

# 블랙 리스트
black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]



def create_user(dummy_data):
    censored_user_list = {}
    for user_data in dummy_data:
        company_name = user_data['company'] # 사용자 정보에서 회사명 추출
        user_name = user_data['name'] # 사용자 정보에서 사용자명 추출

        if censorship(company_name, user_name): #censorship 함수를 사용하여 회사명 검사
            if company_name not in censored_user_list:
                censored_user_list[company_name] = [] # 새로운 회사명을 key로 하여 리스트 생성
            censored_user_list[company_name].append(user_name) # 해당 회사명의 리스트에 사용자명 추가

    return censored_user_list # 완성된 censored_user_list 반환
    


def censorship(company_name, user_name):
    if company_name in black_list: # 회사명이 black_list에 있는지 확인
        print(f"{company_name} 소속의 {user_name}은/는 등록할 수 없습니다.")
        return False
    else:
        print("이상 없습니다.")
        return True

# 사용자 정보를 순회하며 censored_user_list 생성
censored_user_list = create_user(dummy_data)

# 결과 출력
print(censored_user_list)
