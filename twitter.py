import requests

def live_count_twitter(username:str):
    headers = {
        'authority': 'us-central1-tucktools-backend.cloudfunctions.net',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.tucktools.com',
        'referer': 'https://www.tucktools.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    json_data = [
        username
    ]

    response = requests.post(
        'https://us-central1-tucktools-backend.cloudfunctions.net/expressApi/v1/api/twitter',
        headers=headers,
        json=json_data,
    )
    result = response.json()['data'][0]
    template = {
        "name":result['name'],
        "screen_name":result['screen_name'],
        "followers_count":result['followers_count'],
        "friends_count":result['friends_count'],
        "statuses_count":result['statuses_count']
    }
    print(template)

live_count_twitter("ArnoldPoernomo")