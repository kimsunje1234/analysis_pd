import analysis_pd.collection.api as pdapi

# test for ps_gen_url
"""
url = pdapi.pd_gen_url(
    "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList",
    # {0:04d}는 0번째 배열의 값을 4자리 int형으로 기본값 0으로 채워라
    YM='{0:04d}{1:02d}'.format(2017, 1),
    SIDO='서울특별시',
    GUNGU='',
    RES_NM='',
    numOfRows=100,
    _type='json',
    pageNo=1
)
print(url)
"""
"""
# test from pd_fetch_tourspot_visitor
for year in range(2017, 2018):
    for month in range(1, 13):
        for item in pdapi.pd_fetch_tourspot_visitor(district1='부산광역시', year=year, month=month):
            print(item)
"""

# test for pd_fetch_foreign_visitor

item = pdapi.pd_fetch_foreign_visitor(country_code=130, year=2017, month=1)
print(item)
