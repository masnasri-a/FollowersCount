from fastapi import APIRouter
from service import followers_tiktok, followers_instagram, subscriber_youtube, follower_facebook, follower_twitter
app = APIRouter(prefix="/followers")


@app.get("/instagram")
def follow_instagram(url: str):
    return followers_instagram(url)


@app.get("/tiktok")
def follower_tiktok(url: str):
    return followers_tiktok(url)


@app.get("/youtube")
def followers_youtube(username: str):
    return subscriber_youtube(username)


@app.get("/facebook")
def followers_facebook(url: str):
    return follower_facebook(url)


@app.get("/twitter")
def followers_twitter(username: str):
    return follower_twitter(username)
