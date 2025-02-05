from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# ChromeDriver 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 창 없이 실행
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# ChromeDriver 자동 설치 및 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 사이트 접속
url = "https://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_AGS_TMM#"
driver.get(url)

# 페이지가 로드될 때까지 대기
time.sleep(3)

# 사고분석 탭으로 이동
tab = driver.find_element(By.XPATH, '//*[@id="menuPartSearch"]')
tab.click()

time.sleep(3)

# -----------------------------------------------------------------
# '사고년도' 설정 함수
def set_year(start, end):
    year_start = driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]')
    year_start.click()
    num = driver.find_element(By.XPATH, start)
    num.click()
    year_end = driver.find_element(By.XPATH, '//*[@id="ptsRafYearEnd"]')
    year_end.click()
    num = driver.find_element(By.XPATH, end)
    num.click()
    print("사고년도 설정 완료")

# '시도', '시군구' 선택
def set_city(sido, sigungu):
    select = driver.find_element(By.XPATH, '//*[@id="ptsRafSido"]')
    select.click()
    sel_sido = driver.find_element(By.XPATH, sido)
    sel_sido.click()
    select = driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]')
    select.click()
    sel_sigungu = driver.find_element(By.XPATH, sigungu)
    sel_sigungu.click()

# ----------------------------------------------------------------
# '조건설정' 클릭 함수
def filter_click(xpath):
    death_button = driver.find_element(By.XPATH, xpath)  
    death_button.click()
    print("조건설정 완료")
    time.sleep(1)

# ----------------------------------------------------------------
# 모든 필터 '전체해제' 선택 함수
def deSelect(category, desel):
    condition_btn = driver.find_element(By.XPATH, category)
    condition_btn.click()
    deselect = driver.find_element(By.XPATH, desel)
    deselect.click()
    print("전체해제 클릭")

def all_deSelect():
    ## '사고유형' 필터
    deSelect('//*[@id="ptsRaf-ACDNT_CODE"]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[1]/div/p/a[2]')
    ## '법규위반' 필터
    deSelect('//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]')
    ## '가해차종' 필터
    deSelect('//*[@id="ptsRaf-WRNGDO_VHCLE_ASORT_CODE"]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[3]/div/p/a[2]')
    ## '월별' 필터
    deSelect('//*[@id="ptsRaf-ACDNT_DD_DC"]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[4]/div/p/a[2]')
    ## '도로종류' 필터
    deSelect('//*[@id="ptsRaf-ROAD_TYPE"]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[5]/div/p/a[2]')
    ## '노면상태' 필터
    deSelect('//*[@id="ptsRaf-RDSE_STTUS_CODE"]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[6]/div/p/a[2]')
    ## '기상상태' 필터
    deSelect('//*[@id="ptsRaf-WETHER_STTUS_CODE"]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[7]/div/p/a[2]')
    ## '도로형태' 필터
    deSelect('//*[@id="ptsRaf-ROAD_STLE_CODE"]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[8]/div/p/a[2]')
    print("모두 전체해제 완료")

# ----------------------------------------------------------------
# '사고 유형'별 선택 함수
def condition_click(xpath):
    ## '사고유형' 버튼 클릭
    category_btn = driver.find_element(By.XPATH, '//*[@id="ptsRaf-ACDNT_CODE"]')
    category_btn.click()
    ## 세부유형 체크
    specific_check = driver.find_element(By.XPATH, xpath)
    specific_check.click()
    ## 검색
    search = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p/a')
    search.click()
    print("검색 완료")

# ----------------------------------------------------------------
# 페이지 소스 가져와서 데이터 추출 및 csv로 저장
def get_accident_data():
    # 페이지 소스 가져오기
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 사고 데이터 추출
    accident_data = []
    accidents = soup.find_all("div", class_="accident-item")  # 사고 목록이 담긴 요소 찾기 (CSS 클래스 확인 필요)

    for accident in accidents:
        print(accident)
        # location = accident.find("span", class_="location").text.strip()
        # date = accident.find("span", class_="date").text.strip()
        # num_deaths = accident.find("span", class_="deaths").text.strip()

        # accident_data.append([location, date, num_deaths])

    # # 데이터프레임으로 변환
    # df = pd.DataFrame(accident_data, columns=["위치", "날짜", "사망자 수"])

    # # CSV 파일로 저장
    # df.to_csv("death_accidents_car_vs_car.csv", index=False, encoding="utf-8-sig")

    # print("데이터 저장 완료!")


# ----------------------------------------------------------------
# 1. 연도 설정 
### 2021년 ~ 2023년
set_year('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/fieldset/div[1]/p/select[1]/option[3]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/fieldset/div[1]/p/select[2]/option[1]')
time.sleep(3)

# 2. 시도, 시군구 설정
### 서울특별시, 전체
set_city('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/fieldset/div[2]/select/option[1]', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/fieldset/div[3]/select/option[1]')
time.sleep(3)

# 3. 조건설정
# filter_click('//*[@id="ptsRafCh1AccidentContent"]/li[1]/input') # 사망사고는 기본 체크
# time.sleep(3)

# 4. 필터 전체 해제
all_deSelect()
time.sleep(3)

# 5. 세부 필터 설정 및 검색
condition_click('//*[@id="ptsRafCh2AccidentType"]/li[1]/ul/li[1]/span/input') # 횡단중
time.sleep(3)

# 6. 페이지 소스 가져와서 데이터 추출 및 csv로 저장
get_accident_data()
time.sleep(3)

# 7. 브라우저 종료
driver.quit()
