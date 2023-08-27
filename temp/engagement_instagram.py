
# 
url = 'https://www.instagram.com/p/CvWz049h_47/'
import requests
from bs4 import BeautifulSoup

def get_instagram_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    meta_content = soup.find("meta", property="og:description")
    content:str = meta_content.get_attribute_list('content')[0]
    content = content.split(" - ")[0]
    content_splitter = content.split(", ")
    like = content_splitter[0].replace(" likes","")
    # like = like.replace("K","000").replace("M","000000").replace(" ","").replace(",","")

    comment = content_splitter[1].replace(" comments","").replace("K","000").replace("M","000000").replace(" ","")
    return {
        "likes":like,
        "comment":comment
    }
    

# Contoh penggunaan:
likes = get_instagram_likes(url)