from collections import deque

from libs._bridge import init, submit, close

NICKNAME = '기본코드'
game_data = init(NICKNAME)

# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
char_to_dir = {'D': (1, 0), 'R': (0, 1), 'U': (-1, 0), 'L': (0, -1)}
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
    map_data.extend([['' for c in range(map_width)] for r in range(map_height)])
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


def bfs(start, target):
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # D, R, U, L
    queue = deque([(start, [])])  # 현재 위치, 현재까지 도달 경로
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        for direction, (dx, dy) in zip(['D', 'R', 'U', 'L'], dxy):
            nx, ny = x + dx, y + dy

            # map 크기를 초과한 경우
            if nx < 0 or nx >= len(map_data) or ny < 0 or ny >= len(map_data[0]):
                continue
            # 이미 방문한 경로인 경우
            if (nx, ny) in visited:
                continue
            # 도착한 경우
            if (nx, ny) == target:
                return path + [direction]
            # 다음으로 전진할 수 있는 경우
            if map_data[nx][ny] == 'G':
                queue.append(((nx, ny), path + [direction]))
                visited.add((nx, ny))

    return []


def decode(encrypt):
    decrypted = ""
    for char in encrypt:
        decrypted += chr((ord(char) - 65 - 3) % 26 + 65)
    return decrypted


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

    my_position = (-1, -1)
    turret_position = (-1, -1)
    fucility_position = (-1, -1)
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':
                my_position = (i, j)

            if map_data[i][j] == 'X':
                turret_position = (i, j)

            if map_data[i][j] == 'F':
                fucility_position = (i, j)
        # if my_position[0] > 0 and turret_position[0] > 0:
        #     break

    # BFS 알고리즘을 이용하여 도착 지점까지의 이동 경로를 찾음
    turret_path = bfs(my_position, turret_position)

    if turret_path:
        next_position = turret_path[0]
        # 이동 경로에 적 탱크가 있는 경우
        # 시설에 들러서 폭탄 가져와야 함
        if ("E1" in turret_path) or ("E2" in turret_path):
            fucility_path = bfs(my_position, fucility_position)
            if fucility_path:
                next_position = fucility_path[0]
                # 다음 이동 경로에 시설이 있는 경우
                if (my_position[0] + char_to_dir[next_position][0] == fucility_position[0]) \
                        and (my_position[1] + char_to_dir[next_position][1] == fucility_position[1]):
                    # 암호문을 해독해야 함
                    output = f"G {decode(codes)}"
                else:
                    output = f"{next_position} A"

        else:
            # 다음 이동 경로에 포탑이 있는 경우
            if (my_position[0] + char_to_dir[next_position][0] == turret_position[0]) \
                    and (my_position[1] + char_to_dir[next_position][1] == turret_position[1]):
                output = f"{next_position} F M"
            # 다음 이동 경로로 한 칸 전진
            else:
                output = f"{next_position} A"

    # while 문의 끝에는 다음 코드가 필수로 존재하여야 함
    # output에 담긴 값은 submit 함수를 통해 배틀싸피 메인 프로그램에 전달
    game_data = submit(output)

# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()
