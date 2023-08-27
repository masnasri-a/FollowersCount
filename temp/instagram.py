import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.instagram.com/jkt48.marsha/")
def instagram(url):
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('meta', attrs={'property': 'og:description'})
    result:str = data[0].get('content').split(" ")[0]
    return {
        "followers":result
    }