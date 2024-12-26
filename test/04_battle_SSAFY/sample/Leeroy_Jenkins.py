from libs._bridge import init, submit, close
from collections import deque
import pygame
import random

pygame.mixer.init()
pygame.mixer.music.load('assets/Leeroy_Jenkins.mp3')
pygame.mixer.music.play()

NICKNAME = 'Leeroy'
game_data = init(NICKNAME)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


DS = 0

def search(x, y):
    q = deque([(x, y, [])])
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    while q:
        x, y, arr = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if map_data[nx][ny] == 'G':
                    visited[nx][ny] = 1
                    q.append((nx, ny, arr + [int_to_char[i] + ' A']))
                elif map_data[nx][ny] == 'X':
                        arr.append(int_to_char[i] + ' F')
                        return arr
    return arr


def decode(ciphertext):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ciphertext.upper()
    result = []
    # Try all possible shifts and print the result
    for shift in range(1, 26):
        decrypted_text = ''
        for char in ciphertext:
            if char in alphabet:
                index = alphabet.find(char)
                # Shift the letter backwards to decrypt
                new_index = (index - shift) % 26
                decrypted_text += alphabet[new_index]
            else:
                decrypted_text += char  # Leave non-alphabet characters unchanged
        
        # Display the shift and corresponding decrypted text
        result.append(decrypted_text)
    return result[16]

# 입력 데이터 분류
int_to_char = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}
char_to_int = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
allies = {}  # 아군 정보. 예) allies['A'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])  # 맵의 세로 크기
    map_width = int(header[1])  # 맵의 가로 크기
    num_of_allies = int(header[2])  # 아군의 수
    num_of_enemies = int(header[3])  # 적군의 수
    num_of_codes = int(header[4])  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 자기 차례가 되어 받은 게임정보를 파싱
    print(f'----입력데이터----\n{game_data}\n----------------')
    parse_data(game_data)

    # 파싱한 데이터를 화면에 출력하여 확인
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(allies)})')
    for k, v in allies.items():
        if k == 'A':
            print(f'A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 대전차 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(allies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'H (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])


    # 탱크의 동작을 결정하기 위한 알고리즘을 구현하고 원하는 커맨드를 output 변수에 담기
    # 코드 구현 예시: '아래쪽으로 전진'하되, 아래쪽이 지나갈 수 있는 길이 아니라면 '오른쪽로 전진'하라

    output = 'S'  # 알고리즘 결괏값이 없을 경우를 대비하여 초기값을 S로 설정
    N, M = int(game_data.split()[0]), game_data.split()[1]
    my_position = [-1, -1]
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':
                my_position[0] = i
                my_position[1] = j
        
    result = search(my_position[0], my_position[1])
    if len(result) and 'F' in result[0]:
        no = random.choice(range(1, 4))
        file_name = f'assets/fire{no}.mp3'
    
    try:
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except:
        pass
    game_data = submit(result[0])
    # command = input()
    # game_data = submit(command)


# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()
