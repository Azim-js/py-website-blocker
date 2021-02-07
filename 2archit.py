import time
from datetime import datetime as dt 

hosts_path="C:/Windows/System32/drivers/etc/hosts"
redirect="127.0.0.1"
website_list=["facebook.com","www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,dt.now().hour)<dt(dt.now().year,dt.now().month,dt.now().day,20,56):
        print("working hours")
    else:
        print("fun hours")
    time.sleep(5)            