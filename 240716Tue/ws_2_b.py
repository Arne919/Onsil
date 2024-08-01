title = '딕셔너리 활용하기'

data = {
    '과목': ' Python', 
    '구분': '실습', 
    '단계': 2, 
    '문제번호': 3251, 
    '이름': None, 
    '일차': 22
    }
print(data)
# 단계 수정
data['단계'] = '2단계'
# 이름 ->title
data['이름'] = title
# 일차 수정
data['일차'] -= 20
# 출력
print(data)
