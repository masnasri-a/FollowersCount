import requests

def get_proxy():
    # response = requests.get("https://api.getproxylist.com//proxy?apiKey=62e9cf6f693a1701c2ba9497f712fb048064bc46&country=ID&protocol=http")
    # json_response = response.json()
    # print(json_response)
    proxies = {
        'http': f'128.199.202.122:8080',
        # 'https': f'http://{json_response["ip"]}:{json_response["port"]}',
    }
    print(proxies)
    return proxies