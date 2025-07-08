from crawler import bing_image_crawler
from drawcharts import draw_charts
from facedetect import classify_all as classify
from dbutils import save_data2db
from PyQt6.QtCore import QThread, pyqtSignal
import webbrowser

class WorkerThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, keyword_, window=None):
        super().__init__(window)
        self.keyword_ = keyword_
        self.window = window

    def run(self):

        print("calculate start!")
        keyword = self.keyword_
        bing_image_crawler(keyword, 5, self.window)
        lis = classify(keyword, self.window)
        print("crawler result: ", lis)
        save_data2db(keyword, lis, self.window)
        file = draw_charts(keyword, lis)
        webbrowser.open(file)
        print("result: ",lis)

        self.finished.emit("finished !")