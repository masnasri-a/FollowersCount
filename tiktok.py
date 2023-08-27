import requests
from bs4 import BeautifulSoup

url = "https://www.tiktok.com/@megleticia"
def tiktok(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('strong', attrs={'title': 'Followers'})
    return {
        "followers":data.text
    }



