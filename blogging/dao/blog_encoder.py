import json
from blogging.blog import Blog

class BlogEncoder(json.JSONEncoder):
    '''JSON encoder class for Blog class'''
    def default(self, blog):
        if isinstance(blog, Blog):
            return {'id':blog.id,
                    'name':blog.name,
                    'url': blog.url,
                    'email': blog.email,
                    }
        return super().default(blog)