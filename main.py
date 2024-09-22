import os.path
import time

from data import *
from post import *


cate_dict = {
    "零食类": "1837417900753129473",
    "日化类": "1837419306700607489",
    "百货类": "1837661072448131073",
    "粮油调味类": "1833784807941050369",
}


def main():
    # 读取excel
    path = "./excel_data/清理后.xlsx"
    excel_data = para_excel(path)

    # 读取保存的图片
    picture_all_path = "./data"
    picture_data = read_picture(picture_all_path)

    # 上传数据
    for s in excel_data[:5]:
        # 重置P
        p = PictureInfo()
        # 序号
        seq = s.seq
        p.store_name = s.store_name

        print(f"开始上传序号{seq}--{p.store_name}数据")
        # 拿到头图路径
        head_image_path = picture_data[seq].head
        head_image_name = os.path.basename(head_image_path)
        # 上传头图到oss
        head_image_resp = post_oss(head_image_name, head_image_path)

        # 拿到轮播图路径
        slider_image_paths = picture_data[seq].banner
        slider_image_resp = []
        for slider_image_path in slider_image_paths:
            slider_image_name = os.path.basename(slider_image_path)
            # 上传轮播图到oss
            slider_image_resp.append(post_oss(slider_image_name, slider_image_path))

        # 组装PictureInfo数据



        if s.cate_id in cate_dict:
            p.cate_id = cate_dict[s.cate_id]
        p.unit_name = s.unit_name
        p.store_info = "简介"  # 简介
        p.slider_image = slider_image_resp
        p.key_word = "测试"
        p.image = [head_image_resp]

        # 上传到后台数据

        res_code, msg = post_picture(p)

        print(f"序号{seq}上传结果：{res_code}, {msg}")


if __name__ == "__main__":
    main()