# 아래 클래스를 수정하시오.(이름을 입력안해도 출력이 된다<<고쳐야함)
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
