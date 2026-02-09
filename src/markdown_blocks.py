from enum import Enum

from markdown_parser import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block.strip() != "":
            filtered_blocks.append(block.strip())
    return filtered_blocks

def block_to_block_type(block: str):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        for i in range(1,len(lines)+1):
            if not lines[i-1].startswith(f"{i}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    div_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                refined_block = block.replace("\n", " ")
                child_nodes = markdown_to_leaf_nodes(refined_block)
                div_children.append(ParentNode("p", child_nodes))
            case BlockType.HEADING:
                heading_level = heading_level_counter(block)
                refined_block = strip_block_type_identifier(block, block_type)
                child_nodes = markdown_to_leaf_nodes(refined_block)
                div_children.append(ParentNode(f"h{heading_level}", child_nodes))
            case BlockType.CODE:
                refined_block = strip_block_type_identifier(block, block_type)
                code_node = LeafNode("code", refined_block)
                div_children.append(ParentNode("pre", [code_node]))
            case BlockType.QUOTE:
                refined_block = strip_block_type_identifier(block, block_type)
                child_nodes = markdown_to_leaf_nodes(refined_block)
                div_children.append(ParentNode("blockquote", child_nodes))
            case BlockType.UNORDERED_LIST:
                refined_block = strip_block_type_identifier(block, block_type)
                list_children = []
                list_items = refined_block.split("\n")
                for item in list_items:
                    item_children = markdown_to_leaf_nodes(item)
                    list_children.append(ParentNode("li", item_children))
                div_children.append(ParentNode("ul", list_children))
            case BlockType.ORDERED_LIST:
                refined_block = strip_block_type_identifier(block, block_type)
                list_children = []
                list_items = refined_block.split("\n")
                for item in list_items:
                    item_children = markdown_to_leaf_nodes(item)
                    list_children.append(ParentNode("li", item_children))
                div_children.append(ParentNode("ol", list_children))
    return ParentNode("div", div_children)



def strip_block_type_identifier(block, block_type):
    match block_type:
        case BlockType.HEADING:
            space_index = block.find(" ")
            return block[space_index + 1 :]
        case BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                if line.startswith("> "):
                    new_lines.append(line[2:])
                else:
                    new_lines.append(line)
            return " ".join(new_lines)
        case BlockType.CODE:
            lines = block.split("\n")
            return "\n".join(lines[1:-1]) + "\n"
        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                if line.startswith("- ") or line.startswith("* "):
                    new_lines.append(line[2:])
                else:
                    new_lines.append(line)
            return "\n".join(new_lines)
        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                dot_index = line.find(". ")
                if dot_index != -1:
                    new_lines.append(line[dot_index + 2 :])
                else:
                    new_lines.append(line)
            return "\n".join(new_lines)
        case _:
            return block

def markdown_to_leaf_nodes(markdown):
    text_nodes = text_to_textnodes(markdown)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def heading_level_counter(text):
    count = 0
    for c in text:
        if c == "#":
            count += 1
        else:
            break
    return count