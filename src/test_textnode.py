import unittest
from textnode import TextType, TextNode



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_print_correct(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, 'https://google.com')
        self.assertEqual(node.__repr__(), 'TextNode(This is a text node, bold, None)')
        self.assertEqual(node2.__repr__(), 'TextNode(This is a text node, bold, https://google.com)')

    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, 'https://google.com')
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_correct_text_type(self):    
        self.assertRaises(AttributeError, lambda : TextNode("This is a text node", 'b', 'https://google.com'))


if __name__ == "__main__":
    unittest.main()