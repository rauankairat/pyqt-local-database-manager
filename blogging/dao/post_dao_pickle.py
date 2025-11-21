import os
import pickle
from typing import List, Optional
import time

from blogging.configuration import Configuration
from blogging.post import Post
from blogging.dao.post_dao import PostDAO

class PostDAOPickle(PostDAO):

    def __init__(self, blog):
        super().__init__(blog)
        self.posts = {}

    def search_post(self, key):
        return self.posts.get(key)

    def create_post(self, title, text):
        
        self.blog.post_count += 1

        code = self.blog.post_count

        post = Post(code,title,text)

        self.posts[code] = post
        return post

    def update_post(self,key, new_title, new_text):
       
        post = self.posts.get(key)
        if not post:
            return False
        
        post.update(new_title, new_text)
        return True

    def delete_post(self, key):
        if key not in self.posts:
            return False
        
        del self.posts[key]
        return True
    
    def retrieve_posts(self,search_string):
        results = []

        for post in self.posts.values():
            if search_string in post.title or search_string in post.text:
                results.append(post)
        
        return results

    def list_posts(self):

        all_posts = list(self.posts.values())

        all_posts.sort(key=lambda p: p.code, reverse=True)

        return all_posts


        