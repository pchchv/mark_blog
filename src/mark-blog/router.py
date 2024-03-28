from fastapi import APIRouter
from fastapi.templating import Jinja2Templates


def get_router(
        templates: Jinja2Templates,
        favorite_post_ids: set[str] = set()
) -> APIRouter:
    router = APIRouter()
    
    @router.get("/")
    def get():
        return "Blog app"
    
    return router
