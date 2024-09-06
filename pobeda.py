import pyautogui, os, keyboard
import openpyxl
from time import sleep
loads_coordinate = [(30, 120), (100, 135), (450, 90), (500, 170), (1895, 15)]
# запуск exe файла
os.startfile("C:/OEMZ/Production manager/ProductionManager.exe")
sleep(3)
for i in range(4):
    keyboard.press("enter")
    sleep(2)

# выгрузка excel файла
for i in loads_coordinate:
    pyautogui.click(i)
    sleep(5)

# сохранение файла
keyboard.press("ctrl + s")
sleep(3)

for i in range(4):
    keyboard.press("enter")
    sleep(2)

keyboard.press("left")
sleep(1)
keyboard.press("enter")
