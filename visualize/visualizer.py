import matplotlib.pyplot as plt


def graph_scatter(result_analysis):

    fig, subplots = plt.subplots(1, len(result_analysis), sharey=True)

    # list에서는 인덱스를 뽑아낼 수 없으니 enumerate를 사용!
    for index, result in enumerate(result_analysis):
        subplots[index].set_xlabel('{0}인 입국자수'.format(result['contry_name']))
        # if문을 아래 한줄로 대체
        # if index == 0:
        #     subplots[index].set_ylabel('관광지 입장객 수')
        index == 0 and subplots[index].set_ylabel('관광지 입장객 수')
        subplots[index].set_title('r={: 5f}'.format(result['r']))
        subplots[index].scatter(result['x'], result['y'], edgecolor='none', alpha=0.75, c='black', s=6)

    plt.subplots_adjust(wspace=0)
    plt.show()