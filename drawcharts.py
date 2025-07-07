from pyecharts.charts import Bar
from pyecharts import options as opts

def draw_charts(keyword, y_axis):
    """
    画柱状图
    :param keyword: 关键字
    :param y_axis: y轴数据
    :return: 生成的网页
    """
    # 不习惯链式调用的开发者依旧可以单独调用方法
    bar = Bar()  # 创建一个柱状图对象
    # 添加x轴
    bar.add_xaxis(['无人脸', '1', '2', '3', '4',
                   '5', '6', '7', '8', '9', '10'])
    # 添加y轴
    bar.add_yaxis(keyword, y_axis)

    # 设置标题
    bar.set_global_opts(title_opts=opts.TitleOpts(title="颜值分布"))

    file_name = '颜值分布.html'
    # 生成网页,参数为网页名称
    bar.render(file_name)
    return file_name