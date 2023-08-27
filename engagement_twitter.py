# import snscrape.modules.twitter as sntwitter
# from snscrape.modules.twitter import TwitterTweetScraperMode

# # data =twitter.TwitterTweetScraper(tweetId="1695751168813637642",mode=TwitterTweetScraperMode.SINGLE)
# # print(data.get_items())
# for i, data in enumerate(sntwitter.TwitterTweetScraper("1695751168813637642").get_items()):
#     print(data)

import requests

url = "https://cdn.syndication.twimg.com/tweet-result"

querystring = {"id":"1695751168813637642","lang":"id"}

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://platform.twitter.com",
    "Connection": "keep-alive",
    "Referer": "https://platform.twitter.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)