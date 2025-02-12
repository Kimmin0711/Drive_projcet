# # 한페이지에 그래프 전부 다 나오는 코드 (막대그래프)

# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib

# # 한글 폰트 설정 (예: 'Malgun Gothic' 윈도우 기본 폰트, 또는 다른 한글 폰트)
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우에서 사용 가능한 한글 폰트
# matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# # CSV 파일 읽기
# data = pd.read_csv('Seoul.csv', header=None, names=['Accident Type', 'Number of Occurrences'])

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


##################################################################################################################


# # 그래프 하나씩 나오는 코드 (막대그래프)

# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib

# # 한글 폰트 설정
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 사용가능한 한글 폰트
# matplotlib.rcParams['axes.unicode_minus'] = False  

# # CSV 파일 읽기
# data = pd.read_csv('Seoul.csv', header=None, names=['Accident Type', 'Number of Occurrences'])

# # 쉼표 제거하고 발생건수 숫자 변환
# data['Number of Occurrences'] = data['Number of Occurrences'].replace({',': ''}, regex=True).astype(int)

# # CSV에서 읽어온 데이터 확인
# print(data)

# # 사고 유형과 발생건수 추출
# labels = data['Accident Type']
# values = data['Number of Occurrences']

# # 4개씩 7개의 그래프를 그리기 위해 subplot 설정
# for i in range(7):
#     # 4개의 데이터를 분할하여 각 그래프를 그리기
#     start_index = i * 4
#     end_index = (i + 1) * 4
#     subset_data = data[start_index:end_index]
    
#     # 그래프 생성
#     fig, ax = plt.subplots(figsize=(10, 6))  # 그래프 크기 설정
#     ax.bar(subset_data['Accident Type'], subset_data['Number of Occurrences'], color=['#FF0000', 'gold', 'green', 'b'], alpha=0.3, width=0.6)  # 막대 그래프
#     ax.set_xlabel('사고유형', fontsize=10, labelpad=20)  # x축 레이블
#     ax.set_ylabel('발생건수', fontsize=10)  # y축 레이블
#     ax.tick_params(axis='x')  # x축 라벨 회전
    
#     # 그래프에 값 표시
#     for j, value in enumerate(subset_data['Number of Occurrences']):
#         ax.text(j, value + 20, str(value), ha='center', fontsize=8)
    
#     plt.title("교통사고 발생건수", fontsize=15)
#     plt.tight_layout()  # 레이아웃 조정
#     plt.show()  # 각 그래프가 하나씩 나오도록 설정


##################################################################################################################


# 사망/중상/경상/부상신고 법규위반 별 막대그래프 (하나씩)

# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib

# # 한글 폰트 설정
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 사용가능한 한글 폰트
# matplotlib.rcParams['axes.unicode_minus'] = False  

# # CSV 파일 읽기
# df = pd.read_csv('Seoul.csv', header=None, names=['사고유형', '발생건수'])

# # 쉼표 제거하고 발생건수 숫자 변환
# df['발생건수'] = df['발생건수'].replace({',': ''}, regex=True).astype(int)

# # '사고유형'에서 사고 유형 이름만 추출 (사망사고, 중상사고, 경상사고, 부상신고)
# df['사고유형_수정'] = df['사고유형'].str.split(' - ').str[1]

# # 사고유형별로 구분하여 사망사고, 중상사고, 경상사고, 부상신고사고로 나누기
# death_accidents = df[df['사고유형'].str.contains('사망사고')]
# serious_accidents = df[df['사고유형'].str.contains('중상사고')]
# light_accidents = df[df['사고유형'].str.contains('경상사고')]
# minor_injuries = df[df['사고유형'].str.contains('부상신고')]

