# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import matplotlib.pyplot as plt

# # 웹 드라이버 초기화
# driver = webdriver.Chrome()

# # 사이트 열기
# driver.get("https://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_STS_RSN")
# time.sleep(2)

# # 년도와 지역 선택
# driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]').click()
# driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]/option[3]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]').click()
# driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]/option[1]').click()

# # 법규위반 체크 -> 전체해제
# driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
# time.sleep(1)

# # 법규위반 체크박스 리스트로 묶기 
# violations = [
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[1]/input'),
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[2]/input'),
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[3]/input'),
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[4]/input'),
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[5]/input'),
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[6]/input'),
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[7]/input')
# ]

# # 사고유형 리스트로 묶기
# Accident_Type = [
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input'),
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input'),
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input'),
#     driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input')
# ]

# # 체크박스 클릭 및 해제 후 페이지 이동과 검색 버튼 클릭하는 함수
# def handle_violation_checkbox(violation_to_select, violation_to_deselect=None):
#     # 만약 해제할 체크박스가 있다면 해제
#     if violation_to_deselect and violation_to_deselect.is_selected():
#         violation_to_deselect.click()
#         time.sleep(1)

#     # 클릭하려는 체크박스가 선택되지 않았다면 클릭
#     if not violation_to_select.is_selected():
#         violation_to_select.click()
#         time.sleep(1)

#     # 페이지 이동
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]'))
#         ).click()
#     except Exception as e:
#         print(f"페이지 이동 중 오류 발생: {e}")
    
#     # 검색 버튼 클릭 (WebDriverWait 사용)
#     try:
#         search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
#         search_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, search_button_xpath))
#         )
#         search_button.click()
#         time.sleep(10)
#     except Exception as e:
#         print(f"검색 버튼 클릭 중 오류 발생: {e}")

# # 사고 유형 체크박스 클릭 및 해제 함수
# def handle_accident_checkboxes():
#     for i, accident in enumerate(Accident_Type):
#         # 사고 유형 체크박스를 클릭
#         if not accident.is_selected():
#             accident.click()
#             time.sleep(1)

#         # 페이지 이동 후 대기
#         try:
#             # 대기 후 검색 버튼 클릭
#             search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
#             search_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, search_button_xpath))
#             )
#             search_button.click()
#             time.sleep(10)

#             # 결과 출력
#             extract_and_print_data()  # 검색 후 결과를 출력

#         except Exception as e:
#             print(f"사고 유형 {i + 1} 처리 중 오류 발생: {e}")

#         # 사고 유형 해제 (이후 체크박스 클릭 전에 해제)
#         if i < len(Accident_Type) - 1:
#             if accident.is_selected():
#                 accident.click()
#                 # print(f"사고 유형 {i + 1} 해제 완료!")
#                 time.sleep(1)

#     # 4번째 사고유형 해제 후 1번째 사고유형 선택
#     try:
#         if Accident_Type[3].is_selected():
#             Accident_Type[3].click()  # 4번째 사고유형 해제
#             time.sleep(1)

#         if not Accident_Type[0].is_selected():
#             Accident_Type[0].click()  # 1번째 사고유형 선택
#             time.sleep(1)

#     except Exception as e:
#         print(f"4번째 사고유형 해제 및 1번째 사고유형 선택 중 오류 발생: {e}")

# # 사고 발생 건수 추출 및 출력
# def extract_and_print_data():
#     try:
#         # 총 발생건수
#         num = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
#         num2 = driver.find_element(By.XPATH, '//*[@id="map-legend-border"]/li[1]/div/p[4]').text.strip()
#         num3 = driver.find_element(By.XPATH, '//*[@id="map-legend-border"]/li[1]/div/p[3]').text.strip()

#         # "법규위반", "사고내용" 텍스트를 제거
#         num2_cleaned = num2.replace("법규위반", "").strip()
#         num3_cleaned = num3.replace("사고내용", "").strip()
        
#         # 발생 건수 출력
#         print(f"{num3_cleaned}-{num2_cleaned} : {num.text}건")

