import jinja2
from typing import Any
from fastapi import FastAPI, Response
from fastapi.templating import Jinja2Templates

from main import get_blog_app
from router import get_router


__version__ = "0.0.0"