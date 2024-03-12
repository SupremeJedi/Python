import os
from datetime import datetime
os.chdir(r'C:\Users\saksh\Documents')
mod_time=os.stat('d.PNG').st_mtime
print(datetime.fromtimestamp(mod_time))
#print(os.listdir())