# # 사망사고 발생 건수 그래프
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.bar(death_accidents['사고유형_수정'], death_accidents['발생건수'], color=plt.cm.Paired.colors)
# ax.set_title('사망사고 발생 건수')
# ax.set_xlabel('법규위반')
# ax.set_ylabel('발생건수')
# plt.xticks(fontsize=8)
# plt.tight_layout()
# plt.show()  # 그래프 하나씩 나오도록 설정

# # 중상사고 발생 건수 그래프
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.bar(serious_accidents['사고유형_수정'], serious_accidents['발생건수'], color=plt.cm.Paired.colors)
# ax.set_title('중상사고 발생 건수')
# ax.set_xlabel('법규위반')
# ax.set_ylabel('발생건수')
# plt.xticks(fontsize=8)
# plt.tight_layout()
# plt.show()  # 그래프 하나씩 나오도록 설정

# # 경상사고 발생 건수 그래프
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.bar(light_accidents['사고유형_수정'], light_accidents['발생건수'], color=plt.cm.Paired.colors)
# ax.set_title('경상사고 발생 건수')
# ax.set_xlabel('법규위반')
# ax.set_ylabel('발생건수')
# plt.xticks(fontsize=8)
# plt.tight_layout()
# plt.show()  # 그래프 하나씩 나오도록 설정

# # 부상신고 사고 발생 건수 그래프
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.bar(minor_injuries['사고유형_수정'], minor_injuries['발생건수'], color=plt.cm.Paired.colors)
# ax.set_title('부상신고 발생 건수')
# ax.set_xlabel('법규위반')
# ax.set_ylabel('발생건수')
# plt.xticks(fontsize=8)
# plt.tight_layout()
# plt.show()  # 그래프 하나씩 나오도록 설정


##################################################################################################################


# 그래프 하나씩 나오는 코드 (꺾은선그래프)

# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib

# # 한글 폰트 설정
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 사용가능한 한글 폰트
# matplotlib.rcParams['axes.unicode_minus'] = False  

# # CSV 파일 읽기
# data = pd.read_csv('Seoul.csv', header=None, names=['Accident Type', 'Number of Occurrences'])

# # 쉼표 제거하고 발생건수 숫자 변환
# data['Number of Occurrences'] = data['Number of Occurrences'].replace({',': ''}, regex=True).astype(int)

# # CSV에서 읽어온 데이터 확인
# print(data)

# # 사고 유형과 발생건수 추출
# labels = data['Accident Type']
# values = data['Number of Occurrences']

# # 4개씩 7개의 그래프를 그리기 위해 subplot 설정
# for i in range(7):
#     # 4개의 데이터를 분할하여 각 그래프를 그리기
#     start_index = i * 4
#     end_index = (i + 1) * 4
#     subset_data = data[start_index:end_index]
    
#     # 그래프 생성
#     fig, ax = plt.subplots(figsize=(10, 6))  # 그래프 크기 설정
#     ax.plot(subset_data['Accident Type'], subset_data['Number of Occurrences'], marker='o', color='r', linestyle='-', alpha=0.3)  # 꺾은선 그래프
#     ax.set_xlabel('사고유형', fontsize=10, labelpad=20)  # x축 레이블
#     ax.set_ylabel('발생건수', fontsize=10)  # y축 레이블
    
#     # 그래프에 값 표시
#     for j, value in enumerate(subset_data['Number of Occurrences']):
#         ax.text(j, value + 20, str(value), ha='center', fontsize=8)
    
#     plt.title("교통사고 발생건수", fontsize=15)
#     plt.tight_layout()  # 레이아웃 조정
#     plt.show()  # 각 그래프가 하나씩 나오도록 설정


##################################################################################################################


# 파이 차트로 나타낸 것

# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib

# # 한글 폰트 설정
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 사용가능한 한글 폰트
# matplotlib.rcParams['axes.unicode_minus'] = False  

# # CSV 파일 읽기
# df = pd.read_csv('Seoul.csv', header=None, names=['사고유형', '발생건수'])

