# 사망/중상/경상/부상신고 법규위반 별 막대그래프 (하나씩)

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 사용가능한 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False  

# CSV 파일 읽기
df = pd.read_csv('Gangnamgu.csv', header=None, names=['사고유형', '발생건수'])

# 쉼표 제거하고 발생건수 숫자 변환
df['발생건수'] = df['발생건수'].replace({',': ''}, regex=True).astype(int)

# '사고유형'에서 사고 유형 이름만 추출 (사망사고, 중상사고, 경상사고, 부상신고)
df['사고유형_수정'] = df['사고유형'].str.split(' - ').str[1]

# 사고유형별로 구분하여 사망사고, 중상사고, 경상사고, 부상신고사고로 나누기
death_accidents = df[df['사고유형'].str.contains('사망사고')]
serious_accidents = df[df['사고유형'].str.contains('중상사고')]
light_accidents = df[df['사고유형'].str.contains('경상사고')]
minor_injuries = df[df['사고유형'].str.contains('부상신고')]

# 사망사고 발생 건수 그래프
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(death_accidents['사고유형_수정'], death_accidents['발생건수'], color=plt.cm.Paired.colors)
ax.set_title('사망사고 발생 건수')
ax.set_xlabel('법규위반')
ax.set_ylabel('발생건수')
plt.xticks(fontsize=8)
plt.tight_layout()
plt.show()  # 그래프 하나씩 나오도록 설정

# 중상사고 발생 건수 그래프
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(serious_accidents['사고유형_수정'], serious_accidents['발생건수'], color=plt.cm.Paired.colors)
ax.set_title('중상사고 발생 건수')
ax.set_xlabel('법규위반')
ax.set_ylabel('발생건수')
plt.xticks(fontsize=8)
plt.tight_layout()
plt.show()  # 그래프 하나씩 나오도록 설정

# 경상사고 발생 건수 그래프
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(light_accidents['사고유형_수정'], light_accidents['발생건수'], color=plt.cm.Paired.colors)
ax.set_title('경상사고 발생 건수')
ax.set_xlabel('법규위반')
ax.set_ylabel('발생건수')
plt.xticks(fontsize=8)
plt.tight_layout()
plt.show()  # 그래프 하나씩 나오도록 설정

# 부상신고 사고 발생 건수 그래프
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(minor_injuries['사고유형_수정'], minor_injuries['발생건수'], color=plt.cm.Paired.colors)
ax.set_title('부상신고 발생 건수')
ax.set_xlabel('법규위반')
ax.set_ylabel('발생건수')
plt.xticks(fontsize=8)
plt.tight_layout()
plt.show()  # 그래프 하나씩 나오도록 설정