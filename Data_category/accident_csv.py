import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
labels = ["A", "B", "C", "D"]
conditions = ["사망[명]", "(중상자[명])", "(경상자[명])", "(부상신고자[명])"]

def filter_type(type):
    accident_df = df[df[df.columns[2]] == f"{type}"]

    # 숫자 열만 선택하기
    cols_to_sum = accident_df.columns[3:]  # 첫 두 열 제외하고 나머지 열들
    # 모든 열에서 '-'를 NaN으로 변환 후, 숫자형으로 변환
    df_cleaned = accident_df[cols_to_sum].replace("-", pd.NA).apply(pd.to_numeric, errors='coerce')
    # 숫자들만 합산
    total_sum = df_cleaned.sum().sum()
    print(f"{type} 건수 합: {total_sum}")

    return total_sum

data = [filter_type(conditions[0]), filter_type(conditions[1]), filter_type(conditions[2]), filter_type(conditions[3])]

## - 파이차트 그래프 사용
fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(
    data, 
    labels = labels,
    wedgeprops = {'edgecolor':'black','linewidth': 1, 'width': 0.7},
    colors = ["red", "orange", "yellow", "green"], # 사고 유형별 색상 적용
    counterclock = False,
    startangle = 90,
    explode = [0, 0.1, 0, 0.1],
    autopct = '%1.1f%%', 
)

plt.title("2021~2023년 사고 종류별 건수 현황", fontsize=16, pad=10, fontproperties=font)
# 범례 추가
ax.legend(wedges, categories, loc="center left", bbox_to_anchor=(1, 0.5), prop=font)
plt.show()

# ----------------------------------------------------------------
'''
# 2. 사고별 - 차대차, 차대사람, 차량간, 철길건널목 비율
accident_types = ["차대차", "차대사람", "차량단독", "철길건널목"]
combined_df = pd.DataFrame()

## "사망사고 > 차대차" 등을 포함하는 열 필터링해서 찾는 함수
def get_category(category, type):
    accident_df = df[df[df.columns[2]] == f"{type}"]
    # 사고 유형별 합산
    ## 사고유형 행
    category_row = df[df[df.columns[2]] == "사고유형"]
    ## 두 DataFrame을 세로로 결합 (위아래로 붙이기)
    combined_df = pd.concat([category_row, accident_df], ignore_index=True)
    with open("데이터 필터링.csv", "w", encoding="utf-8") as file:
        file.write(combined_df.to_csv(index=False))
    ## 두 번째 행 가져오기
    second_row = combined_df.iloc[0]
    columns = second_row[second_row.str.contains(f"{category}", na=False)].index

    # 해당 열들의 값을 합산 (숫자값만)
    values = []
    for col in columns:
        values.append(combined_df[col])
    # 숫자만 포함된 값으로 변환 후 합산
    sum = 0
    for val in values:
        # 쉼표를 제거하고 숫자형으로 변환
        cleaned_values = val.replace(",", "").apply(pd.to_numeric, errors='coerce')
        sum += cleaned_values.sum()

    print(f"{category}의 {type}수 합: {sum}")
    return sum

df_accident1 = [get_category("차대차", "사망[명]"), get_category("차대사람", "사망[명]"), get_category("차량단독", "사망[명]"), get_category("철길건널목", "사망[명]")]
df_accident2 = [get_category("차대차", "(중상자[명])"), get_category("차대사람", "(중상자[명])"), get_category("차량단독", "(중상자[명])"), get_category("철길건널목", "(중상자[명])")]
df_accident3 = [get_category("차대차", "(경상자[명])"), get_category("차대사람", "(경상자[명])"), get_category("차량단독", "(경상자[명])"), get_category("철길건널목", "(경상자[명])")]
df_accident4 = [get_category("차대차", "(부상신고자[명])"), get_category("차대사람", "(부상신고자[명])"), get_category("차량단독", "(부상신고자[명])"), get_category("철길건널목", "(부상신고자[명])")]

## 꺾은 선 그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.plot(accident_types, df_accident1, label="사망사고", color='red', marker="o", markersize=5, markerfacecolor="red")  # 사고 유형별 색상 적용
plt.plot(accident_types, df_accident2, label="중상사고", color='orange', marker="o", markersize=5, markerfacecolor="orange")
plt.plot(accident_types, df_accident3, label="경상사고", color='yellow', marker="o", markersize=5, markerfacecolor="yellow")
plt.plot(accident_types, df_accident4, label="부상신고", color='green', marker="o", markersize=5, markerfacecolor="green")

plt.title("사고 유형별 건수 현황", fontsize=16, pad=10, fontproperties=font)
plt.xlabel("사고 유형", fontproperties=font)
plt.ylabel("건수(개)", fontproperties=font)
plt.xticks(fontproperties=font)  # 한글 폰트 적용
plt.legend(loc="upper right", ncol=1, prop=font)

plt.grid(axis="y", linestyle="--", alpha=0.7)  # y축 점선 표시
plt.show()
'''
# -------------------------------------------------------------------------------

