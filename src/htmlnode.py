from functools import reduce


class HTMLNode():
    def __init__(self, tag:str = None, value:str = None, childern:list = None, props:dict = None):
        self.tag = tag
        self.value = value
        self.childern = childern
        self.props = props

    def to_html(self):
        raise NotImplementedError('to_html function not implemented')

    def props_to_html(self):
        if self.props == None:
            return ""
        return reduce(lambda acc,next: acc + f'{next}="{self.props[next]}" ', self.props.keys(), " ").rstrip()

    def __repr__(self):
        return f'HTMLNode: tag: {self.tag}, {[i.__repr__() for i in self.childern]}, {self.props}'
