import cv2
import pyautogui
import numpy as np
import time
import keyboard
import pickle
import cProfile

# pink, yellow, light green, dark green, purple, dark blue, light blue, 

def main():
    position_list = []
    try:
        with open('positions', 'rb') as f:
            position_list = pickle.load(f)
    except:
        position_list = []

    template = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
    # time.sleep(5)
    while True:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
        for pos in position_list:
            cropped_img = screenshot[pos[0][1]:pos[1][1], pos[0][0]:pos[1][0]]
            res = cv2.matchTemplate(cropped_img, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val >= 0.9:
                center_x = pos[0][0] + ((pos[1][0] - pos[0][0]) // 2)
                center_y = pos[0][1] + ((pos[1][1] - pos[0][1]) // 2)
                pyautogui.moveTo(center_x, center_y)
                pyautogui.click()
                pyautogui.moveTo(950,585)
        if keyboard.is_pressed('z'):
            break

    cv2.destroyAllWindows()

main()
