"""
トライやるウィーク用
013
"""
import os
from PIL import Image
import pyocr
import pyautogui
import time

pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# pyocrへ利用するOCRエンジンをTesseractに指定する。
tools = pyocr.get_available_tools()
tool = tools[0]

time.sleep(5)
# 1000にしているけどある程度大きかったらOK
for i in range(1000):
    c = 'picture' + str(i) + '.jpg'
    # ↓(705,649)から(1169,684)の場合を例にしています。
    photo = pyautogui.screenshot(region=(770, 431, 320, 25))  # 先ほど取得した位置を入力(左上のX、左上のY、Xの幅、Yの幅)
    photo.save(c)

    img = Image.open(c)
    d = 'complete_picture' + str(i) + '.jpg'
    img = img.convert('RGB')
    size = img.size
    img2 = Image.new('RGB', size)

    border = 110

    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b = img.getpixel((x, y))
            if r < border or g < border or b < border:
                r = 0
                g = 10
                b = 0
            img2.putpixel((x, y), (r, g, b))

    img2.save(d)

    im = Image.open(d)


    def add_margin(pil_img, top, right, bottom, left, color):
        width, height = pil_img.size
        new_width = width + right + left
        new_height = height + top + bottom
        result = Image.new(pil_img.mode, (new_width, new_height), color)
        result.paste(pil_img, (left, top))
        return result


    new_resize = 'new_resize' + str(i) + '.jpg'

    im_new = add_margin(im, 35, 35, 50, 50, (0, 0, 0))
    im_new.save(new_resize, quality=95)

    img3 = Image.open(new_resize)

    builder = pyocr.builders.TextBuilder(tesseract_layout=3)
    text = tool.image_to_string(img3, lang="eng", builder=builder)
    pyautogui.typewrite(text)
    os.remove(c)