import os
import cv2


path = r"F:\Programy\CrowdCounter\data\images_mirrored"

items = os.listdir(path)


for item in items:
    img = cv2.imread(os.path.join(path, item))
    flip = cv2.flip(img, 1)
    cv2.imwrite(item, flip)