# 3. 사고세부 - 차대차>무슨 사고(%), ... 전부 비교 > 바 그래프
categories = ["차대사람", "차대차", "차량단독", "철길건널목"]
accident_details = {
    "차대사람": ["횡단중", "차도통행중", "길가장자리구역통행중", "보도통행중", "기타"],
    "차대차": ["충돌", "추돌", "기타"],
    "차량단독": ["충돌", "도로이탈", "전도전복", "기타"],
    "철길건널목": ["철길건널목"],
}
data = {}
combined_df = pd.DataFrame()

def sum_values(values, accident):
    # 숫자만 포함된 값으로 변환 후 합산
    sum = 0
    for val in values:
        if val[1] == accident:  # 특정 사고 유형(예: '횡단중') 필터링
            
            # 쉼표 제거 후 숫자형 변환
            cleaned_values = val.drop(1).replace(",", "").apply(pd.to_numeric, errors='coerce')
            sum += cleaned_values.sum()
    return sum


## "사망사고 > 차대차 > 횡단중" 등을 포함하는 열 필터링해서 찾는 함수
def get_category(category, type):
    accident_df = df[df[df.columns[2]] == f"{type}"]
    # 사고 유형별 분류 > 세부 유형별 합산
    ## 사고유형 행
    category_row = df[df[df.columns[2]] == "사고유형"]
    specific_row = df[df[df.columns[2]] == "세부유형"]
    ## 세 DataFrame을 세로로 결합 (위아래로 붙이기)
    combined_df = pd.concat([specific_row, accident_df], ignore_index=True)
    new_combined_df = pd.concat([category_row, combined_df], ignore_index=True)
    with open("데이터 필터링.csv", "w", encoding="utf-8") as file:
        file.write(new_combined_df.to_csv(index=False))
    ## 두 번째 행 가져오기
    second_row = new_combined_df.iloc[0]
    columns = second_row[second_row.str.contains(f"{category}", na=False)].index
    ## 그 안에서 세부유형 행으로 나누기
    values = [new_combined_df[col] for col in columns]
    # print(values[0][1]) # 충돌
    # print(values[1][1]) # 추돌
    # print(values[2][1]) # 기타

    # 사고 유형별 비율 계산
    accident_types = accident_details.get(category, [])
    total_sum = sum(sum_values(values, t) for t in accident_types)  # 전체 건수
    data = {}

    if total_sum > 0:
        percentages = [100 * sum_values(values, t) / total_sum if sum_values(values, t) > 0 else 0 for t in accident_types]
    else:
        percentages = [0] * len(accident_types)  # 모든 값이 0이면 에러 방지

    data[category] = percentages
    return accident_types, data, total_sum
# print(get_category("차량단독", "사망[명]"))

# def get_BarGraph(type): # type : 사망, 중상, 경상, 부상
#     fig, axes = plt.subplots(4, 1, figsize=(4, 8))
#     fig.subplots_adjust(hspace=10.0)

#     for i, category in enumerate(categories):
#         ax = axes[i]
#         accident_types, data, total_sum = get_category(category, type)
#         values = data[category]
#         bar_positions = np.arange(len(accident_types))

