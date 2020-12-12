import subprocess
import time
from datetime import date

schedule = [date(2020, 12, 13), date(2020, 12, 14), date(2020, 12, 15), date(2020, 12, 16),
            date(2020, 12, 17),
            date(2020, 12, 18), date(2020, 12, 19), date(2020, 12, 23), date(2020, 12, 27), date(2020, 12, 28),
            date(2020, 12, 29), date(2020, 12, 30),
            date(2020, 12, 31), date(2020, 1, 1), date(2020, 1, 2), date(2020, 1, 3), date(2020, 1, 5),
            date(2020, 1, 6), date(2020, 1, 7), date(2020, 1, 8), date(2020, 1, 9)]


def commit():
    process = subprocess.run('./commit.sh', shell=True, check=True, timeout=100)



print("Program started ...")
while len(schedule) > 0:
    for date in schedule:
        if date == date.today():
            for i in range(0, 3):
                file = open("./dummy.txt", "a")
                time.sleep(2)
                print("File opened")
                file.write("Git Art Made by python script running on rasp-pi-zero!\n")
                time.sleep(2)
                file.close()
                print("File Overwritten")
                time.sleep(4)
                print("Committed")
                commit()
                time.sleep(10)
            print("Committed on", date.today())
            schedule.remove(date)
    time.sleep(86400)

