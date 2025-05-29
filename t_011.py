"""
トライやるウィーク用
011
"""
from PIL import Image
import pyocr

pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# pyocrへ利用するOCRエンジンをTesseractに指定する。
tools = pyocr.get_available_tools()
tool = tools[0]

# 画像ファイルのパス
img_path = "test2.jpg"

# 画像ファイルを読み込む
img = Image.open(img_path)
img_g = img.convert('L') #Gray変換

builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img_g, lang="jpn", builder=builder)
print(text)