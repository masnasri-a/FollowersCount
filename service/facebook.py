from facebook_scraper import get_posts, get_page_info

def insight_facebook(url:str):
    # url = "https://www.facebook.com/jkt48.marsha/posts/pfbid02w3YDn6JUNfA6875dk7hEGQUnDxoNMExyEezDbPR2XKN1tTHJ1aHsrRz9iuV1cQ3Rl"
    detail = None
    for item in get_posts(post_urls=[url], cookies="cookies.txt"):
        detail = item

    temp = {
        "post_text":detail.get("post_text"),
        "like":detail.get("likes"),
        "comments":detail.get("comments"),
        "share":detail.get("shares")
    }
    return temp

def follower_facebook(page_username:str):
    info = get_page_info(page_username, cookies="cookies.txt")
    temp = {
        "name":info.get("Name"),
        "cover_photo":info.get("cover_photo"),
        "profile_picture":info.get("profile_picture"),
        "followers":info.get("followers")
    }
    return temp