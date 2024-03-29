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
    
    return router
