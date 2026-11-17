from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")



posts:list[dict] =[
    {
        "id":1,
        "author":"Sagar Kanade",
        "title":"FastAPI is awesome",
        "content":"This framework is really easy to use",
        "date_posted":"November 15,2026"

    },
    {
        "id":2,
        "author":"Prashant Kanade",
        "title":"Python is great",
        "content":"Python is great for web development",
        "date_posted":"November 16,2026"


    }
]



@app.get("/",include_in_schema=False,name="home")
@app.get("/posts",include_in_schema=False,name="posts")
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts,"title":"Home"},)

@app.get("/api/posts")
def get_posts():
    return posts