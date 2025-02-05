import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 한글설정
path = "Pretendard-Regular.ttf"
font = font_manager.FontProperties(fname=path)

file_name = "AccidentReport.csv"
df = pd.read_csv(file_name, encoding="cp949")

df.columns = df.columns.str.strip()  # 결측값 제거
df = df.astype(str)  # 모든 값을 문자열로 변환

# 서울만 따로 분리해서 저장
def filter_city(city):
    df["시도"] = df["시도"].str.strip()
    category = df[df.astype(str).apply(lambda x: x.str.contains("사고유형", na=False)).any(axis=1)]
    specific = df[df.astype(str).apply(lambda x: x.str.contains("세부유형", na=False)).any(axis=1)]
    sido = df.loc[df["시도"] == city]

    with open(f"{city}시 데이터 필터링.csv", "w", encoding="utf-8") as file:
        file.write(category.to_csv(index=False))
        file.write(specific.to_csv(index=False))
        file.write(sido.to_csv(index=False))

filter_city("서울")

# --------------------------------------------------------------------

# '조건설정' + '사고 유형'별 함수 (사망사고, 중상사고, ...) (차대사람-횡단사고, ..., 차대차-...)

file_name = "서울시 데이터 필터링.csv"
df = pd.read_csv(file_name, encoding="utf-8")

# ----------------------------------------------------------------

# 1. 전체 - 사망사고, 중상사고, ... 비율
categories = ["사망사고", "중상사고", "경상사고", "부상신고"]
conditions = ["사망[명]", "(중상자[명])", "(경상자[명])", "(부상신고자[명])"]

def filter_type(type):
    accident_df = df[df[df.columns[2]] == f"{type}"]
    with open("데이터 필터링.csv", "w", encoding="utf-8") as file:
        file.write(accident_df.to_csv(index=False))
    # 숫자 열만 선택하기
    cols_to_sum = accident_df.columns[3:]  # 첫 두 열 제외하고 나머지 열들
    # 모든 열에서 '-'를 NaN으로 변환 후, 숫자형으로 변환
    df_cleaned = accident_df[cols_to_sum].replace("-", pd.NA).apply(pd.to_numeric, errors='coerce')
    # 숫자들만 합산
    total_sum = df_cleaned.sum().sum()
    print(f"{type} 건수 합: {total_sum}")

    return total_sum

data = [filter_type(conditions[0]), filter_type(conditions[1]), filter_type(conditions[2]), filter_type(conditions[3])]

## - 바 그래프 사용
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.bar(categories, data, color=["red", "orange", "yellow", "green"])  # 사고 유형별 색상 적용

plt.title("2021~2023년 사고 종류별 건수 현황", fontsize=16, pad=10, fontproperties=font)
plt.xlabel("사고 조건", fontproperties=font)
plt.ylabel("건수", fontproperties=font)
plt.xticks(fontproperties=font)  # 한글 폰트 적용

plt.grid(axis="y", linestyle="--", alpha=0.7)  # y축 점선 표시
plt.show()

# ----------------------------------------------------------------

# 2. 사고별 - 차대차, 차대사람, 차량간, 철길건널목 비율
accident_types = ["차대차", "차대사람", "차량단독", "철길건널목"]

# "사고[건]"인 행 필터링
accident_df = df[df[df.columns[2]] == "사고[건]"]

# 사고 유형별 합산
## 사고유형 행
category_row = df[df[df.columns[2]] == "사고유형"]

## 두 DataFrame을 세로로 결합 (위아래로 붙이기)
combined_df = pd.concat([category_row, accident_df], ignore_index=True)

## 두 번째 행 가져오기
second_row = combined_df.iloc[0]

## "차대차" 등을 포함하는 열 찾기
def get_category(category):
    columns_with_car_vs_car = second_row[second_row.str.contains(f"{category}", na=False)].index

    # 해당 열들의 값을 합산 (숫자값만)
    values = []
    for col in columns_with_car_vs_car:
        values.append(combined_df[col])
    # 숫자만 포함된 값으로 변환 후 합산
    sum = 0
    for val in values:
        # 쉼표를 제거하고 숫자형으로 변환
        cleaned_values = val.replace(",", "").apply(pd.to_numeric, errors='coerce')
        sum += cleaned_values.sum()

    print(f"{category}의 건수 합: {sum}")
    return sum

df_accident = [get_category("차대차"), get_category("차대사람"), get_category("차량단독"), get_category("철길건널목")]

# 바 그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.bar(accident_types, df_accident, color=["red", "blue", "green", "purple"])  # 사고 유형별 색상 적용

plt.title("사고 유형별 건수 현황", fontsize=16, pad=10, fontproperties=font)
plt.xlabel("사고 유형", fontproperties=font)
plt.ylabel("건수(개)", fontproperties=font)
plt.xticks(fontproperties=font)  # 한글 폰트 적용

plt.grid(axis="y", linestyle="--", alpha=0.7)  # y축 점선 표시
plt.show()

# 3. 사고세부 - 차대차>무슨 사고, ... 전부 비교 > 꺾은 선 그래프
