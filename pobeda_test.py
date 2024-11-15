import pyautogui, os, keyboard
from time import sleep

from extract import ext


loads_coordinate = [(900, 625), (25, 155), (135, 170), (450, 90), (500, 170), (1895, 15)]
loads_command = ["enter","enter","enter","enter","left","enter"]
password = ['1','0','3','1','3','7','3']

def run():
    # запуск exe файла
    os.startfile("C:/OEMZ/Production manager/ProductionManager.exe")
    sleep(3)

    # выгрузка excel файла
    for c in loads_coordinate:
        pyautogui.moveTo(c)
        sleep(1)
        pyautogui.click(c)
        sleep(3)

    # сохранение файла
    sleep(7)
    keyboard.press("ctrl + s")
    sleep(3)

    for l in loads_command:
        keyboard.press(l)
        sleep(2)

    ext()

if __name__ == "__main__":
    run()
