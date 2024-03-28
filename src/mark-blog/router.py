from fastapi import APIRouter


def get_router() -> APIRouter:
    router = APIRouter()
    
    @router.get("/")
    def get():
        return "Blog app"
    
    return router
