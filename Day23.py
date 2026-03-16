import requests

url = "https://example.com"

response = requests.get(url)

print(response.text)


from bs4 import BeautifulSoup
import requests

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)




for link in soup.find_all("a"):
    print(link.get("href"))
    
    
    
    
    
    
    for heading in soup.find_all("h1"):
    print(heading.text)