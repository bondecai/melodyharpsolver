import cv2
import matplotlib.pyplot as plt

# hist_b = cv2.calcHist([img_color], [0], None, [256], [0, 256])
# hist_g = cv2.calcHist([img_color], [1], None, [256], [0, 256])
# hist_r = cv2.calcHist([img_color], [2], None, [256], [0, 256])

pink = cv2.imread('colors/pink.png')
yellow = cv2.imread('colors/yellow.png')
light_green = cv2.imread('colors/light_green.png', cv2.IMREAD_GRAYSCALE)
dark_green = cv2.imread('colors/dark_green.png', cv2.IMREAD_GRAYSCALE)
purple = cv2.imread('colors/purple.png', cv2.IMREAD_GRAYSCALE)
dark_blue = cv2.imread('colors/dark_blue.png', cv2.IMREAD_GRAYSCALE)
light_blue = cv2.imread('colors/light_blue.png', cv2.IMREAD_GRAYSCALE)

pink_hist = cv2.calcHist([pink], [0], None, [256], [0,256])
plt.plot(pink_hist)
plt.xlim([0, 256])
plt.show()

yellow_hist = cv2.calcHist([yellow], [0], None, [256], [0,256])
plt.plot(yellow_hist)
plt.xlim([0, 256])
plt.show()
