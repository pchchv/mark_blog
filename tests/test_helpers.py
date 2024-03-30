from mark_blog import helpers


def test_list_published_posts_success():
    posts = helpers.list_posts(posts_dirname="tests/examples/posts")
    assert len(posts) == 19
    assert posts[0]["title"] == "No Tags"
    assert posts[-1]["title"] == "Code, Code, Code"
