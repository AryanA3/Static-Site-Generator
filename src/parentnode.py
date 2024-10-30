from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag = None, childern = None, props = None):
        super().__init__(tag, None, childern, props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError('tag not provided')

        if self.childern in [[], None]:
            raise ValueError('childern not provided')
        
        complete_inside = ""

        for child in self.childern:
            complete_inside += child.to_html()
        
        return f'<{self.tag}>{complete_inside}</{self.tag}>'
