import pyautogui
import os 
from time import sleep

from extract import ext

sleep_big_const = 3
sleep_small_const = 0.5

img_list = ["img/ok.png", "img/cmk.png", "img/reg.png",
            "img/prnt.png", "img/vgr.png", "img/ext.png",
            "img/sav.png", "img/path.png", "img/sav1.png",
            "img/yes.png", "img/ext1.png", "img/file.png", "img/close.png"]

def run_pobeda():
    # запуск exe файла
    os.startfile("C:/OEMZ/Production manager/ProductionManager.exe")
    sleep(sleep_big_const)

    for i in range(len(img_list)):
        buttons = pyautogui.locateAllOnScreen(img_list[i], confidence=0.7)

        if i == 1:
            for button in buttons:
                pyautogui.moveTo(button)
                sleep(sleep_small_const)
                pyautogui.doubleClick(button)
            sleep(sleep_big_const)

        elif i == 5:
            for button in buttons:
                pyautogui.moveTo(button)
                sleep(sleep_small_const + 8)
                pyautogui.click(button)
            sleep(sleep_big_const)

        elif i != 1 and i != 5:
            for button in buttons:
                pyautogui.moveTo(button)
                sleep(sleep_small_const)
                pyautogui.click(button)
            sleep(sleep_big_const)

    ext()


            


