import cv2
import pyautogui
import numpy as np
import time
import keyboard
import pickle

# Run this program
# Go to your minecraft (make sure you are not in full screen mode AKA be in windowed fullscreen)
# Open any song from Melody's harp and begin playing
# Before the first note appears, press 'y' on your keyboard
# Check to see if screen.png has correcty captured your minecraft
# Now draw a rectangle enclosing ONLY the row of blocks where you would click notes

while True:
    if keyboard.is_pressed('y'):
        # Capture the screenshot
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Save the screenshot
        cv2.imwrite('screen.png', screenshot)
        print('Screenshot saved.')
        time.sleep(0.2)  # Add a small delay to prevent multiple captures from one key press
        break
cv2.destroyAllWindows()

position_list = []
try:
    with open('positions', 'rb') as f:
        position_list = pickle.load(f)
except:
    position_list = []

top_left_corner=[]
bottom_right_corner=[]
def draw_rect(action, x, y, flags, *userdata):
    # Referencing global variables 
    global top_left_corner, bottom_right_corner
    # Mark the top left corner when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        top_left_corner = [x,y]
        # When left mouse button is released, mark bottom right corner
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_right_corner = [x,y]  
        position_list.append([top_left_corner, bottom_right_corner]) 
        # Draw the rectangle
    elif action == cv2.EVENT_RBUTTONDOWN:
        for i in range(len(position_list)):
            x1_pos, y1_pos = position_list[i][0]
            x2_pos, y2_pos = position_list[i][1]
            if x > x1_pos and x < x2_pos and y > y1_pos and y < y2_pos:
                position_list.pop(i)

    with open('positions', 'wb') as f:
        pickle.dump(position_list, f)

def checkSpaces():
    gray_im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for pos in position_list:
        cropped_im = gray_im[pos[0][1]:pos[1][1], pos[0][0]:pos[1][0]]
        cv2.rectangle(image, pos[0], pos[1], (0,255,0), 2, 8)
        
image = cv2.imread('screen.png')
temp = image.copy()
cv2.namedWindow('meow')

k = 0
# Close the window when key q is pressed
while k!=113:
    image = cv2.imread('screen.png')
    checkSpaces()
    # Display the image
    cv2.imshow("meow", image)
    cv2.setMouseCallback('meow', draw_rect)
    k = cv2.waitKey(1)

cv2.destroyAllWindows()
