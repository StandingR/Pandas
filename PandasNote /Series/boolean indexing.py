import pandas as pd
import numpy as np

#np.random.seed(0)
#s = pd.Series(np.random.randint(10000, 20000, size=(10,)))
#print(s)
#print(s>15000)
#15000 이상인 데이터 필터
#print(s[s > 15000])
#기본 값으로 부여되는 RangeIndex에 사용자 정의의 index를 지정할 수 있습니다.
s = pd.Series(['마케팅','경영','개발','기획','인사'],index=['a','b','c','d','e'])
#print(s)

#print(s.index)
#사용자 정의의 index 부여시 변경된 index로 조회 가능합니다.
#print(s['c'])
#print(s[['a','d']])
# 먼저, Series를 생성 후 index 속성 값에 새로운 index를 할당하여 인덱스를 지정할 수 있습니다.
s = pd.Series(['마케팅','경영','개발','기획','인사'])
#print(s.index)
s.index=list('abcde')
#print(s.index)

# 속성 (attribute)
"""
values

values는 Series 데이터 값(value)만 numpy array 형식으로 가져 옵니다
"""

#print(s.values)

# ndim - 차원
# Series는 1차원 자료구조이기 떄문에 ndim 출력시 1이 출력됩니다.

#print(s.ndim)

"""
shape

shape은 데이터의 모양(shape)을 알아보기 위하여 사용하는데, 
Series의 shape은 데이터의 갯수를 나타냅니다.

튜플(tuple) 형식으로 출력됩니다.
"""

#print(s.shape)

"""
NaN (Not a Number)

Pandas에서 NaN 값은 비어있는 결측치 데이터를 의미합니다.

임의로 비어있는 값을 대입하고자 할 때는 numpy의 nan (np.nan)을 입력합니다.

"""

s = pd.Series(['선화','강호',np.nan,'소정','우영'])
#print(s)

"""
결측치 (NaN) 값 처리

isnull()과 isna()은 NaN 값을 찾는 함수 입니다.

isnull()과 isna()는 결과가 동일합니다

"""

"""
슬라이싱

(주의) 숫자형 index로 접근할 때는 뒷 index가 포함되지 않습니다.
"""

s =pd.Series(np.arange(100,150,10))
#print(s)

#print(s.isnull())

#print(s.isna())

"""
이를 boolean indexing에 적용해볼 수 있습니다
"""

#print(s[s.isnull()])

"""
notnull()은 NaN값이 아닌, 
즉 비어있지 않은 데이터를 찾는 함수 입니다.
"""

#print(s.notnull())

#print(s.notna())

#print(s[s.notnull()])

"""
슬라이싱

(주의) 숫자형 index로 접근할 때는 뒷 index가 포함되지 않습니다.
"""

s = pd.Series(np.arange(100,150,10))
print(s)
print(s[1:3])

s.index = list('가나다라마')
print(s.index)

print(s['나':'라'])

