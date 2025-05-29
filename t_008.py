"""
トライやるウィーク用
008
ここで3時間分
pyautoguiのインストール
pillowのインストールが必要
"""
import pyautogui
import time

time.sleep(5)
for i in range(1):
    c = 'picture' + str(i) + '.jpg'
    photo = pyautogui.screenshot(region=(770, 431, 320, 25))
    photo.save(c)
