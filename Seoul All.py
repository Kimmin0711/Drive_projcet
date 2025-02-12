import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 웹 드라이버 초기화
driver = webdriver.Chrome()

# CSV 파일 열기 (쓰기 모드)
csv_file = open('Seoul All.csv', mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# CSV 파일에 헤더 작성 (첫 번째 행에 컬럼 이름 작성)
csv_writer.writerow(['Accident Type', 'Number of Accidents'])

# 사이트 열기
driver.get("https://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_STS_RSN")
time.sleep(2)

# 년도와 지역 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]').click()
driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]/option[3]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]').click()
driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]/option[1]').click()

Accident_Type = [
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input')
]

# 사고 유형 체크박스 클릭 및 해제 함수
def handle_accident_checkboxes():
    for i, accident in enumerate(Accident_Type):
        if not accident.is_selected():
            accident.click()
            time.sleep(60)

        try:
            search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
            search_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, search_button_xpath))
            )
            search_button.click()
            time.sleep(60)

            extract_and_save_data(i + 1)  # 사고 유형에 맞춰서 데이터를 저장

        except Exception as e:
            print(f"사고 유형 {i + 1} 처리 중 오류 발생: {e}")

        if i < len(Accident_Type) - 1:
            if accident.is_selected():
                accident.click()
                time.sleep(60)

    try:
        if Accident_Type[3].is_selected():
            Accident_Type[3].click()
            time.sleep(60)

        if not Accident_Type[0].is_selected():
            Accident_Type[0].click()
            time.sleep(60)

    except Exception as e:
        print(f"4번째 사고유형 해제 및 1번째 사고유형 선택 중 오류 발생: {e}")

def extract_and_save_data(accident_type_number):
    try:
        num = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
        num1 = driver.find_element(By.XPATH, '//*[@id="map-legend-border"]/li[1]/div/p[3]').text.strip()
        
        num1_cleaned = num1.replace("사고내용", "").strip()
        print(f"{num1_cleaned} : {num.text}건")

        # CSV 파일에 사고 유형과 사고 건수 저장
        csv_writer.writerow([num1_cleaned, num.text])

    except Exception as e:
        print(f"데이터 추출 중 오류 발생: {e}")

handle_accident_checkboxes()
extract_and_save_data()

# CSV 파일 닫기
csv_file.close()
