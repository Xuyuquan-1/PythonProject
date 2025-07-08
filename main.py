from crawler import bing_image_crawler
from drawcharts import draw_charts
from facedetect import classify_all as classify
from dbutils import save_data2db
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit
)
from qtwindow import CalculatorApp
import webbrowser
import sys


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # window = CalculatorApp()
    # sys.exit(app.exec())

    keyword = input('请输入爬取的关键字')
    bing_image_crawler(keyword, 5)
    count = classify()
    save_data2db(keyword, count)
    file = draw_charts(keyword, count)
    webbrowser.open(file)
    print("beauty: ",count)