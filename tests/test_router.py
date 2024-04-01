import jinja2
import mark_blog
from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()
app = mark_blog.get_blog_app(
    app, jinja2_loader=jinja2.FileSystemLoader("src/mark_blog/templates")
)

client = TestClient(app)


def test_blog_index():
    response = client.get("/blog")
    assert response.status_code == 200
    assert "<title>Evgenii Pochchuev</title>" in response.content.decode()
