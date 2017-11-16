import pandas as pd

# pandas를 사용하면 연속된 데이터셋인 Series로 구성해 주기 때문에 데이터만 나오는 것이 아니라 index도 같이 나온다.(두 개의 컬럼)
# dictionary와 비슷하지만 분명히 다르다(사용법은 비슷)

price = [92600, 92400, 92100, 94300, 92300]
s = pd.Series(price)
print(s)
print(s[0], s[1])

# index를 부여할 때는 반드시 데이터 개수와 같아야 한다.
s = pd.Series(
    [92600, 92400, 92100, 94300, 92300],
    index=['2017-01-01', '2017-02-02', '2017-03-03', '2017-04-04', '2017-05-05'])
print(s)
print(s[1], s['2017-02-02'])

# 스칼라 값으로 초기화 하기(당연히, 반드시 인덱스가 들어가야 한다)
s = pd.Series(7, index=['a', 'b', 'c', 'd'])
print(s)

# 사전으로 초기화 하기
d = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(d)
print(s)

s = pd.Series(d, index=['a', 'b', 'c', 'd'])
print(s)

# index와 values라는 이름의 속성을 통해 접근할 수 있다.
for date in s.index:
    print(date, end=' ')
else:
    print()

for price in s.values:
    print(price, end=' ')
else:
    print()

# 연산
# index 기반으로 같은 녀석들끼리 연산을 수행
s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
s2 = pd.Series([10, 20, 30], index=['C', 'B', 'A'])
print(s1 + s2)

s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
s2 = pd.Series([10, 20, 30], index=['B', 'C', 'D'])
print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 / s2)
print(s1 * 3)
