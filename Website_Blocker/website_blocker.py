import pandas
import time
from datetime import datetime as dt 

host_path = r"C:\Windows\System32\drivers\etc\hosts"
host_temp = r"C:\Python WS\Python\Website_Blocker\hosts"
redirect = "127.0.0.1"

def blocked_website():
    blocked = list(pandas.read_csv(open("Website_Blocker/blocked_website.csv")))
    return blocked

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 19) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21):
        with open(host_path, 'r+') as host_file:
            content = host_file.read()
            for website in blocked_website():
                if website in content:
                    pass
                else:
                    host_file.write(redirect + " "+ website +"\n")
    else:
        with open(host_path, 'r+') as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_website()):
                    host_file.write(line)
            host_file.truncate()
    time.sleep(5)