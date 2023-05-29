import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
import copy
def decode(basePx):
    andbw = basePx & 1 
    if  andbw == 1:
        return 1
    else:
        return 0

#prepare to decode
cypherImagePath = './cypher_image.bmp'
cypherImage = cv2.imread(cypherImagePath, 1) 
messageImage = cv2.cvtColor(cypherImage, cv2.COLOR_BGR2GRAY)
images = [copy.deepcopy(cypherImage)]
#decode
for row in range(len(cypherImage)):
    for col in range(len(cypherImage[row])):
        messageImage[row][col] = decode(cypherImage[row][col][2])

messageImage = cv2.normalize(messageImage, dst=None, alpha = 0, beta=255, norm_type=cv2.NORM_MINMAX)
images.append(messageImage)
#print all pic
titles = ["CypherImage", "Message"]
fig = plt.figure(figsize=(200,200))
for i in range(len(images)):
    sub = fig.add_subplot(1,2,i+1)
    sub.set_title(titles[i])
    sub.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB), interpolation="nearest")
plt.show()
