import pandas as pd

# Series와 dict 데이터를 활용한 DataFrame
# json형태로 들어오는 데이터는 Dictionary안의 list들이 모여있는 형태인데, 이를 DataFrame으로 변경하여 많이 사용한다.

d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

d = [
    {'name': '둘리', 'age': 10, 'phone': '010-1111-1111'},
    {'name': '마이콜', 'age': 20, 'phone': '010-2222-2222'},
    {'name': '길동', 'age': 30, 'phone': '010-3333-3333'}]

df = pd.DataFrame(d)
print(df)


df2 = pd.DataFrame(d, columns=('name', 'phone'))
df3 = df2.set_index('name')
print(df3)

# 데이터 추가(열 추가)
df2['height'] = [150, 160, 170]
print(df2)

# 인덱스 선택
df3 = df2.set_index('name')
print(df3)
print(type(df3))

# 컬럼 선택
s = df2['name']
print(s)
print(type(s))

# merge
df4 = pd.DataFrame([{'sido': '서울'}, {'sido': '부산'}, {'sido': '전주'}])
df5 = pd.merge(df2, df4, left_index=True, right_index=True)
print(df5)

# merge & join
# 공통 열인 고객번호 열을 기준으로 데이터를 찾아서 합친다. 이 때 기본적으로는 양쪽 데이터프레임에 모두 키가 존재하는 데이터만 보여주는 inner join 방식
df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']})

df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]})

df3 = pd.merge(df1, df2)
print(df3)

# outer join 방식은 키 값이 한쪽에만 있어도 양쪽 데이터를 모두 보여준다(full)
df3 = pd.merge(df1, df2, how='outer')
print(df3)

# left, right 방식은 첫번째, 혹은 두번째 데이터프레임을 모두 보여준다.
print(pd.merge(df1, df2, how='left'))
# print(pd.merge(df1, df2, how='right'))

# 이름이 같은 열이 여러개 있는 경우에는 모두 기준 열로 사용된다.
# 기준 열은 on 인수로도 명시적 설정이 가능하다.
df1 = pd.DataFrame({'성별': ['남자', '남자', '여자'],
                    '연령': ['미성년자', '성인', '미성년자'],
                    '매출1': [1, 2, 3]})

df2 = pd.DataFrame({'성별': ['남자', '남자', '여자', '여자'],
                    '연령': ['미성년자', '미성년자', '미성년자', '성인'],
                    '매출2': [4, 5, 6, 7]})

# df3 = pd.merge(df1, df2)
# print(df3)
# df3 = pd.merge(df1, df2, on=['성별', '연령'])
# print(df3)
df3 = pd.merge(df1, df2, on=['성별'])
print(df3)

# 기준 열을 각각의 데이터프레임에 대해 다르게 정하려면 left_on, right_on 인수를 사용한다.
df1 = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                    'key2': ['one', 'two', 'one'],
                    'lval': [1, 2, 3]})
df2 = pd.DataFrame({'k1': ['foo', 'foo', 'bar', 'bar'],
                    'k2': ['one', 'one', 'one', 'two'],
                    'rval': [4, 5, 6, 7]})

df3 = pd.merge(df1, df2, left_on='key1', right_on='k1')
print(df3)

# 일반 데이터 열이 아닌 인덱스를 기준열로 사용하려면 left_index 또는 right_index 인수를 True 로 설정한다.
df1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],  'value': range(6)})
df2 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
# join 시 left는 'key' 컬럼을 기준으로 하고, right는 index를 기준으로 하라
pd.merge(df1, df2, left_on='key', right_index=True)

df1 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], columns=['Ohio', 'Nevada'], index=['a', 'c', 'e'])
df2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]], columns=['Missouri', 'Alabama'], index=['b', 'c', 'd', 'e'])
print(pd.merge(df1, df2, left_index=True, right_index=True))
