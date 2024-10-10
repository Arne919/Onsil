'''
Gitlab Manage Ver 1.0
(Gitlab Create Ver 1.0, Gitlab Auto Clone Ver 2.0)

한 파일에서 두개의 기능 실행 가능
실습실 생성 또는 클론 둘 중 하나 실행하면 바로 종료
종료하려면 0 입력 필요



Gitlab Manage Ver 1.1
(Gitlab Create Ver 1.1, Gitlab Auto Clone Ver 2.1)

실습실 생성 후 바로 클론 가능
클론 시 절대경로 사용 수정
실습실 생성 시 드라이버 완전종료하도록 수정



Gitlab Manage Ver 1.2
(Gitlab Create Ver 1.2, Gitlab Auto Clone Ver 2.1)

파일/폴더명 원래대로 변경(실행시 오류 발생확률 줄이기 위함)
실습실 생성시 발생하는 문제 임시 수정

Gitlab Manage Ver 1.2.1
(Gitlab Create Ver 1.2.2, Gitlab Auto Clone Ver 2.1)

핫픽스 - Create ; ARM기반 OS(Aarch64 아키텍쳐 CPU) 고려하도록 추가, 실습생성 과목 입력시 범위가 상수였던 것을 수정
실습실 생성 시 차수 범위 표시
'''

import clone, create

if __name__=='__main__':
    while 1:
        try: c=int(input("\n1. 실습실 생성  2. clone 관리 (종료:0) : "))
        except: print("정수만 입력해주세요.")
        else:
            if c==0: break
            elif c==1: create.main()
            elif c==2: clone.main()
            else:
                print("1, 2 중 하나만 입력해 주세요.")
                continue