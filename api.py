from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import uvicorn

from route import followers_route, insight_route


app = FastAPI()


@app.get("/", include_in_schema=False)
def redirect():
    return RedirectResponse("/docs")


app.include_router(followers_route, tags=['followers'])
app.include_router(insight_route, tags=['insight'])

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=5051, workers=3)
