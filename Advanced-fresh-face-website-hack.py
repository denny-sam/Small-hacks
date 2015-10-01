
import requests
import time
import random

def randomToken():
    alpha=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    a=[]
    for l in range(10):
        a.append(random.choice(alpha))
    rn=random.randrange(11111,88888)
    rn=str(rn)
    rn=list(rn)
    upper=''
    for h in range(5,len(a)):
        upper+=str(a[h]).upper()

    upper=list(upper)
    token=a[:5]+rn+upper

    jumble=''
    while token:
        pos=random.randrange(len(token))
        jumble+=str(token[pos])
        token=token[:pos]+token[(pos+1):]

    return jumble


url="http://api.itimes.com/freshface-contestants-vote/json"
payload={'contestant-id':'55ea97ecd5cc607c5b8b4626',
         'actor':'',
         'city':'pune',
         'platform':'desktop',
         'utoken':''
         }

all_headers={
'User-Agent': 'Mozilla/0.0.1'
}

x=3025

for i in range(x):
    token=randomToken()
    payload['utoken']=token
    i=random.randrange(60,107)
    time.sleep(i)
    r=requests.post(url,data=payload, headers=all_headers)
    print(token,r.text)
    x-=1
