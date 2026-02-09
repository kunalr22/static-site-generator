import os

from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(entry_path) and entry_path.endswith(".md"):
            dest_path = dest_path[:-3] + ".html"
            generate_page(entry_path, template_path, dest_path, basepath)
        elif os.path.isdir(entry_path):
            generate_pages_recursive(entry_path, template_path, dest_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = get_file_content(from_path)
    title = extract_title(markdown)
    html_nodes = markdown_to_html_node(markdown)

    template = get_file_content(template_path)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_nodes.to_html())
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    write_file_content(dest_path, template)

def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise Exception("No title in markdown.")

def get_file_content(filepath):
    with open(filepath) as f:
        return f.read()
    
def write_file_content(dest_path, content):
    parent_dir = os.path.dirname(dest_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    with open(dest_path, "w") as f:
        f.write(content)