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
    param_list = ['beauty','age','face_shape']
    options = {'face_field': param_list[0]+','+param_list[1]+','+param_list[2]}
    json = client.detect(base, 'BASE64', options)
    return json

# 返回胭脂平均值，年龄平均值，出现最多的脸型
def classify_all():
    root_dir = 'bing_img'
    file_list = os.listdir(root_dir)
    print(file_list)

    res = {'beauty':None, 'age': None, 'face_shape':None}
    temp_beau = [0,0,0,0,0,0,0,0,0,0,0]
    temp_age = []
    temp_face = {}

    for i in file_list:
        path = root_dir + '/' + i
        print(path)

        if os.path.isfile(path):
            base = get_file_content(path)
            json = detect_face(base)
            # print(json)

            lis = parse_json(json)



            if lis == -1 or (face_filter(json) == False):
                dic = root_dir + '/' + '-1'
            else:
                temp_beau[lis['beauty']] += 1
                temp_age.append(lis['age'])
                temp_face[lis['face_shape']['type']] = temp_face.get(lis['face_shape']['type'], 0) + 1
                dic = root_dir + '/' + str(lis['beauty'])

            if not os.path.exists(dic):
                os.makedirs(dic)
            os.rename(path, dic + '/' + i)

    res['beauty'] = temp_beau
    res['age'] = sum(temp_age) / len(temp_age) if temp_age else 0
    res['face_shape'] = max(temp_face, key=temp_face.get) if temp_face else None
    print("res: ",res)
    return res

def face_filter(json):
    # 1.通过欧拉角筛选侧脸
    # 滚转角，俯仰角，偏航角
    roll  = json['result']['face_list'][0]['angle']['roll']
    pitch = json['result']['face_list'][0]['angle']['pitch']
    yaw   = json['result']['face_list'][0]['angle']['yaw']
    if (roll>30 or roll < -30) or (pitch > 30 or pitch < -30) or (yaw > 30 or yaw < -30):
        return False
    return True



def parse_json(json):
    code = json['error_code']

    list_dic = {'beauty': None,'age': None, 'face_shape' :None}


    if code == 0:
        list_dic['beauty'] = int(json['result']['face_list'][0]['beauty']/10)+1
        list_dic['age'] = int(json['result']['face_list'][0]['age'])
        list_dic['face_shape'] = json['result']['face_list'][0]['face_shape']
    else:
        return -1
    # print("list_dic :",list_dic)
    return list_dic




if __name__ == '__main__':
    keyword = input('请输入爬取的关键字')
    list = bing_image_crawler(keyword, 10)
    result = classify_all()
    print("result:",result)