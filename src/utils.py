from textnode import *
import unittest
import re


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches



#Mine
# def markdown_to_blocks(markdown:str):
#     splited = markdown.split('\n')
#     blocks = []
#     i = 0
#     while i < len(splited):
#         line = splited[i]

#         if line == '':
#             pass

#         elif line.startswith('# '):
#             blocks.append(line.strip())
        
#         elif line.startswith('* '):
#             _list = [line.strip()]
#             i += 1
#             while i < len(splited):
#                 line = splited[i]
#                 if line == '':
#                     pass
#                 elif not line.startswith('* '):
#                     break
                
#                 _list.append(line.strip())
#                 i += 1
            
#             blocks.append('\n'.join(_list))
#             i -= 1
        
#         else:
#             _list = [line.strip()]
#             i += 1
#             while i < len(splited):
#                 line = splited[i]
#                 if line == '':
#                     pass
#                 elif line.startswith('* ') or line.startswith('* '):
#                     break
                
#                 _list.append(line.strip())
#                 i += 1
            
#             blocks.append(''.join(_list))
#             i -= 1
        
#         i += 1
#     return blocks
        


#provided code
#didnt read correctly that blocks where separated by \n\n i though it was just \n :()

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks



def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph