# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/20 14:46
# @File:     graphCode.py
# @Software: PyCharm

import pytesseract

from PIL import Image

image = Image.open('images/test1.png')
result = pytesseract.image_to_string(image)
print('未二值化前: %s' % result)  # som k_v

# 二值化处理
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
image.show()
result2 = pytesseract.image_to_string(image)
print('二值化后: %s ' % result2)
