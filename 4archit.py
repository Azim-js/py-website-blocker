import time 
from datetime import datetime as dt 

temp_path="hosts"
host_path="C:/Windows/System32/drivers/etc/hosts"

redirect="127.0.0.1"
website_list=["www.facebook.com","www.gmail.com","google.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt(dt.now().year,dt.now().month,dt.now().day,7):
        print("working hours")
        with open(temp_path,"r+") as files:
            content=files.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    files.write(redirect+" "+website+"\n")
    else:
        print("fun hours")   
        with open(temp_path,"r+") as files:
            content=files.readlines()
            files.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    files.write(line)
                files.truncate() 
    time.sleep(5)                

