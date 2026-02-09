from textnode import TextNode, TextType
from markdown_parser import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from markdown_blocks import markdown_to_html_node


def main():
    # node = TextNode(
    #         "This is text with a **bolded** word and **another**", TextType.TEXT
    #     )
    # new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    # print(node)
    # print(new_nodes)

    # matches = extract_markdown_links(
    #         "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
    #     )
    # print(matches)

    # node = TextNode(
    #         "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
    #         TextType.TEXT,
    #     )
    # new_nodes = split_nodes_link([node])
    # print(node)
    # print(new_nodes)

    # text = "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
    # nodes = text_to_textnodes(text)

    # print(text)
    # print(nodes)

    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print("<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>")
    print("-----------------------------------------")
    print(html)

main()
