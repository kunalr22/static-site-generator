import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_neq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_neq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_eq_link(self):
        node = TextNode("This is a text node", TextType.BOLD, "a.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "a.com")
        self.assertEqual(node, node2)

    def test_neq_link(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "a.com")
        self.assertNotEqual(node, node2)
    
    def test_neq_all(self):
        node = TextNode("This is a text node", TextType.BOLD, "a.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, "b.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()