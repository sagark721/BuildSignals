from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()



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
        "content":"Python is great for webd development",
        "date_posted":"November 16,2026"


    }
]



@app.get("/",response_class=HTMLResponse,include_in_schema=False)
def home():
    return f"<h1> Ganapati Bappa Moraya!!! </h1>"

@app.get("/api/posts")
def get_posts():
    return posts