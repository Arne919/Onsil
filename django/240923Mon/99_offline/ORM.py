# g1 instance 생성
g1 = Garage()
# g1 인스턴스의 변수 location에 값 설정
g1.location = '서울'

print(g1.location)
# 서울

# g2 instance 생성
g2 = Garage()
# g2는 아직 location 정보가 없다.
print(g2.location)
# 출력결과 없음.

# g1에 다른 정보 추가
g1.capacity = 30
g1.is_parking_avaliable = False
g1.opening_time = '08:00'
g1.closing_time = '22:00'
# save 메서드를 호출하기 전까지는 아직 DB에 g1 데이터가 생성되기 전이다.
g1.save()   # db에 반영


# g2도 정보 추가
g1.is_parking_avaliable = False
g2.capacity = 20
g2.is_parking_avaliable = True
g2.opening_time = '08:00'
# closing_time 누락된 채로 저장 시도
g2.save()

# IntegrityError >> 무결성 에러
# closing_time 필드에 데이터가 없어 저장 할 수 없음.

g2.closing_time = '23:00'   # 종료 시간 지정후
g2.save()                   # 데이터 삽입

garages = Garage.objects.all()  # 모든 데이터 조회

# garages
# Out[28]: <QuerySet [<Garage: Garage object (1)>, <Garage: Garage object (2)>]>

for garage in garages:
    print(garage.location)
    
# 서울
# 부산

# get QuerySet API가 가진 주요한 특징!
# 반드시 1개를 찾을 수 있어야 한다.
    # 0개도 안되고, 2개 이상도 안된다.
    # get(condition) -> 이 조건이 반드시 1개를 찾을 수 있는지를 보장하는 조건이 좋다.
    # 그러면 보통... get방식으로 조회 할떄는 뭘 기준으로 하느냐? PK 
    # id == PK (지금 우리가 설계한 모양대로는 두개는 똑같은거다.)
dokdo = Garage.objects.get(location='독도')
print(dokdo.location)
# '독도'

# lookup
# fucn(kwarg=30) : 키워드 인자 넘겨서 호출하는 방식
    # __lte 이게 뭐길래???? -> 이건... 그냥 그런걸로합시다.
    # django 만든사람이 그렇게 동작하도록 만든거에요.
# filter는 0개면 비어있는 querySet, 여러개면 여러개 잘 담은 값
garges = Garage.objects.filter(capacity__lte = 30)

# filter가 항상 get보다 우월하다.
# 웹 서비스를 구축할때, 상대방이 찾고자 하는 데이터가 없는경우 
    # 1. 없으면, 없다고 알려주고 종료.
    # 2. 없으면, 잘못 찾아왔다고 알려주고 종료.