import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
import copy
def encode(basePx,toHidePx):
    lastBit_basePx = basePx % 2 
    # 0 dark 1 bright
    if toHidePx == 1 and lastBit_basePx == 0:
            if basePx - 1 < 0:
                return 1
            else:
                return -1
    elif toHidePx == 0 and lastBit_basePx == 1:
            if basePx - 1 < 0:
                return 1
            else:
                return -1
    return 0

#prepare to encode
baseImagePath = './base_image.jpg'
toHidePath = './to_hide.jpg' #must be 2 level pic
baseImage = cv2.imread(baseImagePath, 1) 
toHideImage = cv2.imread(toHidePath, 0)
cypherImage = copy.deepcopy(baseImage)
baseImgHeight,baseImgWidth = baseImage.shape[:2]
toHideImage = copy.deepcopy(cv2.resize(toHideImage,(baseImgWidth, baseImgHeight)))
images = [copy.deepcopy(baseImage), copy.deepcopy(toHideImage)]
toHideImage = np.uint8(toHideImage/128)

#encode
for row in range(len(baseImage)):
    for col in range(len(baseImage[row])):
        cypherImage[row][col][2] += encode(baseImage[row][col][2], toHideImage[row][col]) 


images.append(cypherImage)
cv2.imwrite('./cypher_image.bmp',cypherImage)

#print all pic
titles = ["BaseImage", "toHideImage", "CypherImage", "decodeImage"]
fig = plt.figure(figsize=(200,200))
for i in range(len(images)):
    sub = fig.add_subplot(1,3,i+1)
    sub.set_title(titles[i])
    sub.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB), interpolation="nearest")
plt.show()
