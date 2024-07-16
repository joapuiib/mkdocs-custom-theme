import os

from inspect import getfile
from markdown import Markdown
from material.extensions.emoji import _load_twemoji_index
import custom_theme

# Create twemoji index
def twemoji(options: object, md: Markdown):
    paths = options.get("custom_icons", [])[:]

    root = os.path.dirname(getfile(custom_theme))
    root = os.path.join(root, ".icons")

    paths.append(root)
    return _load_twemoji_index(tuple(paths))
