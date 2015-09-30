
import requests
import time
import random

url="http://api.itimes.com/freshface-contestants-vote/json"
payload={'contestant-id':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
         'actor':'',
         'city':'pune',
         'platform':'desktop',
         'utoken':''
         }

all_headers={
'User-Agent': 'classes/0.0.1'
}

x=3025

for i in range(x):
    i=random.randrange(14,80)
    time.sleep(i)
    r=requests.post(url,data=payload, headers=all_headers)
    print(r.text)
    x-=1
