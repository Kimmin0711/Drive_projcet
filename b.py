# 한페이지에 그래프 전부 다 나오는 코드 

# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib

# # 한글 폰트 설정 (예: 'Malgun Gothic' 윈도우 기본 폰트, 또는 다른 한글 폰트)
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우에서 사용 가능한 한글 폰트
# matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# # CSV 파일 읽기
# data = pd.read_csv('accident_data.csv', header=None, names=['Accident Type', 'Number of Occurrences'])

# # 쉼표 제거하고 발생건수 숫자 변환
# data['Number of Occurrences'] = data['Number of Occurrences'].replace({',': ''}, regex=True).astype(int)

# # 데이터 확인 (CSV에서 읽어온 데이터 확인)
# print(data)

# # 사고 유형과 발생건수 추출
# labels = data['Accident Type']
# values = data['Number of Occurrences']

# # 4개씩 7개의 그래프를 그리기 위해 subplot 설정
# fig, axes = plt.subplots(2, 4, figsize=(20, 12))  # 2행 4열의 그래프
# axes = axes.flatten()  # axes를 1차원으로 변환하여 접근하기 쉽게 만들기

# # 4개의 사고 유형씩 그래프 생성
# for i in range(7):
#     # 각 그래프에 4개의 데이터를 분할하여 그리기
#     start_index = i * 4
#     end_index = (i + 1) * 4
#     subset_data = data[start_index:end_index]
    
#     ax = axes[i]  # 각 서브플롯에 접근
#     ax.bar(subset_data['Accident Type'], subset_data['Number of Occurrences'], color = ['#FF0000', 'gold', 'green', 'b'], alpha = 0.3)  # 막대 그래프
#     ax.set_xlabel('Accident Type', fontsize=6)  # x축 레이블
#     ax.set_ylabel('Number of Occurrences', fontsize=6)  # y축 레이블
#     ax.tick_params(axis='x', rotation=45)  # x축 라벨 회전
    
#     # 그래프에 값 표시
#     for j, value in enumerate(subset_data['Number of Occurrences']):
#         ax.text(j, value + 20, str(value), ha='center', fontsize=6)

# # 불필요한 빈 그래프 없애기
# for i in range(7, 8):  # 7번 그래프는 비어있는 부분이므로 해당 부분은 숨김
#     axes[i].axis('off')

# plt.tight_layout()  # 레이아웃 조정
# plt.show()


# 그래프 하나씩 나오는 코드

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 사용가능한 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False  

# CSV 파일 읽기
data = pd.read_csv('accident_data.csv', header=None, names=['Accident Type', 'Number of Occurrences'])

# 쉼표 제거하고 발생건수 숫자 변환
data['Number of Occurrences'] = data['Number of Occurrences'].replace({',': ''}, regex=True).astype(int)

# CSV에서 읽어온 데이터 확인
print(data)

# 사고 유형과 발생건수 추출
labels = data['Accident Type']
values = data['Number of Occurrences']

# 4개씩 7개의 그래프를 그리기 위해 subplot 설정
for i in range(7):
    # 4개의 데이터를 분할하여 각 그래프를 그리기
    start_index = i * 4
    end_index = (i + 1) * 4
    subset_data = data[start_index:end_index]
    
    # 그래프 생성
    fig, ax = plt.subplots(figsize=(10, 6))  # 그래프 크기 설정
    ax.bar(subset_data['Accident Type'], subset_data['Number of Occurrences'], color=['#FF0000', 'gold', 'green', 'b'], alpha=0.3, width=0.6)  # 막대 그래프
    ax.set_xlabel('사고유형', fontsize=10, labelpad=20)  # x축 레이블
    ax.set_ylabel('발생건수', fontsize=10)  # y축 레이블
    ax.tick_params(axis='x')  # x축 라벨 회전
    
    # 그래프에 값 표시
    for j, value in enumerate(subset_data['Number of Occurrences']):
        ax.text(j, value + 20, str(value), ha='center', fontsize=8)
    
    plt.title("교통사고 범례위반 별 사고유형 발생건수", fontsize=15)
    plt.tight_layout()  # 레이아웃 조정
    plt.show()  # 각 그래프가 하나씩 나오도록 설정
