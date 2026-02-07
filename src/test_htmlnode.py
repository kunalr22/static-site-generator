import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_props(self):
        node = HTMLNode(
            tag="a", 
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            })
        node2 = HTMLNode(
            tag="a", 
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            })
        self.assertEqual(node.props_to_html(), node2.props_to_html())
        
    def test_eq_no_props(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_neq_props(self):
        node = HTMLNode(
            tag="a", 
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            })
        node2 = HTMLNode(
            tag="a", 
            props={
                "href": "https://www.apple.com",
            })
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())
