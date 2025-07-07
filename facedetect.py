from aip import AipFace
import base64
from crawler import bing_image_crawler
import os

APP_ID = '16966840'
API_KEY = 'B0e6QoxUB0gwQxxzWT6fCgMU'
SECRET_KEY = 'rGQji0R0X76e4CP9rbcdPbcNRdS6EwC9'

keyword = ''
def get_file_content(file_path):
    file = open(file_path , 'rb')
    data = file.read()
    content = base64.b64encode(data)
    file.close()
    base = content.decode('utf-8')
    return base

def detect_face(base):
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    options = {'face_field': 'beauty'}
    json = client.detect(base, 'BASE64', options)
    return json

def classify():
    root_dir = 'bing_img'
    file_list = os.listdir(root_dir)
    print(file_list)

    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in file_list:
        path = root_dir + '/' + i
        print(path)

        if os.path.isfile(path):
            base = get_file_content(path)
            json = detect_face(base)
            beauty = parse_json(json)



            if beauty == -1:
                count[0] += 1
            else:
                count[beauty] += 1
            dic = root_dir + '/' + str(beauty)
            if not os.path.exists(dic):
                os.makedirs(dic)
            os.rename(path, dic + '/' + i)
    return count

def parse_json(json)->int:
    code = json['error_code']
    if code == 0:
        beauty = int(json['result']['face_list'][0]['beauty']/10)+1
    else:
        beauty = -1
    return beauty


if __name__ == '__main__':
    keyword = input('请输入爬取的关键字')
    bing_image_crawler(keyword, 100)
    # base = get_file_content('./bing_img/000002.jpg')
    # json = detect_face(base)
    # beauty = parse_json(json)
    # print(beauty)
    count = classify()
    print("beauty: ",count)