import sys
sys.stdin = open('sample_input1.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    # 수열의 전체 합이 2N (N 곱하기 2) 이상이 되도록 하고 싶다.
    result = 2 * N
    # 변환 시 얻을 수 있는 값과 실제 값의 차이
    dp = [max(arr[idx] + idx, idx) - arr[idx] for idx in range(N+1)]

    # 내림차순 정렬
    dp.sort(reverse=True)

    # 기본 전체 합
    sum_arr = sum(arr)
    cnt = 0                     # 변환 횟수
    if sum_arr < result:        # 2배가 안되면
        for item in dp:         # 제일 많이 증가 시킬 수 있는 순으로 변경
            sum_arr += item     # 값을 추가하고
            cnt += 1            # 변환 횟수를 증가 시킨 후
            if sum_arr >= result:   # 재검사
                break
    print(f'#{tc} {cnt}')
