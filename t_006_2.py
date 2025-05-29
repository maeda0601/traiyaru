"""
トライやるウィーク用
006_2
"""
from turtle import * #turtleモジュールから全ての関数をインポートする
shape("turtle")
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    forward(200)
    left(144)
done()