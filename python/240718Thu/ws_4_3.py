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
        dummy_data.append(user_data)

# 변환 데이터 출력
print(dummy_data)
