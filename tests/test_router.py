import jinja2
import mark_blog
from fastapi import FastAPI


app = FastAPI()
app = mark_blog.get_blog_app(
    app, jinja2_loader=jinja2.FileSystemLoader("src/mark_blog/templates")
)
