from PIL import Image
import numpy as np

# 元となる画像の読み込み
img = Image.open('original.bmp')
#オリジナル画像の幅と高さを取得
width, height = img.size
# オリジナル画像と同じサイズのImageオブジェクトを作成する
img2 = Image.new('RGB', (width, height))

img_pixels = []
for y in range(height):
  for x in range(width):
    # getpixel((x,y))で左からx番目,上からy番目のピクセルの色を取得し、img_pixelsに追加する
    img_pixels.append(img.getpixel((x,y)))
# あとで計算しやすいようにnumpyのarrayに変換しておく
img_pixels=np.array(img_pixels)

img_pixels
