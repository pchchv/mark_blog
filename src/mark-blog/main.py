from typing import Any
from fastapi import FastAPI
from router import get_router


app = blog_app(FastAPI())


def blog_app(
        app: FastAPI,
        prefix: str | None = "blog",
) -> FastAPI:
    router = get_router()
    router_kwargs: dict[str, Any] = {"router": router, "tags": ["blog"]}

    if prefix is not None:
        router_kwargs["prefix"] = f"/{prefix}"
    app.include_router(**router_kwargs)

    return app
