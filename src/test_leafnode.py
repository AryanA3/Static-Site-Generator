import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html_with_tag_and_value(self):
        node = LeafNode(tag='p', value='Hello, World!', props={'class': 'text'})
        expected_output = '<p class="text">Hello, World!</p>'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_without_tag(self):
        node = LeafNode(value='Just some text')
        expected_output = 'Just some text'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_without_value_raises_value_error(self):
        node = LeafNode(tag='p', value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_without_tag_and_no_value_raises_value_error(self):
        node = LeafNode(tag=None, value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_no_props(self):
        node = LeafNode(tag='div', value='Content')
        expected_output = '<div>Content</div>'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_with_empty_props(self):
        node = LeafNode(tag='span', value='Text', props={})
        expected_output = '<span>Text</span>'
        self.assertEqual(node.to_html(), expected_output)

if __name__ == '__main__':
    unittest.main()
