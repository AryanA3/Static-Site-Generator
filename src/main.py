from textnode import *
from leafnode import LeafNode


def text_node_to_html_node(text_node:TextNode):
    if text_node.text_type in [TextType.TEXT, TextType.NORMAL]:
        return LeafNode(value=text_node.text)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    
    elif text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text, {"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode('img', "", {'src': text_node.url, 'alt': text_node.text})
    
    else:
        raise Exception(f'No such text type {text_node.text_type}')


def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")

    print(text_node)

if __name__ == "__main__":
    main()