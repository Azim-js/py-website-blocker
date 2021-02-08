import time
from datetime import datetime as dt 

temp_path="hosts"
host_path="C:/Windows/System32/drivers/etc/hosts"

redirect="127.0.0.1"
website_lists=["www.facebook.com","facebook.com"]

#requests from local computer to internet 
#commiting changes to hosts file leads to blocking of website

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13)<dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours")
        with open(temp_path,'r+') as files:
            content=files.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    files.write(redirect+" "+website+"\n")
    else:
        print("fun hours")
    time.sleep(5)                     
