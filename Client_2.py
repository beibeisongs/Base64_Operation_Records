# encoding=utf-8
# Date: 2018-09-13
# Author: MJUZY
# Reference:
#   https://blog.csdn.net/u013517229/article/details/81132008
#
# Reference:
#   solve the UnicodeDecodeError by "解决方法2" in the following URL page
#   https://www.cnblogs.com/mengyu/p/6638975.html
#
# Reference:
#   another good reference:
#   https://blog.csdn.net/dcrmg/article/details/80542665


import base64
import cv2
import numpy as np


if __name__ == "__main__":

    with open("kkk.jpeg", 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode("utf-8")
        print("data: image/jpeg; base64, %s" % s)

    base64_data_bytes = s.encode("utf-8")
    base64_decode = base64.b64decode(base64_data_bytes)

    img_array = np.fromstring(base64_decode, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)

    cv2.imwrite("kkk2.jpeg", img)
