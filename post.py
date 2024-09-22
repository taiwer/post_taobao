import time

import requests
import json

from openpyxl.styles.builtins import total


# 上传图片的信息
class PictureInfo:
    def __init__(self,
                 # store_name,  # 商品名称
                 # cate_id,  # 分类id
                 # unit_name,  # 单位
                 # store_info,  # 简介
                 # slider_image,  # 轮播图--传list
                 # key_word,  # 关键字
                 # image  # 主图--传list
                 ):
        self.store_name = ""
        self.cate_id = ""
        self.unit_name = ""
        self.store_info = ""
        self.slider_image = []
        self.key_word = ""
        self.image = ""


def post_oss(img_name, img_path):
    url = "https://withisland.com/prod-api/system/oss/upload"

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxIiwicm5TdHIiOiJFd0FROVc3ejJjV3RxMFcyaGM3MEZPb1hQNFpOZU1vMyJ9.4Lb2apOQ6A3z4pS5QhRtItLQDrS7SIE0g4l0KPjfKI0",
        "Connection": "keep-alive",
        "Cookie": "Admin-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxIiwicm5TdHIiOiJFd0FROVc3ejJjV3RxMFcyaGM3MEZPb1hQNFpOZU1vMyJ9.4Lb2apOQ6A3z4pS5QhRtItLQDrS7SIE0g4l0KPjfKI0; sidebarStatus=0",
        "Origin": "https://withisland.com",
        "Referer": "https://withisland.com/product/storeProduct",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        "sec-ch-ua": "^\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\"Windows\""
    }

    files = {
        'file': (img_name, open(img_path, 'rb'), 'image/png')
    }

    response = requests.post(url, headers=headers, files=files)

    image_dic = {
        "ossId": "",
        "url": ""
    }

    if response.status_code == 200:
        print("oss上传成功")
        res_json = response.json()
        if res_json.get("code") == 200:
            image_dic["ossId"] = res_json.get("data").get("ossId")
            image_dic["url"] = res_json.get("data").get("url")

    return image_dic


def get_update():
    url = "https://withisland.com/prod-api/product/storeProduct/list"
    params = {
        'pageNum': 1,
        'pageSize': 10
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxIiwicm5TdHIiOiJFd0FROVc3ejJjV3RxMFcyaGM3MEZPb1hQNFpOZU1vMyJ9.4Lb2apOQ6A3z4pS5QhRtItLQDrS7SIE0g4l0KPjfKI0',
        'Connection': 'keep-alive',
        'Content-Language': 'zh_CN',
        'Cookie': 'Admin-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxIiwicm5TdHIiOiJFd0FROVc3ejJjV3RxMFcyaGM3MEZPb1hQNFpOZU1vMyJ9.4Lb2apOQ6A3z4pS5QhRtItLQDrS7SIE0g4l0KPjfKI0; sidebarStatus=0',
        'Referer': 'https://withisland.com/product/storeProduct',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'sec-ch-ua': '^"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^"Windows"^'
    }

    response = requests.get(url, params=params, headers=headers)

    res_json = response.json()

    total_num = res_json.get("total")

    print(f"当前商品{total_num}个")


def post_picture(s: PictureInfo):
    url = "https://withisland.com/prod-api/product/storeProduct"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxIiwicm5TdHIiOiJFd0FROVc3ejJjV3RxMFcyaGM3MEZPb1hQNFpOZU1vMyJ9.4Lb2apOQ6A3z4pS5QhRtItLQDrS7SIE0g4l0KPjfKI0",
        "Connection": "keep-alive",
        "Content-Language": "zh_CN",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "Admin-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxIiwicm5TdHIiOiJFd0FROVc3ejJjV3RxMFcyaGM3MEZPb1hQNFpOZU1vMyJ9.4Lb2apOQ6A3z4pS5QhRtItLQDrS7SIE0g4l0KPjfKI0; sidebarStatus=0",
        "Origin": "https://withisland.com",
        "Referer": "https://withisland.com/product/storeProduct",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        "sec-ch-ua": "^\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\"Windows\""
    }

    data = {
        "storeName": s.store_name,
        "cateId": s.cate_id,
        "unitName": s.unit_name,
        "storeInfo": s.store_info,
        "sliderImage": s.slider_image,
        "specType": 0,
        "isIntegral": 0,
        "isSub": 0,
        "isShow": 1,
        "isHot": 1,
        "isBenefit": 1,
        "isBest": 1,
        "isNew": 1,
        "header": [],
        "keyword": s.key_word,
        "image": s.image,
        "attrs": [
            {
                "imageArr": [],
                "pic": "",
                "price": 1,
                "cost": 0,
                "otPrice": 0,
                "stock": 1,
                "seckillStock": 0,
                "seckillSrice": 0,
                "pinkStock": 0,
                "pinkPrice": 0,
                "barCode": "",
                "weight": 0,
                "volume": 0,
                "brokerage": 0,
                "brokerageTwo": 0,
                "integral": 0
            }
        ],
        "items": []
    }

    response = requests.post(url, headers=headers, json=data)

    res_json = response.json()

    msg = res_json.get("msg")

    get_update()

    return response.status_code, msg


if __name__ == "__main__":
    get_update()