from fastapi import FastAPI
import uvicorn
from instagram import instagram
from tiktok import tiktok
from engagement_instagram import get_instagram_likes
from engagement_tiktok import get_engagement_tiktok

app = FastAPI()


@app.get("/followers/instagram")
def followers_instagram(url:str):
    return instagram(url)

@app.get("/followers/tiktok")
def followers_tiktok(url:str):
    return tiktok(url)

@app.get("/engagement/instagram")
def engagement_instagram(url:str):
    return get_instagram_likes(url)

@app.get("/engagement/tiktok")
def engagement_tiktok(url:str):
    return get_engagement_tiktok(url)

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)