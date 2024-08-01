############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_days_to_fill_tank(tank_capacity, fill_amount, evaporation_amount):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    day = fill_amount - evaporation_amount #하루 채워지는 양
    days = int(tank_capacity/day) #전체/하루채우는양 = 일수(나머지있을수잇음)
    if tank_capacity%day == 0: #만약 나머지가 0이면 걍 일수.
        return days
    elif (days-1)*day + fill_amount >= tank_capacity: #만약 fill_amount 로 채워진다면 days 출력
        return days
    else:
        return days + 1

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_days_to_fill_tank(100, 20, 5))  # 7
print(calculate_days_to_fill_tank(1000, 100, 10))  # 11
print(calculate_days_to_fill_tank(100, 10, 1))  # 11
#####################################################
