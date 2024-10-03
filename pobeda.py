
import pyautogui, os, keyboard
from time import sleep

from extract import ext

loads_coordinate = [(25, 120), (100, 135), (450, 90), (500, 170), (1895, 15)]

def run():
    # запуск exe файла
    os.startfile("C:/OEMZ/Production manager/ProductionManager.exe")
    sleep(3)

    # авторизация в победе
    for i in range(3):
        keyboard.press("enter")
        sleep(3)

    # выгрузка excel файла
    sleep(1)
    for i in loads_coordinate:
        pyautogui.click(i)
        sleep(3)

    # сохранение файла
    sleep(4)
    keyboard.press("ctrl + s")
    sleep(3)

    for i in range(4):
        keyboard.press("enter")
        sleep(2)

    keyboard.press("left")
    sleep(1)
    keyboard.press("enter")
    sleep(2)

    ext()


if __name__ == "__main__":
    run()
