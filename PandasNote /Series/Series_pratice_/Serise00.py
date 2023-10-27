import pandas as pd
import numpy as np




# 다음의 Serise를 생성하시오.

# dtype은 float32가 되도록 생성하세요.
"""

Sol_1 = pd.Series([3.0, 5.0, 7.0, 9.0, 11.0])
print(Sol_1)


Sol_2 = pd.Series(['가','나','다','라','마'])
print(Sol_2)

# 다음에 Serise를 생성하고, Sample 변수에 대입하고 출력하세요

Sol_3 = pd.Series(['가','나','다','라','마'],index=([0, 1, 2, 3, 4]))
print(Sol_3)

Sol_4 = pd.Series([10,20,30,40,50],index=(['가','나','다','라','마']))
print(Sol_4)

# Sol4 중 '나'와 '라' 데이터를 조회하세요
print(Sol_4[['나','라']])
"""

# sample2 중 160 이하인 데이터만 필터하세요
np.random.seed(20)
sample2 = pd.Series(np.random.randint(100, 200, size=(15,)))
#print('Sol4 중 나와 라 데이터를 조회하세요 :')
#print(sample2[sample2 < 160])

# sample2 중 130 이상 170 이하인 데이터만 필터하세요
print('sample2 중 130 이상 170 이하인 데이터만 필터하세요')

print(sample2[130 <= sample2])

Sol5 = pd.Series(['apple',np.nan,'banana','kiwi','gubong'])
print(Sol5)

sample = pd.Series(['IT서비스',np.nan,'반도체',np.nan,'바이오','자율주행'])
print(sample)

# sample 중 결측치 데이터만 필터하세요
print(sample[[1,3]])

# sample중 결측치가 아닌 데이터만 필터하세요
print(sample[[0,2,4,5]])


np.random.seed(0)
sample = pd.Series(np.random.randint(100,200,size=(10,)))
print(sample)

print('sample에서 다음과 같은 결과를 가지도록 슬라이싱 하세요')
print(sample[2:7])

np.random.seed(0)
sample2 = pd.Series(np.random.randint(100, 200, size=(10,)),index=list('가나다라마바사아자차'))
print('sample2에서 다음과 같은 결과를 가지도록 슬라이싱 하세요')
print(sample2['바':])
print('sample2에서 다음과 같은 결과를 가지도록 슬라이싱 하세요 가나다')
print(sample2['가':'다'])
print('sample2에서 다음과 같은 결과를 가지도록 슬라이싱 하세요 나~바')
print(sample2['나':'바'])