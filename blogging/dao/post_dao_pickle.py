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

        # read autosave setting from Configuration
        self.autosave = Configuration.autosave

        # build path to records directory: blogging/records/<blog_id>.dat
        records_dir = os.path.join(os.path.dirname(__file__), "..", "records")
        records_dir = os.path.normpath(records_dir)
        os.makedirs(records_dir, exist_ok=True)

        self.file_path = os.path.join(records_dir, f"{self.blog.id}.dat")

        if self.autosave and os.path.exists(self.file_path):
            with open(self.file_path, "rb") as f:
                try:
                    loaded = pickle.load(f)

                    # normalize to dict: {code: Post}
                    if isinstance(loaded, dict):
                        self.posts = loaded
                    else:
                        # list of Post objects
                        self.posts = {post.code: post for post in loaded}

                    # update counter
                    if self.posts:
                        self.blog.post_count = max(self.posts.keys())

                except Exception:
                    # corrupt or empty file → start clean
                    self.posts = {}
                    self.blog.post_count = 0

    def search_post(self, key):
        return self.posts.get(key)

    def create_post(self, title, text):
        
        self.blog.post_count += 1

        code = self.blog.post_count

        post = Post(code,title,text)

        self.posts[code] = post
        self._save()
        return post

    def update_post(self,key, new_title, new_text):
       
        post = self.posts.get(key)
        if not post:
            return False
        
        post.update(new_title, new_text)
        self._save()
        return True

    def delete_post(self, key):
        if key not in self.posts:
            return False
        
        del self.posts[key]
        self._save()
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

    def _save(self):
        if not self.autosave:
            return

        # always save as dict {code: Post}
        with open(self.file_path, "wb") as f:
            pickle.dump(self.posts, f)

        