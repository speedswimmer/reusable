#!/usr/bin/env python3
import time
from datetime import datetime
import sys

now = datetime.now()
timestamp = now.strftime("%d-%m-%Y, %H:%M:%S")
count = 0
start_time = time.time()

while True:
    try:
        uptime = round((time.time() - start_time)/3600,4)
        print(uptime)
        with open ('log.txt', 'a') as f:
            if count == 0:
                f.write(f'Battery test start: {timestamp}\n')
                f.write(str(uptime) + '\n')
            else:
                f.write(str(uptime) + '\n')
            count = count + 1
        time.sleep(300)
    except KeyboardInterrupt:
        print('[script stopped...]')
        sys.exit(0)
