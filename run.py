import os
import time
def collect():
    print("Collecting metrics")
    os.system("python collect.py")
starttime = time.time()
while True:
    print("tick")
    collect()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))