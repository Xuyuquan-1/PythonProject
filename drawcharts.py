from pyecharts.commons.utils import JsCode

from select_data import select_AgeBdata
from select_data import select_FaceBdata
from select_data import select_Beautydata

from pyecharts import options as opts
from pyecharts.charts import Scatter, Pie, Page, Radar


def draw_charts(rows_AgeB,rows_Shape,rows_Beauty):

    """
    画散点图
    :param rows: 列表套元组，每个人的数据是一个元组对象
    :return: 生成的网页
    """
    # 准备散点图数据
    ages = []  # x轴数据：平均年龄
    beauties = []  # y轴数据：平均颜值
    keywords = []  # 标签数据：关键词

    # 从查询结果中提取数据
    for row in rows_AgeB:
        keywords.append(row[0])  # 第一列：关键词
        ages.append(row[1])  # 第二列：平均年龄
        beauties.append(row[2])  # 第三列：平均颜值

    # 创建散点图
    scatter = (
        Scatter()
        .add_xaxis(ages)  # x轴：年龄数据列表
        .add_yaxis(
            "颜值分布",
            beauties,  # y轴：颜值数据列表
            symbol_size=10,
            label_opts=opts.LabelOpts(is_show=False),

            # 添加工具提示，显示关键词
            tooltip_opts=opts.TooltipOpts(
                formatter=JsCode(
                    "function(params) {"
                    "   return '姓名: ' + keywords[params.dataIndex] + '<br/>'"
                    "          + '平均年龄: ' + params.value[0].toFixed(1) + '<br/>'"
                    "          + '平均颜值: ' + params.value[1].toFixed(1);"
                    "}"
                )
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="年龄与颜值关系分析"),
            xaxis_opts=opts.AxisOpts(
                name="平均年龄",
                name_location="end",
                type_="value"
            ),
            yaxis_opts=opts.AxisOpts(
                name="平均颜值",
                name_location="end",
                type_="value"
            ),
            tooltip_opts=opts.TooltipOpts(trigger="item"),
            visualmap_opts=opts.VisualMapOpts(
                dimension=1,  # 根据颜值分数着色
                min_=min(beauties),
                max_=max(beauties),
                range_color=['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61',
                             '#f46d43', '#d73027', '#a50026']
            )
        )
    )

    # 在JavaScript中传递关键词列表
    scatter.add_js_funcs(f"var keywords = {keywords};")

    scatter.chart_id='ac768466652c467387ca0f0843ea1e9f'


    # 饼图

    data = []
    for row in rows_Shape:
        shape = row[0]  # 第一个字段是keyword
        count = row[1]  # 第二个字段是shape值
        data.append((shape, count))

    # 创建饼图
    pie = (
        Pie()
        .add(
            "",  # 系列名称
            data,  # 使用实际数据库数据
            radius=["40%", "75%"],  # 内外半径比例
            center=["50%", "50%"]  # 饼图位置
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="脸型分布分析",  # 更符合内容的标题
                subtitle="基于数据库实际数据",
                pos_left="center"
            ),
            legend_opts=opts.LegendOpts(
                orient="vertical",
                pos_top="15%",
                pos_left="2%",
                type_="scroll"  # 添加滚动条防止项目过多
            ),
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(
                formatter="{b}: {c} ({d}%)",  # 显示名称、值、百分比
                font_size=12
            ),
            tooltip_opts=opts.TooltipOpts(
                formatter="{b}: {c} <br/>占比: {d}%"
            )
        )
    )

    pie.chart_id='3e3b9d9744df4dbfbea1f8f5c57877f7'



    # 创建一个网页对象
    page = Page(layout=Page.DraggablePageLayout)  # 参数为可拖拽
    # 把统计添加到一个网页中，如果有多张图可以一直添加
    page.add(scatter, pie)
    # 生成网页
    page.render('charts.html')
    # 加载JSON数据，重新改变布局
    page.save_resize_html(
        source='charts.html',  # 原来的网页
        cfg_file='chart_config.json',  # JSON文件
        dest='charts.html'  # 新生成的布局网页
    )

    return 'charts.html'




if __name__ == '__main__':
    rows1 = select_AgeBdata()
    rows2 = select_FaceBdata()
    file = draw_charts(rows1,rows2)

