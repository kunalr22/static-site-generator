import os
from generate_page import generate_pages_recursive
from utils import copy_dir, create_clean_public_dir


def main():
    base_dir = os.path.dirname(__file__)
    static_dir = os.path.join(base_dir, "..", "static")
    public_dir = os.path.join(base_dir, "..", "public")
    content_dir = os.path.join(base_dir, "..", "content")
    template_path = os.path.join(base_dir, "..", "template.html")
    create_clean_public_dir(public_dir)
    copy_dir(static_dir, public_dir)
    generate_pages_recursive(content_dir, template_path, public_dir)

if __name__ == "__main__":
    main()
