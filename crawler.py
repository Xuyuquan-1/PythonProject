from icrawler.builtin import BingImageCrawler
import os
import shutil

def bing_image_crawler(keyword, max_num):
    dic = "bing_img"
    if os.path.exists(dic):
        shutil.rmtree(dic)

    bing_crawler = BingImageCrawler(
        feeder_threads = 1,
        parser_threads = 2,
        downloader_threads = 4,
        storage = {'root_dir': dic}
    )
    bing_crawler.crawl(keyword=keyword, max_num=max_num)

if __name__ == '__main__':
    keyword = input('请输入爬取的关键字')
    bing_image_crawler(keyword, 100)
