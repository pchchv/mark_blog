import jinja2

from typing import Any
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from router import get_router


def get_blog_app(
    app: FastAPI,
    prefix: str | None = "blog",
    favorite_post_ids: set[str] = set(),
    jinja2_loader: jinja2.BaseLoader = jinja2.PackageLoader(
        "mark_blog", "templates"
    ),
    jinja2_extensions: set[str] = {
        "jinja2_time.TimeExtension",
        "jinja2.ext.debug",
    },
    mount_statics: bool = True,
) -> FastAPI:
    env = jinja2.Environment(
        loader=jinja2_loader,
        extensions=list(jinja2_extensions),
    )
    templates = Jinja2Templates(env=env)

    # Router controls
    router = get_router(templates=templates, favorite_post_ids=favorite_post_ids)
    router_kwargs: dict[str, Any] = {"router": router, "tags": ["blog"]}
    if prefix is not None:
        router_kwargs["prefix"] = f"/{prefix}"
    app.include_router(**router_kwargs)

    return app
