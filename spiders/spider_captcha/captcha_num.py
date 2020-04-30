try:
    from PIL import Image
except:
    import Image

import requests
import pytesseract

from os import path

# 根据脚本位置,自行设定基本路径
BASE_PATH = path.dirname(path.dirname(path.abspath(__file__)))


def save_image():
    response = requests.get('http://shanghai.chinatax.gov.cn/newxbwz/servlet/GetshowimgSmall')
    IMAGE_PATH = path.join(BASE_PATH, 'images')
    with open(IMAGE_PATH + '\match.jpg', 'wb') as f:
        f.write(response.content)


def handler(grays, threshold=120):
    """
    对灰度图片进行二值化处理
    默认阈值为160，可根据实际情况调整
    """
    table = []
    for i in range(256):
        table.append(0) if i < threshold else table.append(1)
    anti = grays.point(table, '1')
    return anti


def test_result():
    # 保存在本地的验证码图片路径
    test_image = path.join(BASE_PATH, 'images\match.jpg')
    # 图片灰度处理
    gray = Image.open(test_image).convert('L')
    # 图片二值化处理
    image = handler(gray)
    image.show()
    # 使用pytesseract库识别验证码中的字符饼打印
    print(pytesseract.image_to_string(test_image))


if __name__ == '__main__':
    """
    该脚本用来测试pytesseract库对于简单图形验证码识别,
    因该验证码有一定倾斜度，
    经测验后,基本识别不了,可以弃用了。。。
    """
    save_image()
    test_result()
