import requests

def get_youtube(username:str):
    response = requests.get(f'https://api.socialcounts.org/youtube-live-subscriber-count/search/{username}')
    json_response = response.json()['items'][0]
    print(json_response)
    return json_response
# https://www.youtube.com/@Ardhianzy
get_youtube("@Ardhianzy")