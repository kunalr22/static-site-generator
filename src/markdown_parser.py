import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("Invalid Markdown Syntax: Unclosed delimiter")
        for i, section in enumerate(split_node):
            if section == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(section, node.text_type))
                continue
            new_nodes.append(TextNode(section, text_type))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for alt, url in images:
            split_text = text.split(f"![{alt}]({url})", 1)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = split_text[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes
        

def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for anchor_text, url in links:
            split_text = text.split(f"[{anchor_text}]({url})", 1)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            text = split_text[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def text_to_textnodes(text):
    res = [TextNode(text, TextType.TEXT)]
    delimiters = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}
    for delimiter in delimiters:
        res = split_nodes_delimiter(res, delimiter, delimiters[delimiter])
    res = split_nodes_image(res)
    res = split_nodes_link(res)
    return res
