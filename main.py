from crawler import bing_image_crawler
from drawcharts import draw_charts
from facedetect import classify
from dbutils import save_data2db
import webbrowser


if __name__ == '__main__':
    keyword = input('请输入爬取的关键字')
    bing_image_crawler(keyword, 100)
    count = classify()
    save_data2db(keyword, count)
    file = draw_charts(keyword, count)
    webbrowser.open(file)
    print("beauty: ",count)