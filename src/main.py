from textnode import TextNode, TextType

def main():
    print("hello world")
    test = TextNode("This is some anchor test", TextType.TEXT_LINK, "https://www.boot.dev")
    print(test)

main()
