# Configuration file for the Sphinx documentation builder.
import os

from src.__metadata__ import __project__ as project
from src.__metadata__ import __version__ as version

# -- Environmental Data ------------------------------------------------------


# -- Project information -----------------------------------------------------
project = project
author = "Jolt Org"
release = os.getenv("_PYTHON-REDDIT_DOCS_BUILD_VERSION", version.rsplit(".")[0])
copyright = "2023, Python Reddit"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_toolbox.collapse",
    "sphinx_design",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
PY_CLASS = "py:class"
PY_RE = r"py:.*"
PY_METH = "py:meth"
PY_ATTR = "py:attr"
PY_OBJ = "py:obj"

nitpicky = True
nitpick_ignore = [
    # external library / undocumented external
    (PY_CLASS, "ExternalType"),
    (PY_CLASS, "TypeEngine"),
    (PY_CLASS, "UserDefinedType"),
    (PY_CLASS, "_types.TypeDecorator"),
    (PY_METH, "_types.TypeDecorator.process_bind_param"),
    (PY_METH, "_types.TypeDecorator.process_result_value"),
    (PY_METH, "type_engine"),
    # type vars and aliases / intentionally undocumented
    (PY_CLASS, "CollectionT"),
    (PY_CLASS, "EmptyType"),
    (PY_CLASS, "ModelT"),
    (PY_CLASS, "T"),
    (PY_CLASS, "AsyncSession"),
    (PY_CLASS, "Select"),
]
nitpick_ignore_regex = [
]

napoleon_google_docstring = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_attr_annotations = True

autoclass_content = "class"
autodoc_class_signature = "separated"
autodoc_default_options = {"special-members": "__init__", "show-inheritance": True, "members": True}
autodoc_member_order = "bysource"
autodoc_typehints_format = "short"
autodoc_type_aliases = {"FilterTypes": "FilterTypes"}

autosectionlabel_prefix_document = True

todo_include_todos = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Style configuration -----------------------------------------------------
html_theme = "shibuya"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_show_sourcelink = True
html_title = "Docs"
html_favicon = "_static/logo.png"
html_logo = "_static/logo.png"
html_context = {
    "source_type": "github",
    "source_user": "python-reddit",
    "source_repo": project.replace("_", "-"),
}

brand_colors = {
    "--brand-primary": {"rgb": "75, 139, 190", "hex": "#4b8bbe"},
    "--brand-secondary": {"rgb": "255, 232, 115", "hex": "#ffe873"},
    "--brand-dark-blue": {"rgb": "48, 105, 152", "hex": "#306998"},
    "--brand-yellow": {"rgb": "255, 212, 59", "hex": "#ffd43b"},
    "--brand-dark": {"rgb": "100, 100, 100", "hex": "#646464"},
    "--brand-light": {"rgb": "235, 221, 221", "hex": "#ebdddd"},
}


html_theme_options = {
    "logo_target": "/",
    "announcement": "This documentation is currently under development.",
    "github_url": "https://github.com/python-reddit/python",
    "nav_links": [
        {"title": "Home", "url": "https://python-reddit.github.io/python"},
        {"title": "Docs", "url": "https://python-reddit.github.io/python"},
        {"title": "Code", "url": "https://github.com/python-reddit/python"},
    ],
    "light_css_variables": {
        # RGB
        "--sy-rc-theme": brand_colors["--brand-primary"]["rgb"],
        "--sy-rc-text": brand_colors["--brand-primary"]["rgb"],
        "--sy-rc-invert": brand_colors["--brand-primary"]["rgb"],
        # "--sy-rc-bg": brand_colors["--brand-secondary"]["rgb"],
        # Hex
        "--sy-c-link": brand_colors["--brand-secondary"]["hex"],
        # "--sy-c-foot-bg": "#191919",
        "--sy-c-foot-divider": brand_colors["--brand-primary"]["hex"],
        "--sy-c-foot-text": brand_colors["--brand-dark"]["hex"],
        "--sy-c-bold": brand_colors["--brand-primary"]["hex"],
        "--sy-c-heading": brand_colors["--brand-primary"]["hex"],
        "--sy-c-text-weak": brand_colors["--brand-primary"]["hex"],
        "--sy-c-text": brand_colors["--brand-dark"]["hex"],
        "--sy-c-bg-weak": brand_colors["--brand-dark"]["rgb"],
    },
    "dark_css_variables": {
        # RGB
        "--sy-rc-theme": brand_colors["--brand-primary"]["rgb"],
        "--sy-rc-text": brand_colors["--brand-primary"]["rgb"],
        "--sy-rc-invert": brand_colors["--brand-primary"]["rgb"],
        "--sy-rc-bg": brand_colors["--brand-dark"]["rgb"],
        # Hex
        "--sy-c-link": brand_colors["--brand-primary"]["hex"],
        "--sy-c-foot-bg": brand_colors["--brand-dark"]["hex"],
        "--sy-c-foot-divider": brand_colors["--brand-primary"]["hex"],
        "--sy-c-foot-text": brand_colors["--brand-light"]["hex"],
        "--sy-c-bold": brand_colors["--brand-primary"]["hex"],
        "--sy-c-heading": brand_colors["--brand-primary"]["hex"],
        "--sy-c-text-weak": brand_colors["--brand-primary"]["hex"],
        "--sy-c-text": brand_colors["--brand-light"]["hex"],
        "--sy-c-bg-weak": brand_colors["--brand-dark"]["hex"],
        "--sy-c-bg": brand_colors["--brand-primary"]["hex"],
    },
}
