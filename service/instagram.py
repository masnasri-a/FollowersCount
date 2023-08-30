import requests
from bs4 import BeautifulSoup

def insight_instagram(url:str):
    if "instagram.com" not in url:
        url = f"https://www.instagram.com/{url}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    meta_content = soup.find("meta", property="og:description")
    content:str = meta_content.get_attribute_list('content')[0]
    content = content.split(" - ")[0]
    content_splitter = content.split(", ")
    like = content_splitter[0].replace(" likes","")
    comment = content_splitter[1].replace(" comments","").replace("K","000").replace("M","000000").replace(" ","")
    return {
        "likes":like,
        "comment":comment
    }
    
def followers_instagram(url:str):
    if "instagram.com" not in url:
        url = f"https://www.instagram.com/{url}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('meta', attrs={'property': 'og:description'})
    print(data)
    result:str = data[0].get('content').split(" ")[0]
    return {
        "followers":result
    }