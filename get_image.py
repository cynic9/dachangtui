import os
from hashlib import md5
import requests
import re
from requests import codes


# 获取图片地址，标题
def get_images(json):
    if json.get('data'):
        data = json.get('data')
        # 遍历data里的字典，拿到文章标题和图标地址
        for item in data:
            if item.get('image_list') is None:
               continue
            if item.get('title') is None:
               continue
            # 去掉标题里的制表符
            title = re.sub('[\t]', '', item.get('title'))
            images = item.get('image_list')
            for image in images:
                if 'url' not in image.keys():
                    break
                # 使用正则修改图片地址，将小图修改为大图
                large_image = re.sub("list.*?pgc-image", "large/pgc-image", image.get('url'))
                yield {'image': large_image, 'title': title}


def save_images(item):
    img_path = 'img' + '/' + item.get('title')
    # 判断图片文件夹是否已经创建过
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == codes.ok:
            # 设置下载的图片名字，以jpg保存
            file_path = img_path + '/'+'{}.{}'.format(md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print('正在下载图片：%s' % file_path)
            else:
                print('下载过了: %s' % file_path)
    except Exception as e:
        print(e)