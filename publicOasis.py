from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import subprocess
import os
import time
import tkinter as tk
from tkinter import ttk

def login_account(id, pwd):
    # 로그인 정보
    username = id
    password = pwd
    
    # Chrome 드라이버 경로 설정 (자신의 환경에 맞게 설정)
    driver_path = '' # Chrome 드리이버 경로를 적어주세요!
    
    # Chrome 서비스 생성
    chrome_service = Service(executable_path=driver_path)
    
    # 웹 드라이버 초기화
    driver = webdriver.Chrome(service=chrome_service)
    
    # 로그인 페이지로 이동
    driver.get("https://oasis.jbnu.ac.kr/com/login.do")
    
    # 현재 페이지의 쿠키 가져오기
    cookies_before_login = driver.get_cookies()
    
    # 로그인 정보 입력
    id_input = driver.find_element(By.NAME, "userUid")  # 수정: 아이디 입력 필드의 이름이 'userUid'로 변경되었습니다.
    password_input = driver.find_element(By.NAME, "userPwd")  # 수정: 비밀번호 입력 필드의 이름이 'userPwd'로 변경되었습니다.
    id_input.send_keys(username)
    password_input.send_keys(password)
    
    # 로그인 버튼 클릭
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), '로그인')]")  # 수정: 로그인 버튼의 텍스트가 '로그인'으로 변경되었습니다.
    login_button.click()
    
    # 일정 시간 대기 (로그인 후 페이지가 로딩되는데 시간이 필요한 경우에 대비)
    time.sleep(5)
    
    # 시간표 조회 페이지로 이동
    driver.get("https://oasis.jbnu.ac.kr/com/disp/main.do#")
    
    # 메뉴 버튼 클릭
    search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu-btn")))
    search_input.click()
    
    # 원스탑 메뉴 클릭
    onestop_link = driver.find_element(By.XPATH, "//a[text()='원스탑']")
    onestop_link.click()
    
    # '학생수업시간표출력' 링크를 찾아서 클릭
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '학생수업시간표출력')]"))
    )
    link.click()
    
    # change iframe 해서 시간표 조회
    driver.switch_to.frame("view")
    
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/div[7]/div[3]/div/div[5]/div/div/div[9]/div/div[2]/div').click()
    
    # 해당 id를 사용하여 요소 찾기
    element = driver.find_element('id', 'mainframe_VFrameTop_HFrameLeft_VFrameWork_frameWork_form_tabMdi_tabPageMdi1_grdStudLessTimeTblB_head_gridrow_-1_cell_-1_5GridCellTextSimpleContainerElement')
    
    # ActionChains를 초기화하고 해당 요소에서 우클릭 시뮬레이션
    actions = ActionChains(driver)
    actions.context_click(element).perform()
    
    # 'Excel 내보내기' 텍스트를 가진 div 요소 선택
    excel_export_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Excel 내보내기")]'))
    )
    
    # 선택한 요소를 클릭
    excel_export_element.click()
    
    # 종료
    time.sleep(5)
    
    #aaa = input("aaa : ")

temp_name = None
temp_pwd = None

def make_login_window():
    def on_login_button_click():
        global temp_name, temp_pwd
        temp_name = entry_username.get()
        temp_pwd = entry_password.get()
        print("학번:", temp_name)
        root.destroy()
        login_account(temp_name, temp_pwd)
    
    root = tk.Tk()
    root.title("오아시스 로그인 창")
    
    # 아이디 레이블과 입력 필드
    label_username = tk.Label(root, text="학번:")
    label_username.grid(row=0, column=0, sticky=tk.E)
    
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)
    
    # 비밀번호 레이블과 입력 필드
    label_password = tk.Label(root, text="비밀번호:")
    label_password.grid(row=1, column=0, sticky=tk.E)
    
    entry_password = tk.Entry(root, show="*")  # show="*"를 사용하여 입력 내용을 가리기
    entry_password.grid(row=1, column=1)
    
    # 로그인 버튼
    login_button = tk.Button(root, text="로그인", command=on_login_button_click)
    login_button.grid(row=2, column=0, columnspan=2)
    
    # Tkinter 메인 루프 실행
    root.mainloop()
    

def main():
    make_login_window()

if __name__ == "__main__":
    print("직접 실행")
