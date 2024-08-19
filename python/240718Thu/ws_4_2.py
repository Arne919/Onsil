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
    dummy_data.append(user['name'])

# 변환 데이터 출력
print(dummy_data)
