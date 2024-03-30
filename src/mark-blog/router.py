import pathlib
from typing import Any
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import helpers


def get_router(
    templates: Jinja2Templates,
    favorite_post_ids: set[str] = set()
) -> APIRouter:
    router = APIRouter()

    @router.get("/")
    async def blog_index(request: Request, response_class=HTMLResponse):
        posts = helpers.list_posts()
        recent_3 = posts[:3]

        favorite_posts: list[dict[Any, Any]] = list(
            filter(lambda x: x["slug"] in favorite_post_ids, posts)
        )

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"recent_3": recent_3, "favorite_posts": favorite_posts},
        )

    @router.get("/posts/{post_id}")
    async def blog_post(post_id: str, request: Request, response_class=HTMLResponse):
        post = [
            x for x in filter(lambda x: x["slug"] == post_id, helpers.list_posts())
        ][0]
        content = pathlib.Path(f"posts/{post_id}.md").read_text().split("---")[2]
        post["content"] = helpers.markdown(content)

        return templates.TemplateResponse(
            request=request, name="post.html", context={"post": post}
        )

    return router
