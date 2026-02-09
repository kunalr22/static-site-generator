import os
import sys
from generate_page import generate_pages_recursive
from utils import copy_dir, create_clean_public_dir


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    project_root = os.path.dirname(__file__)
    static_dir = os.path.join(project_root, "..", "static")
    docs_dir = os.path.join(project_root, "..", "docs")
    content_dir = os.path.join(project_root, "..", "content")
    template_path = os.path.join(project_root, "..", "template.html")
    create_clean_public_dir(docs_dir)
    copy_dir(static_dir, docs_dir)
    generate_pages_recursive(content_dir, template_path, docs_dir, basepath)

if __name__ == "__main__":
    main()
