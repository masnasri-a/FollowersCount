import requests
from bs4 import BeautifulSoup

url = "https://www.tiktok.com/@megleticia"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find('strong', attrs={'title': 'Followers'})
print(data.text)



