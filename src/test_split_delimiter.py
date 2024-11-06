from textnode import *
import unittest
from utils import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_single_delimiter(self):
        """Test case for a single delimiter in the text."""
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        
        self.assertEqual(new_nodes, expected_nodes)

    def test_no_delimiter(self):
        """Test case when there is no delimiter in the text."""
        node = TextNode("This is some regular text", TextType.TEXT)
        
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected_nodes = [
            TextNode("This is some regular text", TextType.TEXT),
        ]
        
        self.assertEqual(new_nodes, expected_nodes)

    def test_delimiter_at_start(self):
        """Test case when the delimiter is at the start of the text."""
        node = TextNode("`code block` here is text", TextType.TEXT)
        
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected_nodes = [
            TextNode("code block", TextType.CODE),
            TextNode(" here is text", TextType.TEXT),
        ]
        
        self.assertEqual(new_nodes, expected_nodes)

    def test_delimiter_at_end(self):
        """Test case when the delimiter is at the end of the text."""
        node = TextNode("Here is text with a `code block`", TextType.TEXT)
        
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected_nodes = [
            TextNode("Here is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ]

        self.assertEqual(new_nodes, expected_nodes)

