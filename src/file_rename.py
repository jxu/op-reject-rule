# 1.py => 001.py
import os
for filename in os.listdir('.'):
    if filename[-3:] == ".py" and len(filename) < 6:
        os.rename(filename, filename[:-3].zfill(3) + ".py")
        