import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('yy.jpg')
img.shape
img.dtype
plt.figure()
imgplot = plt.imshow(img)

plt.figure()
lum_img = img[:, :, 0]
imgplot = plt.imshow(lum_img)
# plt.figure()
# imgplot = plt.imshow(lum_img)
# imgplot.set_clim(0.0, 0.7)



plt.figure()
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('hot')

plt.figure()
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0,0.7)

plt.show()