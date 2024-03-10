import cv2
import keyboard
import time
import pyautogui
import numpy as np
import pickle

def template_match():
    main_image = cv2.imread('harpwithwhite.png', cv2.IMREAD_GRAYSCALE)
    template = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

    result = cv2.matchTemplate(main_image, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    thresh = 0.99996417760849
    print(max_val)
    if max_val >= thresh:

        top_left = max_loc
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
        cv2.rectangle(main_image, top_left, bottom_right, 0, 5)
        center_x = max_loc[0] + template.shape[1] // 2
        center_y = max_loc[1] + template.shape[0] // 2
        pyautogui.click(center_x, center_y)
        print(center_x, center_y)

    cv2.imshow('Matched Region', main_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# template_match()

def melodysolver():
    position_list = []
    with open('positions', 'rb') as f:
        position_list = pickle.load(f)
    region = (position_list[0][0][0], position_list[0][0][1], position_list[0][1][0]-position_list[0][0][0], position_list[0][1][1]-position_list[0][0][1])
    # print(region)
    template = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
    while True:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # thresh = 0.99996417760849
        # if max_val >= thresh:
            # print('meow')
            # top_left = max_loc
            # bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
            # cv2.rectangle(main_image, top_left, bottom_right, 0, 5)
        if max_val >= 0.99:
            center_x = max_loc[0] + template.shape[1] // 2
            center_y = max_loc[1] + template.shape[0] // 2
            pyautogui.moveto(center_x, center_y)
            # print(center_x, center_y)
            pyautogui.click()
            # pyautogui.press('q')
            pyautogui.moveTo(400,400)
            # time.sleep(0.05)
        if keyboard.is_pressed('z'):
            break

    cv2.destroyAllWindows()

melodysolver()

# position_list = []

# with open('positions', 'rb') as f:
#     position_list = pickle.load(f)

# print(position_list)

# region = (position_list[0][0][0], position_list[0][0][1], position_list[0][1][0]-position_list[0][0][0], position_list[0][1][1]-position_list[0][0][1])
# print(region)

# while True:
#     if keyboard.is_pressed('y'):
#         # Capture the screenshot
#         screenshot = pyautogui.screenshot(region=region)
#         screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
#         # Save the screenshot
#         cv2.imwrite('test.png', screenshot)
#         print('Screenshot saved.')
#         time.sleep(0.2)  # Add a small delay to prevent multiple captures from one key press
#     elif keyboard.is_pressed('q'):
#         break

# cv2.destroyAllWindows()
