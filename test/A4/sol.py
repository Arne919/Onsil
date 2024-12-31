import sys
sys.stdin = open('sample_input2.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    q = deque([[x, y, 0]])
    while q:
        x, y, acc = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            add_acc = 0
            if 0 <= nx < N and 0 <= ny < N:
                height = data[nx][ny] - data[x][y]  # 다음 탐색지 높이 차
                if height == 0:     # 같음
                    add_acc += 1        # 연료 1 추가
                elif height > 0:    # 더 높음
                    add_acc += height * 2   # 높이차 2배
                # 더 낮으면 연료 소모량 증가 없음

                if visited[nx][ny] >= acc + add_acc:  # 해당 방문지 누적 연료값이 지금보다 높으면
                    visited[nx][ny] = acc + add_acc   # 갱신 후 이동
                    q.append((nx, ny, acc + add_acc))

    return acc
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = N**10
    visited = [[result for _ in range(N)] for _ in range(N)]

    search(0, 0)

    print(f'#{tc} {visited[N-1][N-1]}')

