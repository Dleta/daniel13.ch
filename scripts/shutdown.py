import os
import time

t=input("in how mutche seconds shouold your pc shutdown: ")
t=int(t)
time.sleep(t)
os.system("shutdown /s /t 1")
