import base64
from matplotlib import figure
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from io import BytesIO




def get_image():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph


def get_simple_plot(chart_type, title="Grafik Çıktısı", *args, **kwargs):
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(11, 4))
    # fig, ax = plt.subplots()
    x = kwargs.get("x")
    y = kwargs.get("y")
    data = kwargs.get("data")
    if chart_type == "bar grafik":    # Bar grafik 
        plt.title(title)
        plt.xticks(rotation=45)  # 45 / 'vertical'
        plt.yticks(rotation=45)  # 45 / 'vertical'
        barWidth = 0.25
        br1 = np.arange(len(x))
        br2 = [x - barWidth for x in br1]
        br3 = [x + 2*barWidth for x in br2]
        # fig = plt.subplots(figsize =(12, 4))
        plt.bar(br1, data["bugunkuVaka"], color ='r', width = barWidth,  edgecolor ='grey', label ='Vaka')
        plt.bar(br2, data["bugunkuTest"], color ='g', width = barWidth,  edgecolor ='grey', label ='Test')
        plt.bar(br3, data["bugunkuIyilesen"], color ='b', width = barWidth,  edgecolor ='grey', label ='İyileşen')
        # ax.bar_label(ax.containers[2])
        # fig(plt.bar_label(plt.containers[2]))
        plt.xticks([r for r in range(len(x))], list(x))
        plt.legend()
        # data[['bugunkuIyilesen','bugunkuTest']].plot(x=x, kind="bar")
        # plt.bar(x, data)
        # plt.bar(x, y=data["bugunkuVaka", "bugunkuTest"])
        # data.plot(x=x, y=["bugunkuVaka", "bugunkuTest"], kind="bar", )
 
    elif chart_type == "çizgi grafik":
        plt.title(title)
        plt.xticks(rotation=45)  # 45 / 'vertical'
        plt.yticks(rotation=45)  # 45 / 'vertical'
        
        plt.plot(x, y)
    else:
        plt.title(title)
        plt.xticks(rotation='vertical')  # 45 / 
        sns.countplot("bugunkuVefat", data=data)

    plt.tight_layout()

    graph = get_image()
    return graph

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip