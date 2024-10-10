'''
Gitlab Create Ver 1.0

실습실 자동 생성 프로그램
셀레니움으로 크롤링 사용
깃랩 아이디(이메일)와 비밀번호를 입력하고 
과목과 차수를 선택하여 실습실 자동 생성 가능
headless모드로 브라우저 창을 띄우지는 않음
webdrivermanager로 크롬드라이버 자동관리



Gitlab Create Ver 1.1

headless block 방지용
    userAgent 추가
    language 추가
chromedriver 완전종료 추가 (feat. 지연쓰 Error)
쉘 정리 추가



Gitlab Create Ver 1.2

Chrome 129버전의 headless 모드 설정 문제로 흰 창이 영역전개 해버림
-> 창이 뜨는 위치를 저 멀리 보내는 것으로 임시 해결



Gitlab Create Ver 1.2.1

핫픽스 ; ARM기반 운영체제에 Chrome driver 설치 시 x86으로 다운받을 가능성 발견.
arm64에 맞게 다운받도록 하는 코드 추가.

Gitlab Create Ver 1.2.2

핫픽스 ; 실습실 생성할 과목 입력 시 범위가 상수로 고정되어 있어 수정.
실습실 차수 목록 범위 추가
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from getpass import getpass
from platform import system
from subprocess import run
import os
os_nlst={'Windows':1, 'Darwin':2, 'Linux':3, 'Ubuntu':4, '':5}

def main():
    os_n=os_nlst[system()]
    if os_n==5:print('운영체제 뭐쓰세요...? 정보가 없는데요....')
    clear = 'cls' if os_n==1 else 'clear'
    
    run(clear, shell=True)
    
    if os_n!=1:
        output=run('uname -m', shell=True, capture_output=True, text=True)
        if 'arm64' in output.stdout or 'aarch64' in output.stdout: os.environ['WDM_ARCH'] = 'arm64'
    
    print('\n동작 중 터미널 화면의 다른 곳을 클릭하면 멈춘 것처럼 보일 수 있습니다...')
    print('작동이 멈춘거 같다면 엔터를 한번 눌러주세요...')
    options = Options()
    options.add_argument("--headless")  # 129버전에선 --headless=old로 흰창 날릴 순 있으나 다른버전에서 문제 생길 수 있으므로 저 멀리 날려버림
    options.add_argument("--window-position=-15400,-15400")  # 창이 뜨는 위치 변경. 4k나 8k에선 보일수도?
    options.add_argument("log-level=3")
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument("lang=ko_KR")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    options.add_experimental_option("useAutomationExtension", False)
    # options.add_argument(userAgent)
    service = Service(ChromeDriverManager().install())
    url = 'https://project.ssafy.com'

    dr = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(dr, 5)
    dr.get(url)
    dr.implicitly_wait(4)

    id_box = dr.find_element(By.ID,"userId")
    password_box = dr.find_element(By.ID,"userPwd")

    while True:
        button = dr.find_elements(By.CLASS_NAME,'btn')
        login_button=button[0]
        
        act = ActionChains(dr)
        dr.implicitly_wait(2)
        
        if len(button)>1:
            print("아이디 또는 비밀번호를 잘못 입력하였습니다. 다시 입력해주세요.")
            modal_button=button[1]
            act.click(modal_button).perform()
            id_box.send_keys(Keys.CONTROL + "a")
            id_box.send_keys(Keys.DELETE)
            password_box.send_keys(Keys.CONTROL + "a")
            password_box.send_keys(Keys.DELETE)
        dr.implicitly_wait(2)
        
        id =   input("\nGitlab ID(email) : ")
        password = getpass("Gitlab PASSWORD : ")
        act.send_keys_to_element(id_box, '{}'.format(id)).send_keys_to_element(password_box,'{}'.format(password)).click(login_button).perform()
        sleep(5)
        dr.implicitly_wait(5)
        if dr.current_url == 'https://project.ssafy.com/login?returnPath=%2Fhome':continue
        break
    act = ActionChains(dr)
    print("\n깃랩 로그인 성공!\n")
    dr.implicitly_wait(4)
    
    run(clear, shell=True)
    
    # 실습실 과목 가져오기
    Xpath="//div[contains(@class,'tit_')]//a"
    elements=dr.find_elements(By.XPATH, Xpath)
    sub=[]
    i=0
    
    print()
    for e in elements:
        i+=1
        sub.append(e)
        print(f'{i}. {e.text}', end='\t')
    print()
    x=0
    while x<1 or x>len(elements):
        try:x=int(input("\n실습실을 생성할 과목을 선택해주세요 : "))
        except:print("정수만 입력해주세요.")
        else:
            if x<1 or x>len(elements):print(f"1과 {len(elements)} 사이 숫자만 입력해주세요.")

    
    # 해당과목의 실습실 목록 불러오기
    print("\n목록을 불러오는 중입니다...\n")
    select=sub[x-1]
    act.click(select).perform()
    sleep(3)
    table=dr.find_element(By.CLASS_NAME, 'con_table')
    lst=table.find_elements(By.TAG_NAME, 'a')
    N=len(lst)
    x=0
    while x<1 or x>N:
        try:x=int(input(f'차수를 입력해주세요. [1 ~ {N}] (ex> 2차. Templates ==> 2) : '))
        except:print("정수를 입력해주세요.")
        else:
            if x<1 or x>N:print("없는 차수입니다. 다시 입력해주세요.")
    
    run(clear, shell=True)
    
    print(f"\n {x}차수 실습실 생성 시도중 입니다...\n")
    select=lst[x-1]
    act.click(select).perform()
    sleep(2)
    page=dr.current_url
    tab=[]
    for i in range(9):  # 실습실 탭 10개 열기
        tab.append(dr.current_window_handle)
        dr.execute_script(f'window.open("{page}");')
        dr.switch_to.window(dr.window_handles[-1])
    tab.append(dr.current_window_handle)
    
    
    # 10개 탭 순회하면서 순서대로 상세보기 버튼 누르기
    Xpath="//a[contains(text(),'상세보기')]"
    for i in range(10):
        dr.switch_to.window(tab[i])
        #elements=dr.find_elements(By.XPATH, Xpath)
        sleep(3)
        try:
            elements=dr.find_elements(By.XPATH, Xpath)
            name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(elements[i]))
            name.click()
        except Exception as e:
            try:
                print(e)
                print("재시도중...")
                elements=dr.find_elements(By.XPATH, Xpath)
                name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(elements[i]))
                name.send_keys(Keys.ENTER)
            except Exception as e:
                try:
                    print(e)
                    print("재시도중......")
                    elements=dr.find_elements(By.XPATH, Xpath)
                    name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(elements[i]))
                    dr.execute_script("arguments[0].click();", name)
                except Exception as e:
                    print(e)
                    print(f"{i+1}번째 실습실 생성 문제 생김....")
                    break
        sleep(3)
        print(f'{i+1}. \"{dr.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, "h3").get_attribute("title")}\" 실습실 생성중....')
        pro=dr.find_element(By.XPATH, "//a[contains(text(),'실습하기')]")
        
        # 각 실습실 실습하기 버튼 누르기
        try:
            pro=dr.find_element(By.XPATH, "//a[contains(text(),'실습하기')]")
            name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(pro))
            name.click()
        except Exception as e:
            try:
                print(e)
                pro=dr.find_element(By.XPATH, "//a[contains(text(),'실습하기')]")
                print("재시도중...")
                name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(pro))
                dr.execute_script("arguments[0].click();", name)
            except Exception as e:
                try:
                    print(e)
                    pro=dr.find_element(By.XPATH, "//a[contains(text(),'실습하기')]")
                    print("재시도중......")
                    name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(pro))
                    name.send_keys(Keys.ENTER)
                except Exception as e:
                    print(e)
                    print(f"{i+1}번째 실습실 생성 문제 생김....")
                    break
        sleep(3)
        dr.switch_to.window(tab[i])
        dr.close()
    else:
        for i in range(10):
            dr.switch_to.window(dr.window_handles[-1])
            dr.close()
        print('\n실습실 생성 성공!')
    
    try:dr.quit()
    except Exception as e:print(f'\n{e}\n 실습실 생성 프로그램을 종료합니다.')  # 오류 쳌
    else:print('\n실습실 생성 프로그램을 종료합니다.')
    sleep(1)
    run(clear, shell=True)