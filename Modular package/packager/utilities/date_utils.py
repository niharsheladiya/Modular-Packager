import datetime
import time

def get_current():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_difference(d1_str, d2_str):
    d1 = datetime.datetime.strptime(d1_str, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d")
    return abs((d2 - d1).days)

def format_custom(fmt):
    return datetime.datetime.now().strftime(fmt)

def stopwatch():
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    return round(time.time() - start, 2)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i, end=' ', flush=True)
        time.sleep(1)
    print("\nTime's up!")
