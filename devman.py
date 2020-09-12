import requests

url = "http://wttr.in/череповец?lang=ru&1"
response = requests.get(url)
response.raise_for_status()
print(response.text)


url = "http://wttr.in/шереметьево?1"
response = requests.get(url)
response.raise_for_status()
print(response.text)


url = "http://wttr.in/лондон?1"
response = requests.get(url)
response.raise_for_status()
print(response.text)
