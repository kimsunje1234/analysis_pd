import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import json

with open('../__results__/crawling/서울특별시_tourspot_2017_2017.json', 'r', encoding='utf-8') as infile:
    json_data = json.loads(infile.read())

cn_visit_table = pd.DataFrame(json_data, columns=['date', 'visit_count'])
cn_visit_table.date = pd.to_datetime(cn_visit_table.date, format='%Y%m')
# 아래는 pandas에서 제공해주는 것들
cn_visit_table['year'] = cn_visit_table.date.dt.year
cn_visit_table['month'] = cn_visit_table.date.dt.month

# head()는 원하는 개수만큼만 보여줌
# print(cn_visit_table.head(10))

# fill_value=0를 하지 않으면 NaN인 데이터들이 하얗게 나오면서 시각화가 제대로 이뤄지지 않는다.
cn_visit_table = cn_visit_table.set_index(['year', 'month'])['visit_count'].unstack(fill_value=0)

# sb.heatmap(cn_visit_table)
# plt.show()