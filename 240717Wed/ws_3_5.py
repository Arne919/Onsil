number_of_book = 100 #대여 가능한 책의 수
def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')
    return number_of_book


number_of_people = 0 #회원 수
def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]



def create_user(name, age):
    increase_user()
    print(f'{name}님 환영합니다!')
    return {'name' : name, 'age' : age}


many_user = list(map(create_user, name, age))
# [{'name': '김시습', 'age': 20}, {'name': '허균', 'age': 16}, {'name': '남영로', 'age': 52}, {'name': '임제', 'age': 36}, {'name': '박지원', 'age': 60}]

def rental_book(info):
    decrease_book(info['age']//10)
    print(f"{info['name']}님이 {info['age']//10}권의 책을 대여하였습니다.")



info = list(map(lambda user : {'name':user['name'], 'age':user['age']}, many_user))
# [{'name': '김시습', 'age': 20}, {'name': '허균', 'age': 16}, {'name': '남영로', 'age': 52}, {'name': '임제', 'age': 36}, {'name': '박지원', 'age': 60}]
list(map(rental_book, info))


# list(map(rental_book, map(lambda user : {'name':user['name'], 'age':user['age']}, many_user)))




