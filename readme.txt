注意事项：
    1.图片不要上传，只传代码，数据库和配置文件
    2.如果因使用加速器导致了无法push或pull，尝试设置git代理
    git config --global http.proxy 127.0.0.1:[你的加速器端口]
    git config --global https.proxy 127.0.0.1:[你的加速器端口]
    取消配置的方法如下：
    git config --global --unset http.proxy
    git config --global --unset https.proxy
    如果还不行：
    尝试通过下面的配置关闭ssl证书检验：
    git config --global http.sslVerify false

软件依赖：
    pyecharts:2.08
    icrawler:0.6.10
    baidu-aip:4.16.13
    chardet:5.2.0
    PyQt6:6.7.1

使用方法：
    在主函数main.py中点击运行即可

创新点：
    1. 首次获取的数据表记录会进行insert；重复插入数据表记录会进行update
    2. 对于滚转角，俯仰角，偏航角超过30度的人脸进行筛除，只保留正脸
    3. 获取了三种不同的信息：脸型，颜值，年龄
    4. 对整个项目进行模块化重构，耦合性大大降低，便于维护和添加功能
    5. 采用PyQt6添加了窗口小程序，优化操作体验

TODO：
    1.采用接口方式进行进一步模块化
    2.丰富窗体的打印信息
    3.完善图表
    4.增加所分析的数据广度，如：对某一人群的爬取与统计
    5.优化运算速度