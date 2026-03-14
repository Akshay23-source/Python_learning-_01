import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)




import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data)



import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

joke = response.json()

print(joke["setup"])
print(joke["punchline"])




