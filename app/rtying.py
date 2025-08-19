import requests


try:
    r = requests.get("https://dsadsad.ai/67afcdeb-261a-4729-be43-001de2435923")
except requests.exceptions.RequestException as e:
    print(e)
