from config import CONFIG
import collection
import analyze
import visualize
import pandas as pd
import matplotlib.pyplot as plt

# 공공 API사용
# 1. 출입국관광통계서비스
# 2. 관광자원통계서비스
if __name__ == '__main__':

    resultfiles = dict()

    # collection
    resultfiles['tourspot_visitor'] = \
        collection.crawling_tourspot_visitor(CONFIG['district'], **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collection.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

    # 1. analysis & visualization
    # result_analysis = analyze.analysis_correlation(resultfiles)
    # visualize.graph_scatter(result_analysis)

    # 2. analysis & visualization
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)
    graph_table = pd.DataFrame(result_analysis, columns=['tourspot', 'r_중국', 'r_일본', 'r_미국'])
    graph_table = graph_table.set_index('tourspot')

    graph_table.drop('서울시립미술관 본관')
    graph_table.drop('서울자연사박물관')

    graph_table.plot(kind='bar', rot=60)
    plt.show()