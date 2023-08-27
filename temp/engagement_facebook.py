from facebook_scraper import get_posts
import json
url = "https://www.facebook.com/jkt48.marsha/posts/pfbid02w3YDn6JUNfA6875dk7hEGQUnDxoNMExyEezDbPR2XKN1tTHJ1aHsrRz9iuV1cQ3Rl"
detail = None
for item in get_posts(post_urls=[url], cookies="cookies.txt"):
    detail = item

temp = {
    "post_text":detail.get("post_text"),
    "like":detail.get("likes"),
    "comments":detail.get("comments"),
    "share":detail.get("shares")
}
print(temp)