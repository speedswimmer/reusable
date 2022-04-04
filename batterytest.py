#!/usr/bin/env python3

import time
from datetime import datetime
now = datetime.now()
timestamp = now.strftime('%d-%m-%Y, %H:%M:%S')
count = 0

while True:
        start_time = time.time()
        time.sleep(3)
        uptime = (time.time() - start_time)/3600
        print(uptime)
        with open('/home/pi/Scripts/log.txt', 'a') as f:
                if count == 0:
                        f.write(f'Start: {timestamp}\n')
                        f.write(str(uptime)+'\n')
                else:
                        f.write(str(uptime)+'\n')
                count = count+1
