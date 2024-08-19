#240725test

#hw_8_2
# 아래 함수를 수정하시오.
# def check_number(num):
#     try:
#         num = int(input('숫자를 입력하세요: '))
#         if num > 0:
#             print('양수입니다.')
#         elif num == 0:
#             print('0입니다.')
#         else:
#             print('음수입니다.')
#     except:
#         print('잘못된 입력입니다.')

# check_number(input)


#hw_8_4
# 아래 클래스를 수정하시오. (이름을 입력안해도 출력이 된다<<고쳐야함)
class UserInfo:

    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        try:
            name = str(input('이름을 입력하세요: '))
            age = int(input('나이를 입력하세요: '))
            self.user_data['name'] = name
            self.user_data['age'] = age
            
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')

    def display_user_info(self):
        try:
            self.user_data.get('name')[0] #이름을 입력 안했을 때
            print('사용자 정보:')
            print(f'이름: {self.user_data["name"]}')
            print(f'나이: {self.user_data["age"]}')
        except:
            print('사용자 정보가 입력되지 않았습니다.')

    # def display_user_info(self):
    #     if 'name' in self.user_data and 'age' in self.user_data:
    #         print('사용자 정보:')
    #         print(f'이름: {self.user_data["name"]}')
    #         print(f'나이: {self.user_data["age"]}')
    #     else:
    #         print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()


#hw_8_1
# 아래 클래스를 수정하시오.
# class Animal:
#     num_of_animal = 0

#     def __init__(self):
#         Animal.num_of_animal += 1

# class Dog(Animal):
#     def __init__(self):
#         super().__init__()

# class Cat(Animal):
#     def __init__(self):
#         super().__init__()

# class Pet(Dog, Cat):
#     @classmethod
#     def access_num_of_animal(cls):
#         return f'동물의 수는 {cls.num_of_animal}마리 입니다.'


# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())


#hw_8_2
# 아래 클래스를 수정하시오.
# class Animal:
#     num_of_animal = 0

#     def __init__(self):
#         Animal.num_of_animal += 1

# class Dog(Animal):
#     def __init__(self):
#         super().__init__()

#     def bark(self):
#         return print('멍멍!')

# dog1 = Dog()
# dog1.bark()


#hw_8_3
# 아래 클래스를 수정하시오.
# class Animal:
#     num_of_animal = 0

#     def __init__(self):
#         Animal.num_of_animal += 1

# class Dog(Animal):
#     def __init__(self):
#         super().__init__()

#     def bark(self):
#         print('멍멍!')

# class Cat(Animal):
#     def __init__(self):
#         super().__init__()

#     def meow(self):
#         print('야옹!')

# cat1 = Cat()
# cat1.meow()


#hw_8_4
# 아래 클래스를 수정하시오.
# class Dog():
#     def bark(self):
#         print('멍멍!')

# class Cat():
#     def meow(self):
#         print('야옹!')

# class Pet(Dog, Cat):

#     def __init__(self, sound):
#         super().__init__()
#         self.sound = sound
    
#     def make_sound(self):
#         print(self.sound)

#     def play(self):
#         print('애완동물과 놀기')


# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()


#hw_8_5
# 아래 클래스를 수정하시오.
# class Dog():
#     sound = '멍멍!'

# class Cat():
#     sound = '야옹!'

# class Pet(Dog, Cat):
#     def __str__(self):
#         return f'애완동물은 {self.sound} 소리를 냅니다.'

# pet1 = Pet()
# print(pet1.__str__())


#ws_8_a
# # data = {'name': '홍길동'}
# # if not data['age']:
# #     print(data['age'])
# # else:
# #     print('data에는 age라는 키가 없습니다.')
# #     data['age'] = 30
# #     print(data)
# # 아래에 코드를 작성하시오.
# try:
#     data = {'name': '홍길동'}
#     print(data['age'])
# except KeyError:
#     print('data에는 age라는 키가 없습니다.')
#     data['age'] = 30
#     print(data)


# # arr = ['반갑', '하세요', '안녕']
# # for i in range(4):
# #     print(arr.pop())
# # print(arr)
# # 아래에 코드를 작성하시오.
# try:
#     arr = ['반갑', '하세요', '안녕']
#     for i in range(4):
#         print(arr.pop())
# except IndexError:
#     print(arr)
#     print('더 이상 pop 할 수 없습니다.')


# # word = '3.15'
# # print(int(word))
# # 아래에 코드를 작성하시오.
# try:
#     word = '3.15'
#     print(int(word))
# except ValueError:
#     print('정수로 변환 가능한 값을 입력해 주세요')


#ws_8_b
# class BaseModel:
#     PK = 1
#     TYPE = 'Basic Model'

#     def __init__(self, data_type, title, content, created_at, updated_at):
#         self.PK = BaseModel.PK
#         self.data_type = data_type 
#         self.title = title 
#         self.content = content 
#         self.created_at = created_at 
#         self.updated_at = updated_at
#         BaseModel.PK += 1
    
#     def save(self):
#         print('데이터를 저장합니다.')

# class Novel(BaseModel):
#     def __init__(self, data_type, title, content, created_at, updated_at, author):
#         super().__init__(data_type, title, content, created_at, updated_at)
#         self.author = author
    
# class Other(BaseModel):
#     TYPE = 'OtherModel'

#     def save(self):
#         print('데이터를 다른 장소에 저장합니다.')

# hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
# print('Novel 모델 인스턴스의 PK와 save 메서드')
# print(hong.PK)
# print(chun.PK)
# hong.save()
# chun.save()
# print(hong.author)
# print(chun.author)
# print('---')

# company = Other('회사', '회사명', '회사 설명', 2000, 2023)
# print('Other 모델 인스턴스의 PK와 save 메서드')
# print(company.PK)
# company.save()

# print('---')
# print('모델 별 타입')
# print(Novel.TYPE)
# print(Other.TYPE)


#ws_8_c
# class BaseModel:
#     PK = 1
#     TYPE = 'Basic Model'

#     def __init__(self, data_type, title, content, created_at, updated_at):
#         self.PK = BaseModel.PK
#         self.data_type = data_type 
#         self.title = title 
#         self.content = content 
#         self.created_at = created_at 
#         self.updated_at = updated_at
#         BaseModel.PK += 1
    
#     def save(self):
#         print('데이터를 저장합니다.')

# class Novel(BaseModel):
#     def __init__(self, data_type, title, content, created_at, updated_at, author):
#         super().__init__(data_type, title, content, created_at, updated_at)
#         self.author = author
    
# class Other(BaseModel):
#     TYPE = 'OtherModel'

#     def save(self):
#         print('데이터를 다른 장소에 저장합니다.')

# class ExtendedModel(Novel, Other):

#     def __init__(self, extended_type):
#         self.extended_type = extended_type # 'Extended Type'

#     def display_info(self):
#         print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
#         print(f'PK: {super().PK}, TYPE: {super().TYPE}, Extended Type: {self.extended_type}')

#     def save(self):
#         print('데이터를 확장해서 저장합니다.')

# extended_instance = ExtendedModel('Extended Type') #()
# extended_instance.display_info()
# extended_instance.save()