# # 쉼표 제거하고 발생건수 숫자 변환
# df['발생건수'] = df['발생건수'].replace({',': ''}, regex=True).astype(int)

# # '사고유형'에서 사고 유형 이름만 추출 (사망사고, 중상사고, 경상사고, 부상신고)
# df['사고유형_수정'] = df['사고유형'].str.split(' - ').str[1]

# # 사고유형별로 구분하여 사망사고, 중상사고, 경상사고, 부상신고사고로 나누기
# death_accidents = df[df['사고유형'].str.contains('사망사고')]
# serious_accidents = df[df['사고유형'].str.contains('중상사고')]
# light_accidents = df[df['사고유형'].str.contains('경상사고')]
# minor_injuries = df[df['사고유형'].str.contains('부상신고')]

# # 그래프 그리기
# fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# # 파이차트
# axs[0, 0].pie(death_accidents['발생건수'], autopct='%1.1f%%', startangle=90, colors = plt.cm.Paired.colors)
# axs[0, 0].set_title('사망사고 발생 비율')

# axs[0, 1].pie(serious_accidents['발생건수'], autopct='%1.1f%%', startangle=90, colors = plt.cm.Paired.colors)
# axs[0, 1].set_title('중상사고 발생 비율')

# axs[1, 0].pie(light_accidents['발생건수'], autopct='%1.1f%%', startangle=90, colors = plt.cm.Paired.colors)
# axs[1, 0].set_title('경상사고 발생 비율')

# axs[1, 1].pie(minor_injuries['발생건수'], autopct='%1.1f%%', startangle=90, colors = plt.cm.Paired.colors)
# axs[1, 1].set_title('부상신고 발생 비율')

# fig.legend(death_accidents['사고유형_수정'], title="법규위반", loc='upper right')

# plt.tight_layout()
# plt.show()



##################################################################################################################


# 꺾은선 그래프로 나타낸 것 

# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib

# # 한글 폰트 설정
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 사용가능한 한글 폰트
# matplotlib.rcParams['axes.unicode_minus'] = False  

# # CSV 파일 읽기
# df = pd.read_csv('Seoul.csv', header=None, names=['사고유형', '발생건수'])

# # 쉼표 제거하고 발생건수 숫자 변환
# df['발생건수'] = df['발생건수'].replace({',': ''}, regex=True).astype(int)

# # '사고유형'에서 사고 유형 이름만 추출 (사망사고, 중상사고, 경상사고, 부상신고)
# df['사고유형_수정'] = df['사고유형'].str.split(' - ').str[1]

# # 사고유형별로 구분하여 사망사고, 중상사고, 경상사고, 부상신고사고로 나누기
# death_accidents = df[df['사고유형'].str.contains('사망사고')]
# serious_accidents = df[df['사고유형'].str.contains('중상사고')]
# light_accidents = df[df['사고유형'].str.contains('경상사고')]
# minor_injuries = df[df['사고유형'].str.contains('부상신고')]

# # 꺾은선 그래프 그리기
# plt.figure(figsize=(14, 8))

# # 각 사고유형의 발생건수를 꺾은선 그래프로 나타내기
# plt.plot(death_accidents['사고유형_수정'], death_accidents['발생건수'], marker='o', label='사망사고', color='red')
# plt.plot(serious_accidents['사고유형_수정'], serious_accidents['발생건수'], marker='o', label='중상사고', color='orange')
# plt.plot(light_accidents['사고유형_수정'], light_accidents['발생건수'], marker='o', label='경상사고', color='green')
# plt.plot(minor_injuries['사고유형_수정'], minor_injuries['발생건수'], marker='o', label='부상신고', color='blue')

# # 그래프 제목, 레이블 설정
# plt.title('법규위반 별 건수 현황')
# plt.xlabel('법규위반')
# plt.ylabel('발생건수')

# # 범례 표시
# plt.legend(title='사고유형')

# # 그래프 출력
# plt.tight_layout()
# plt.show()