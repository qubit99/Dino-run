
import webbrowser
from PIL import ImageGrab, ImageOps
import pyautogui
import numpy as np
import time


def getImg():
    im = ImageGrab.grab(bbox=(732, 476, 803, 522))
    bw_im = ImageOps.grayscale(im)
    a = np.array(bw_im)
    s = a.sum()
    # print(s)
    return(s)



if __name__ == "__main__":
    webbrowser.open_new("https://elgoog.im/t-rex/?bot")
    time.sleep(3)
    pyautogui.click(x=892, y=594, button='left')
    time.sleep(1)
    pyautogui.press('space')
    while(True):
        val = getImg()
        if val != 806702:
            pyautogui.keyDown('up')
        
