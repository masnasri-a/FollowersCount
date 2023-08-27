import requests
from bs4 import BeautifulSoup


def get_engagement_tiktok(url:str):
    print(url)
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('meta', attrs={'name': 'description'})
    content:str = data.get_attribute_list('content')[0]
    splitter = content.split(". ")[0].split(", ")
    likes = splitter[0].replace(" Likes","")
    comments = splitter[1].replace(" Comments","") 
    return {
        "likes":likes,
        "comment":comments
    }

# engagement_tiktok("https://www.tiktok.com/@achietns/video/7271501094428200198")