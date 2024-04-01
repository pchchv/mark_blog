import pathlib
from mark_blog import helpers


def test_list_published_posts_success():
    posts = helpers.list_posts(posts_dirname="tests/examples/posts")
    assert len(posts) == 19
    assert posts[0]["title"] == "No Tags"
    assert posts[-1]["title"] == "Code, Code, Code"


def test_list_published_posts_failure():
    posts = helpers.list_posts(posts_dirname="blarg")
    assert len(posts) == 0


def test_load_markdown_content_success():
    path = pathlib.Path("tests/examples/posts/2024-02-fitness.md")
    page = helpers.load_markdown_content(path)
    assert page["metadata"]["title"] == "My training plans"
    assert "My training plans" in page["metadata"]["title"]
    assert (
        "Weight loss and training for marathon and bike trips."
        in page["metadata"]["description"]
    )
