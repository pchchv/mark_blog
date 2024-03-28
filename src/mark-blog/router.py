from fastapi import APIRouter


def get_router(favorite_post_ids: set[str] = set()) -> APIRouter:
    router = APIRouter()
    
    @router.get("/")
    def get():
        return "Blog app"
    
    return router
