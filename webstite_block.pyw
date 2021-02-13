import time
from datetime import datetime as dt 

host_path="C:/Windows/System32/drivers/etc/hosts"
temp_path="C:/Users/azim/Desktop/udemyproject3/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","www.gmail.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours")
        for website in website_list:
            with open(host_path,"r+") as files:
                content=files.read()
                if website in content:
                    pass
                else:
                    files.write(redirect+" "+website+"\n")
    else:
        print("fun hours") 
        with open(host_path,"r+") as files:
            content=files.readlines()
            files.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    files.write(line)
                files.truncate()
    time.sleep(5)               