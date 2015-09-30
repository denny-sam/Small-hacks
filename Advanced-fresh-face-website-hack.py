import requests
import time
url="http://api.itimes.com/freshface-contestants-vote/json"
payload={'contestant-id':'55ea97ecd5cc607c5b8b4626',
         'actor':'',
         'city':'pune',
         'platform':'desktop',
         'utoken':''
         }

all_headers={
'User-Agent': 'classes/0.0.1'
}

x=3025

for i in range(14,30):
    time.sleep(i)
    r=requests.post(url,data=payload, headers=all_headers)
    print(r.text)
    x-=1
