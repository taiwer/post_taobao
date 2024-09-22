import pandas as pd
import os


class Item:
    def __init__(self):
        # 序号
        self.seq = ""
        # 商品名称
        self.store_name = ""
        # 规格
        self.quality = ""
        # 单位
        self.unit_name = ""
        # 分类
        self.cate_id = ""
        # 价格
        self.price = ""


class Picture:
    def __init__(self):
        # 头图
        self.head = ""
        # 轮播图
        self.banner = []
        # 详情图
        self.detail = []


def para_excel(path_in):
    df = pd.read_excel(path_in, dtype=str)
    df.fillna("", inplace=True)

    item_all = []
    for row in df.iterrows():
        if row[1].iloc[0] == "":
            continue
        item = Item()
        item.seq = row[1].iloc[0]
        item.store_name = row[1].iloc[1]
        item.quality = row[1].iloc[2]
        item.unit_name = row[1].iloc[3]
        item.cate_id = row[1].iloc[4]
        item.price = row[1].iloc[6]
        item_all.append(item)

    return item_all



def read_picture(picture_all_path):
    data_path = picture_all_path
    dic_list = os.listdir(data_path)

    res_all = {}

    for dic in dic_list:
        # 判断是不是文件夹
        if not os.path.isdir(os.path.join(data_path, dic)):
            continue
        sub_list = os.listdir(os.path.join(data_path, dic))
        # 转数值排序
        sub_list = sorted(sub_list, key=lambda x: int(x))
        for sub in sub_list:

            picture = Picture()
            item_path = os.path.join(data_path, dic, sub)
            item_path_list = os.listdir(item_path)

            for item in item_path_list:

                if item == "头图":
                    item_head_path = os.path.join(item_path, item)
                    head_list = os.listdir(item_head_path)
                    if len(head_list) > 0:
                        picture.head = os.path.join(item_head_path, head_list[0])

                if item == "详情图":
                    item_detail_path = os.path.join(item_path, item)
                    detail_list = os.listdir(item_detail_path)
                    detail_lists = [os.path.join(item_detail_path, i) for i in detail_list if i.endswith(".png")]
                    if len(detail_list) > 0:
                        picture.detail = detail_lists

                if item == "轮播图":
                    item_banner_path = os.path.join(item_path, item)
                    banner_list = os.listdir(item_banner_path)
                    banner_lists = [os.path.join(item_banner_path, i) for i in banner_list if i.endswith(".png")]
                    if len(banner_list) > 0:
                        picture.banner = banner_lists

            if len(picture.head) == 0:
                print("error: {}缺少头图".format(item_path))

            if len(picture.banner) == 0:
                print("error: {}缺少轮播图".format(item_path))

            if len(picture.detail) == 0:
                print("error: {}缺少详情图".format(item_path))

            res_all.update({sub: picture})

    return res_all


if __name__ == "__main__":
    # path = "./excel_data/清理后.xlsx"
    # para_excel(path)
    read_picture(r"E:\taobao\下载")
    # read_picture(r"./data")
