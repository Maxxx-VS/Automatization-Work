from datetime import datetime
from pobeda import run_pobeda
from time import sleep

run_time = str(input("Введите время запуска: "))

def run_processing():
    while True:
        is_now = datetime.now()
        current_time = is_now.strftime("%H:%M")
        if current_time == run_time:
            run_pobeda()
            sleep(86350)

if __name__ == "__main__":
    run_processing()

