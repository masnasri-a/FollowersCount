
# 
url = 'https://www.instagram.com/p/CvWz049h_47/'
# url = 'https://www.instagram.com/jkt48.marsha/'
from lxml import etree
import requests
from bs4 import BeautifulSoup

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# dom = etree.HTML(str(soup))
# print(dom.selector('#mount_0_0_6Y > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > section > main > div._aa6b._ad9f._aa6d > div._aa6e > article > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div._ae2s._ae3v._ae3w > section._ae5m._ae5n._ae5o > div > div > span > a > span > span'))


def get_instagram_likes(url):
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