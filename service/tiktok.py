import requests
from bs4 import BeautifulSoup

# url = "https://www.tiktok.com/@megleticia"

def followers_tiktok(url):
    if 'www.tiktok.com' not in url:
        url = "https://www.tiktok.com/"+url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('strong', attrs={'title': 'Followers'})
    return {
        "followers":data.text
    }


def get_engagement_tiktok(url:str):
    if 'www.tiktok.com' not in url:
        url = "https://www.tiktok.com/"+url
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('meta', attrs={'name': 'description'})
    content:str = data.get_attribute_list('content')[0]
    splitter = content.split(". ")[0].split(", ")
    print(splitter)
    likes = splitter[0].replace(" Likes","")
    comments = splitter[1].replace(" Comments","") 
    return {
        "likes":likes,
        "comment":comments
    }