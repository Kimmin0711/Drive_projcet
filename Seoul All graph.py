import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# CSV 파일을 읽기 (기본적으로 쉼표로 구분된 파일임)
df = pd.read_csv('Seoul All.csv')

# 열 이름을 수동으로 지정
df.columns = ['사고유형', '수']

# '사고유형'과 '수'에서 공백 제거
df['사고유형'] = df['사고유형'].str.strip()
df['수'] = df['수'].str.replace(',', '').str.strip()

# '수'를 정수로 변환
df['수'] = df['수'].astype(int)

# 데이터 확인
print(df)

# '사고유형'과 '수' 열 추출
labels = df['사고유형']
sizes = df['수']

# 전체 사고 수
total = sizes.sum()

# 각 항목의 비율 계산
percentages = sizes / total * 100

# 출력: 각 항목의 비율
for label, percentage in zip(labels, percentages):
    print(f'{label}: {percentage:.1f}%')

# 파이차트 생성
# 한글폰트 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 사용가능한 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False  

# 파이차트 생성
explode = [0.07, 0.1, 0, 0.08]  # 항목별로 분리되는 크기 조정
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=120, 
        colors=['red', 'orange', 'yellow', 'green'], wedgeprops={"edgecolor":"black",'width': 0.6})

# 그래프 제목
plt.title("사고 유형별 비율")
plt.legend(labels=labels, loc='center right', fontsize=12, frameon=False, bbox_to_anchor=(1.18, 0.5))

# 파이차트 출력
plt.show()
