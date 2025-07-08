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
