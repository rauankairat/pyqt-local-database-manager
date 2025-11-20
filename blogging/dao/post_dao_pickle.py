import os
import pickle
from typing import List, Optional

from blogging.configuration import Configuration
from blogging.post import Post
from blogging.dao.post_dao import PostDAO


class PostDAOPickle(PostDAO):
  

    def __init__(self):
        self.posts = []      


    def search_post(self, key: int):
        for p in self.posts:
            if p.code == key:
                return p
        return None

    def create_post(self, post):
        if post.id in self.posts:
            return False
        self.posts[post.id] = post
        return True

    def retrieve_posts(self, search_string):
        return [p for p in self.posts.values()
                if search_string.lower() in p.title.lower()
                or search_string.lower() in p.text.lower()
        ]

    def update_post(self, key: int, new_title: str, new_text: str) -> bool:
        post = self.search_post(key)
        if post is None:
            return False
        post.title = new_title
        post.text = new_text
        self._save_to_file()
        return True

    def delete_post(self, key: int) -> bool:
        post = self.search_post(key)
        if post is None:
            return False
        self.posts.remove(post)
        self._save_to_file()
        return True

    def list_posts(self):
        return list(self.posts)
