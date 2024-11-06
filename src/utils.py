from textnode import *
import unittest

def split_nodes_delimiter(old_nodes:TextNode, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        acc = ""
        i = 0
        while i < len(node.text):
            if node.text[i] == delimiter:
                if acc != "":
                    new_nodes.append(TextNode(acc, TextType.TEXT))
                acc = ""
                delimiter_closed = False
                for j in range(i + 1, len(node.text)):
                    if node.text[j] == delimiter:
                        delimiter_closed = True
                        break

                    acc += node.text[j]
                
                if not delimiter_closed:
                    raise ValueError("Invalid markdown, formatted section not closed")
                new_nodes.append(TextNode(acc, text_type))
                i = j + 1
                acc = ""

            if i < len(node.text):
                acc += node.text[i]
            i += 1
        if acc != "":
            new_nodes.append(TextNode(acc, TextType.TEXT))

    return new_nodes

node = TextNode("Here is text with a `code block`", TextType.TEXT)
        
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
print(new_nodes)
