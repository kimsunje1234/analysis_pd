import json

import math

import numpy as np
import pandas as pd
import scipy.stats as ss


def analysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspot_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    tourspots = tourspot_table['tourist_spot'].unique()

    results = []
    for tourspot in tourspots:
        data = {'tourspot':tourspot}

        # tourspot_table['tourist_spot'] == tourspot 이걸 찍어보면, index와 boolean값이 나온다.
        # tourspot_table[tourspot_table['tourist_spot'] == tourspot] 는 True인 애들의 index로 접근해서 가져옴
        temp_tourspot_table = tourspot_table[tourspot_table['tourist_spot'] == tourspot].set_index('date')

        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())

            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
            country_name = foreignvisitor_table['country_name'].unique().item()

            foreignvisitor_table = foreignvisitor_table.set_index('date')
            merge_table = pd.merge(temp_tourspot_table, foreignvisitor_table, left_index=True, right_index=True)

            x = list(merge_table['visit_count'])
            y = list(merge_table['count_foreigner'])
            r = r = correlation_coefficient(x, y)

            data['r_' + country_name] = r

        results.append(data)

    return results


def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError:
        r = 0.0

    return r


# 분석 시에는 데이터셋으로 뭘 할건지 이해한 후에 입력/출력값을 확실히 한 후에 코드를 완성할 것
def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspot_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    temp_tourspot_table = tourspot_table.groupby('date')['count_foreigner'].sum()
    print(temp_tourspot_table.index)

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        foreignvisitor_table = foreignvisitor_table.set_index('date')

        # 아래는 공통된 컬럼이 없으니 index로 조인
        merge_table = pd.merge(temp_tourspot_table, foreignvisitor_table, left_index=True, right_index=True)

        x = list(merge_table['visit_count'])
        y = list(merge_table['count_foreigner'])
        # unique()는 SQL문의 distinct와 동일 -> unique()는 리턴값이 numpy.ndarray로 나오니(모양은 list이나 ndarry type의 다차원 배열임) 주의!!
        country_name = foreignvisitor_table['country_name'].unique().item()

        # 상관계수 구하기 (scipy lib의 seaborn 을 사용하면 좋으나 여기선 사용 안함)
        # r = correlation_coefficient(x, y)

        # scipy를 이용한 상관계수 구하기
        r = ss.pearsonr(x, y)[0]

        # numpy 이용한 상관계수 구하기
        # r = np.corrcoef(x, y).item(1)
        results.append({'x':x, 'y':y, 'country_name':country_name, 'r':r})

    return results