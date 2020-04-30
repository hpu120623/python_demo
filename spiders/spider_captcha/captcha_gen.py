from captcha.image import ImageCaptcha  # pip install spider_captcha
from PIL import Image
import random
import time
from spiders.spider_captcha.captcha_setting import *
import os


def random_captcha():
    captcha_text = []
    for i in range(MAX_CAPTCHA):
        c = random.choice(ALL_CHAR_SET)
        captcha_text.append(c)
    return ''.join(captcha_text)


# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha()
    captcha_text = random_captcha()
    captcha_image = Image.open(image.generate(captcha_text))
    return captcha_text, captcha_image


if __name__ == '__main__':
    count = 3
    path = TRAIN_DATASET_PATH  # 通过改变此处目录，以生成 训练、测试和预测用的验证码集
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(count):
        text, image = gen_captcha_text_and_image()
        filename = text + '.png'
        image.save(path + os.path.sep + filename)
        print('saved %d : %s' % (i + 1, filename))
