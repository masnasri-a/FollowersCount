import requests

def engagement_youtube_views(code:str):
    url = f"https://api.socialcounts.org/youtube-video-live-view-count/{code}"
    response = requests.get(url)
    detail_url = f"https://api.socialcounts.org/youtube-video-live-view-count/search/{code}"
    detail_response = requests.get(detail_url)
    counter = response.json()
    detail = detail_response.json()['items'][0]
    template = {
        "title": detail['title'],
        "views":counter['est_sub'],
        "like":counter['table'][0]['count']
    }
    return template

engagement_youtube_views("2HwP1VzYn28")