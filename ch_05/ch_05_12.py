import os

print os.path.exists('/etc/passwd')
print os.path.isfile('ch_05_11.py')
print os.path.isdir('ch_05_11.py')
print os.path.islink('ch_05_11.py')
print os.path.realpath('ch_05_11.py')
print os.path.getsize('ch_05_11.py')
print os.path.getmtime('ch_05_11.py')

import time

print time.ctime(os.path.getmtime('ch_05_11.py'))