#     except Exception as e:
#         print(f"데이터 추출 중 오류 발생: {e}")

# # 반복문을 사용하여 체크박스 처리
# for i, violation in enumerate(violations):
#     # 법규 위반 창 클릭 (체크박스 클릭 전에 매번 클릭해야 함)
#     driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
#     time.sleep(1)

#     # 이전 체크박스가 있다면 해제 후 클릭
#     previous_violation = violations[i-1] if i > 0 else None
#     handle_violation_checkbox(violation, previous_violation)

#     # 사고 유형 처리
#     handle_accident_checkboxes()

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 웹 드라이버 초기화
driver = webdriver.Chrome()

# CSV 파일 열기 (쓰기 모드)
csv_file = open('accident_data.csv', mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# CSV 파일의 헤더 작성
csv_writer.writerow(['사고내용', '법규위반', '발생건수'])

# 사이트 열기
driver.get("https://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_STS_RSN")
time.sleep(2)

# 년도와 지역 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]').click()
driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]/option[3]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]').click()
driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]/option[1]').click()

# 법규위반 체크 -> 전체해제
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
time.sleep(1)

# 법규위반 체크박스 리스트로 묶기
violations = [
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[1]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[2]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[3]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[4]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[5]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[6]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[7]/input')
]

# 사고유형 리스트로 묶기
Accident_Type = [
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input'),
    driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input')
]

# 체크박스 클릭 및 해제 후 페이지 이동과 검색 버튼 클릭하는 함수
def handle_violation_checkbox(violation_to_select, violation_to_deselect=None):
    if violation_to_deselect and violation_to_deselect.is_selected():
        violation_to_deselect.click()
        time.sleep(1)

    if not violation_to_select.is_selected():
        violation_to_select.click()
        time.sleep(1)

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]'))
        ).click()
    except Exception as e:
        print(f"페이지 이동 중 오류 발생: {e}")
    
    try:
        search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_button_xpath))
        )
        search_button.click()
        time.sleep(10)
    except Exception as e:
        print(f"검색 버튼 클릭 중 오류 발생: {e}")

# 사고 유형 체크박스 클릭 및 해제 함수
def handle_accident_checkboxes():
    for i, accident in enumerate(Accident_Type):
        if not accident.is_selected():
            accident.click()
            time.sleep(1)

        try:
            search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, search_button_xpath))
            )
            search_button.click()
            time.sleep(10)

            extract_and_print_data()

        except Exception as e:
            print(f"사고 유형 {i + 1} 처리 중 오류 발생: {e}")

        if i < len(Accident_Type) - 1:
            if accident.is_selected():
                accident.click()
                time.sleep(1)

    try:
        if Accident_Type[3].is_selected():
            Accident_Type[3].click()
            time.sleep(1)

        if not Accident_Type[0].is_selected():
            Accident_Type[0].click()
            time.sleep(1)

    except Exception as e:
        print(f"4번째 사고유형 해제 및 1번째 사고유형 선택 중 오류 발생: {e}")

# 사고 발생 건수 추출 및 출력
def extract_and_print_data():
    try:
        num = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
        num2 = driver.find_element(By.XPATH, '//*[@id="map-legend-border"]/li[1]/div/p[4]').text.strip()
        num3 = driver.find_element(By.XPATH, '//*[@id="map-legend-border"]/li[1]/div/p[3]').text.strip()

        num2_cleaned = num2.replace("법규위반", "").strip()
        num3_cleaned = num3.replace("사고내용", "").strip()

        # CSV에 데이터 기록
        csv_writer.writerow([num3_cleaned, num2_cleaned, num.text])

        print(f"{num3_cleaned}-{num2_cleaned} : {num.text}건")

    except Exception as e:
        print(f"데이터 추출 중 오류 발생: {e}")

# 반복문을 사용하여 체크박스 처리
for i, violation in enumerate(violations):
    driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
    time.sleep(1)

    previous_violation = violations[i-1] if i > 0 else None
    handle_violation_checkbox(violation, previous_violation)

    handle_accident_checkboxes()

# CSV 파일 닫기
csv_file.close()
