from fastapi import FastAPI, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

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



@app.get("/posts/{post_id}",include_in_schema=False)
def post_page(request:Request, post_id:int):
    for post in posts:
        if post.get("id")==post_id:
            return  templates.TemplateResponse(request,"post.html",{"post":post})
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Post not found")  



@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/post/{post_id}")
def get_post(post_id:int):
    for post in posts:
        post_id1=post.get("id")
        if post_id==post_id1:
            return post
    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Not Found")


@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request:Request,exception:StarletteHTTPException):
    message=(
        exception.detail 
        if exception.detail 
        else "An error occured. Please check your request and try again."
    )

    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail":message}
        )

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code":exception.status_code,
            "title":exception.status_code,
            "message":message
        },
        status_code=exception.status_code
    )





@app.exception_handler(RequestValidationError)
def validation_exception_handler(request:Request,excepion:RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail":excepion.errors()}
        ) 
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code":status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title":status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message":"Invalid input, please check your request and try again."
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT
    )