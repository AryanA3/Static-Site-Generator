import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_initialization(self):
        """Test initialization of HTMLNode with given parameters."""
        node = HTMLNode(tag='div', value='Hello, World!', childern=[], props={'class': 'container', 'id': 'main'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello, World!')
        self.assertEqual(node.childern, [])
        self.assertEqual(node.props, {'class': 'container', 'id': 'main'})

    def test_props_to_html(self):
        """Test props_to_html method to ensure it formats properties correctly."""
        node = HTMLNode(tag='div', props={'class': 'container', 'id': 'main'})
        expected_props_html = ' class="container" id="main"'
        self.assertEqual(node.props_to_html(), expected_props_html)

    def test_repr(self):
        """Test the __repr__ method for accurate string representation."""
        node = HTMLNode(tag='span', childern=[], props={'class': 'text'})
        expected_repr = "HTMLNode: tag: span, [], {'class': 'text'}"
        self.assertEqual(repr(node), expected_repr)

if __name__ == '__main__':
    unittest.main()
