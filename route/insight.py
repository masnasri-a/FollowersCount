from fastapi import APIRouter
from service import get_engagement_tiktok, insight_instagram, insight_facebook, insight_twitter, insight_youtube

app = APIRouter(prefix="/insight")

@app.get("/instagram")
def engagement_instagram(url:str):
    return insight_instagram(url)

@app.get("/tiktok")
def engagement_tiktok(url:str):
    return get_engagement_tiktok(url)

@app.get("/facebook")
def engagement_facebook(url:str):
    return insight_facebook(url)

@app.get("/twitter")
def engagement_twitter(tweetId:str):
    return insight_twitter(tweetId)

@app.get("/youtube")
def engagement_youtube(videoId:str):
    return insight_youtube(videoId)