#         # 색상을 accident_types 개수에 맞게 동적으로 조정
#         colors = plt.cm.viridis(np.linspace(0, 1, len(accident_types)))

#         ax.bar(bar_positions, values, color=colors, label=f"{category} 총 건수: {total_sum}건")

#         # 막대 위에 % 표시
#         for pos, val in zip(bar_positions, values):
#             ax.text(pos, val + 2, f"{val:.1f}%", ha='center', va='bottom')

#         # 서브플롯 제목 및 축 설정
#         ax.set_title(f"{category} 사고 그래프", fontsize=20 ,fontproperties=font)
#         ax.set_xticks(bar_positions)
#         ax.set_xticklabels(accident_types, fontproperties=font)
#         ax.set_ylim(0, 100)  # % 기준으로 Y축 고정
#         ax.legend(loc="upper right", prop=font)

#     plt.tight_layout()
#     plt.show()
def get_StackedBarGraph(type):
    """ 누적 퍼센트 그래프 생성 (Stacked Bar Chart) """
    fig, ax = plt.subplots(figsize=(5, 15))

    bar_positions = np.arange(len(categories))
    bottom_values = np.zeros(len(categories))  # 누적을 위한 초기 값
    colors = plt.cm.viridis(np.linspace(0, 1, max(len(d) for d in accident_details.values())))

    for i, category in enumerate(categories):
        accident_types, data, total_sum = get_category(category, type)
        values = data[category]

        for j, (accident_type, value) in enumerate(zip(accident_types, values)):
            bars = ax.bar(bar_positions[i], value, bottom=bottom_values[i], color=colors[j], label=accident_type if i == 0 else "")
            bottom_values[i] += value

            # 막대의 중앙에 비율(%) 표시
            if value > 0:
                ax.text(bar_positions[i], bottom_values[i] - (value / 2), f"{accident_type}: {value:.1f}% ({int(total_sum*value/100)}건)", ha='center', va='center', fontsize=8, color='white', fontweight='bold', fontproperties=font)

        # 각 막대 위에 총 건수 표시
        ax.text(bar_positions[i], 105, f"{total_sum}건", ha='center', fontsize=12, fontweight='bold', color='black', fontproperties=font)

    ax.set_xticks(bar_positions)
    ax.set_xticklabels(categories, fontsize=12, fontproperties=font)
    ax.set_ylabel("비율 (%)", fontproperties=font)
    ax.set_ylim(0, 110)  # Y축 100% + 여백
    ax.set_title(f"사고 유형별 세부 유형 비율 ({type})", fontsize=14, fontproperties=font)

    plt.show()

get_StackedBarGraph("사망[명]")
get_StackedBarGraph("(중상자[명])")
get_StackedBarGraph("(경상자[명])")
get_StackedBarGraph("(부상신고자[명])")











'''
## 바 그래프 그리기 (사망 > 중간유형(세부유형 %로), 총 건수 / 중상 > 중간유형(세부유형 %로), 총 건수 / ...)
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
def get_barGraph(category):
    plt.bar(accident_types, get_category(f"{category}", "사망[명]"), label="사망사고", color='red')  # 사고 유형별 색상 적용
    plt.bar(accident_types, get_category(f"{category}", "(중상자[명])"), label="중상사고", color='orange')
    plt.bar(accident_types, get_category(f"{category}", "(경상자[명])"), label="경상사고", color='yellow')
    plt.bar(accident_types, get_category(f"{category}", "(부상신고자[명])"), label="부상신고", color='green')

plt.title("사고 유형별 건수 현황", fontsize=16, pad=10, fontproperties=font)
plt.xlabel("사고 유형", fontproperties=font)
plt.ylabel("건수(개)", fontproperties=font)
plt.xticks(fontproperties=font)  # 한글 폰트 적용
plt.legend(loc="upper right", ncol=1, prop=font)

plt.grid(axis="y", linestyle="--", alpha=0.7)  # y축 점선 표시
plt.show()
'''