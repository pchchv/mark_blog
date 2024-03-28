from typing import Any
from fastapi import FastAPI

from router import get_router


def get_blog_app(
    app: FastAPI,
    prefix: str | None = "blog",
    favorite_post_ids: set[str] = set(),
) -> FastAPI:
    # Router controls
    router = get_router(favorite_post_ids=favorite_post_ids)
    router_kwargs: dict[str, Any] = {"router": router, "tags": ["blog"]}
    if prefix is not None:
        router_kwargs["prefix"] = f"/{prefix}"
    app.include_router(**router_kwargs)

    return app
