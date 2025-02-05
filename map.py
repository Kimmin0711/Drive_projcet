from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # By사용
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

# 옵션 설정
chrome_option = Options()
chrome_option.add_argument("--headless")  # GUI창 안열기
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_option)

driver.get("https://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_STS_RSN#")
time.sleep(2)

# 사고년도 설정
year = driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]')
year.click()
year_check = driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]/option[3]')
year_check.click()
time.sleep(2)

# 시도 설정
city = driver.find_element(By.XPATH, '//*[@id="ptsRafSido"]')
city.click()
city_check = driver.find_element(By.XPATH, '//*[@id="ptsRafSido"]/option[1]')
city_check.click()
time.sleep(2)

# 조건 설정
for i in range(1, 5):  # 1부터 4까지의 체크박스
    checkbox_xpath = f'//*[@id="ptsRafCh1AccidentContent"]/li[{i}]/input'
    checkbox = driver.find_element(By.XPATH, checkbox_xpath)
    if not checkbox.is_selected():
        # 체크상태로 만들기
        checkbox.click()
        time.sleep(1)
# 처음 강남구 값 출력
test = driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]')
test.click()
test_check = driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]/option[2]')
test_check.click()
time.sleep(2)
test_search = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[2]/p/a')
test_search.click()
time.sleep(2)

raw_data = []

#시군구 설정
for t in range(2, 27):
    town = driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]')
    town.click()
    town_check = driver.find_element(By.XPATH, f'//*[@id="ptsRafSigungu"]/option[{t}]')
    town_check.click()
    time.sleep(2)

    # 검색하기
    search = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[2]/p/a')
    search.click()
    time.sleep(5)

# 값이 바뀌기 전까지 최대 30초 대기
    value_xpath = '//*[@id="regionAccidentFind"]/div[3]/div[1]/span'
    value = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, value_xpath)))
    value.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
    time.sleep(2)
    print(f"{town_check.text}: 총 {value.text} 건")
    value_text = value.text.replace(',', '')
    if value_text.isdigit():
        value_number = int(value_text)
        raw_data.append([town_check.text, value_text])
    time.sleep(2)
# print(raw_data)

# 지도 시각화
import folium
import pandas as pd


# 서울시 구 지도데이터
geo_json = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
data = pd.DataFrame(raw_data, columns=['name', 'value'])

map = folium.Map(
    location=[37.566345, 126.977893],  # 서울시 위치
    zoom_start=11,
    # tiles='CartoDB Positron',
    )

folium.Choropleth(
    geo_data=geo_json,
    # name='choropleth',
    data=data,
    columns=['name', 'value'],
    # geo_json 안에 있는 데이터 값을 지정
    key_on='feature.properties.name',
    fill_color='PuRd',
    fill_opacity=0.7,  # 배경 색칠 불투명도
    line_opacity=0.5, # 구분선 불투명도
    legend_name= '교통사고 피해 건수'
).add_to(map)

map.save('map.html')