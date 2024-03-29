import yaml
import pathlib
import functools
import markdown as md
from pymdownx import emoji


extensions = [
    "markdown.extensions.tables",
    "toc",  # "markdown.extensions.toc
    # "markdown.extensions.toc",
    "pymdownx.magiclink",
    "pymdownx.betterem",
    "pymdownx.tilde",
    "pymdownx.emoji",
    "pymdownx.tasklist",
    "pymdownx.superfences",
    "pymdownx.saneheaders",
]

extension_configs = {
    "markdown.extensions.toc": {
        "permalink": True,
        "permalink_leading": True,
        "title": "Tabula Rasa",
    },
    "pymdownx.magiclink": {
        "repo_url_shortener": True,
        "repo_url_shorthand": True,
        "provider": "github",
        "user": "facelessuser",
        "repo": "pymdown-extensions",
    },
    "pymdownx.tilde": {"subscript": False},
    "pymdownx.emoji": {
        "emoji_index": emoji.gemoji,
        "emoji_generator": emoji.to_png,
        "alt": "short",
        "options": {
            "attributes": {"align": "absmiddle", "height": "20px", "width": "20px"},
            "image_path": "https://github.githubassets.com/images/icons/emoji/unicode/",
            "non_standard_image_path": "https://github.githubassets.com/images/icons/emoji/",
        },
    },
    "toc": {
        "title": "Table of Contents!",  # Title for the table of contents
        "anchorlink": True,  # Add anchor links to the headers
        "permalink": "# ",  # Add permanent links to the headers
        "permalink_leading": True,  # Add permanent links to the headers
    },
}

markdown = functools.partial(
    md.markdown, extensions=extensions, extension_configs=extension_configs
)


@functools.lru_cache
def list_posts(published: bool = True, posts_dirname="posts") -> list[dict]:
    posts: list[dict] = []
    for post in pathlib.Path(".").glob(f"{posts_dirname}/*.md"):
        raw: str = post.read_text().split("---")[1]
        data: dict = yaml.safe_load(raw)
        data["slug"] = post.stem
        posts.append(data)

    posts = [x for x in filter(lambda x: x["published"] is True, posts)]

    posts.sort(key=lambda x: x["date"], reverse=True)
    return [x for x in filter(lambda x: x["published"] is published, posts)]