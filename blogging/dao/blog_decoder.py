import json
from blogging.blog import Blog


class BlogDecoder(json.JSONDecoder):
    '''JSON decoder class fot Blog class'''
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    def object_hook(self, dct):
        return Blog(
            dct['id'], 
            dct['name'], 
            dct['url'], 
            dct['email'],
        )