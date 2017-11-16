import json

import pandas as pd

with open('../__results__/crawling/일본(130)_foreignvisitor_2017_2017.json', 'r', encoding='utf-8') as infile:
    json_string = infile.read()

# json_data = json.loads(json_string)
# tour_table = pd.DataFrame(json_data, columns=['tourist_spot', 'count_foreigner', 'date'])
# print(tour_table)
#
# tour_table = tour_table.set_index('date')
# print(tour_table)

