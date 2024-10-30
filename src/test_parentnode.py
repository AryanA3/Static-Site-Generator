import unittest
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_no_tag(self):
        """Test that an exception is raised if no tag is provided."""
        with self.assertRaises(ValueError) as context:
            parent = ParentNode()
            parent.to_html()
        self.assertEqual(str(context.exception), 'tag not provided')

    def test_no_children(self):
        """Test that an exception is raised if no children are provided."""
        with self.assertRaises(ValueError) as context:
            parent = ParentNode(tag='div', childern=None)
            parent.to_html()
        self.assertEqual(str(context.exception), 'childern not provided')

    def test_empty_children(self):
        """Test that an exception is raised if children is an empty list."""
        with self.assertRaises(ValueError) as context:
            parent = ParentNode(tag='div', childern=[])
            parent.to_html()
        self.assertEqual(str(context.exception), 'childern not provided')

    def test_render_children(self):
        """Test that the to_html method correctly renders children."""
        child1 = LeafNode(tag='p', value='Hello')
        child2 = LeafNode(tag='span', value='World')
        parent = ParentNode(tag='div', childern=[child1, child2])
        
        expected_html = '<div><p>Hello</p><span>World</span></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_nested_children(self):
        """Test that the to_html method works with nested children."""
        child1 = LeafNode(tag='p', value='Hello')
        child2 = ParentNode(tag='section', childern=[LeafNode(tag='span', value='World')])
        parent = ParentNode(tag='div', childern=[child1, child2])
        
        expected_html = '<div><p>Hello</p><section><span>World</span></section></div>'
        self.assertEqual(parent.to_html(), expected_html)

