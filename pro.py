import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import matplotlib.pyplot as plt

# 웹 드라이버 초기화
driver = webdriver.Chrome()

# 사이트 열기
driver.get("https://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_STS_RSN")
time.sleep(2)

# 년도와 지역 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]').click()
driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]/option[3]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]').click()
driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]/option[1]').click()

# 메뉴 선택
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
time.sleep(1)

# 1번 체크박스 클릭 후 결과 출력
checkbox_1 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[1]/input')
if not checkbox_1.is_selected():
    checkbox_1.click()  # 체크박스 1번 클릭
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num1 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-중앙선침범 : {num1.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['사망사고-중앙선침범', num1.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num2 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"중상사고-중앙선침범 : {num2.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['중상사고-중앙선침범', num2.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num3 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"경상사고-중앙선침범 : {num3.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['경상사고-중앙선침범', num3.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num4 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"부상신고-중앙선침범 : {num4.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['부상신고-중앙선침범', num4.text])

# 메뉴 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
time.sleep(1)

# 2번 체크박스 클릭
checkbox_2 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[2]/input')
checkbox_2.click()  # 2번 체크박스 클릭
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num5 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-신호위반 : {num5.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['사망사고-신호위반', num5.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num6 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"중상사고-신호위반 : {num6.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['중상사고-신호위반', num6.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num7 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"경상사고-신호위반 : {num7.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['경상사고-신호위반', num7.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num8 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"부상신고-신호위반 : {num8.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['부상신고-신호위반', num8.text])

# 메뉴 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
time.sleep(1)

# 3번 체크박스 클릭
checkbox_3 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[3]/input')
checkbox_3.click()  # 3번 체크박스 클릭
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num9 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-안전거리미확보 : {num9.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['사망사고-안전거리미확보', num9.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num10 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"중상사고-안전거리미확보 : {num10.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['중상사고-안전거리미확보', num10.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num11 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"경상사고-안전거리미확보 : {num11.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['경상사고-안전거리미확보', num11.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num12 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"부상신고-안전거리미확보 : {num12.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['부상신고-안전거리미확보', num12.text])

# 메뉴 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
time.sleep(1)

# 4번 체크박스 클릭
checkbox_4 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[4]/input')
checkbox_4.click()  # 4번 체크박스 클릭
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num13 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-안전운전불이행 : {num13.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['사망사고-안전운전불이행', num13.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num14 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"중상사고-안전운전불이행 : {num14.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['중상사고-안전운전불이행', num14.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num15 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"경상사고-안전운전불이행 : {num15.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['경상사고-안전운전불이행', num15.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num16 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"부상신고-안전운전불이행 : {num16.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['부상신고-안전운전불이행', num16.text])

# 메뉴 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
time.sleep(1)

# 5번 체크박스 클릭
checkbox_5 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[5]/input')
checkbox_5.click()  # 5번 체크박스 클릭
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num17 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-교차로운행방법위반 : {num17.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['사망사고-교차로운행방법위반', num17.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num18 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"중상사고-교차로운행방법위반 : {num18.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['중상사고-교차로운행방법위반', num18.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num19 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"경상사고-교차로운행방법위반 : {num19.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['경상사고-교차로운행방법위반', num19.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num20 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"부상신고-교차로운행방법위반 : {num20.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['부상신고-교차로운행방법위반', num20.text])

# 메뉴 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
time.sleep(1)

# 6번 체크박스 클릭
checkbox_6 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[6]/input')
checkbox_6.click()  # 6번 체크박스 클릭
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num21 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-보행자의무보호위반 : {num21.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['사망사고-보행자의무보호위반', num21.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num22 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"중상사고-보행자의무보호위반 : {num22.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['중상사고-보행자의무보호위반', num22.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num23 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"경상사고-보행자의무보호위반 : {num23.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['경상사고-보행자의무보호위반', num23.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num24 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"부상신고-보행자의무보호위반 : {num24.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['부상신고-보행자의무보호위반', num24.text])

# 메뉴 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
time.sleep(1)

# 7번 체크박스 클릭
checkbox_7 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[7]/input')
checkbox_7.click()  # 6번 체크박스 클릭
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num25 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-기타 : {num25.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['사망사고-기타', num25.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num26 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"중상사고-기타 : {num26.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['중상사고-기타', num26.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num27 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"경상사고-기타 : {num27.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['경상사고-기타', num27.text])

# 사고 선택 및 법규 위반 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num28 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"부상신고-기타 : {num28.text}건")

# 사고 데이터를 CSV에 저장
with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일에 헤더가 없을 경우 한 번만 작성
    # writer.writerow(['사고 유형', '발생건수'])
    writer.writerow(['부상신고-기타', num28.text])