import os
import pickle
from typing import List, Optional
import time

from blogging.configuration import Configuration
from blogging.post import Post
from blogging.dao.post_dao import PostDAO

class PostDAOPickle(PostDAO):
    """
    DAO implementation that stores and retrieves a blog’s posts using pickle.
    Posts for each blog are kept in a separate .dat file under blogging/records/.
    """

    def __init__(self, blog):
        super().__init__(blog)
        self.posts = {}

        # read autosave setting from Configuration
        self.autosave = Configuration.autosave

        
        records_dir = os.path.join(os.path.dirname(__file__), "..", "records")
        records_dir = os.path.normpath(records_dir)
        os.makedirs(records_dir, exist_ok=True)

        self.file_path = os.path.join(records_dir, f"{self.blog.id}.dat")

        if self.autosave and os.path.exists(self.file_path):
            with open(self.file_path, "rb") as f:
                try:
                    loaded = pickle.load(f)

                   
                    if isinstance(loaded, dict):
                        self.posts = loaded
                    else:
                        
                        self.posts = {post.code: post for post in loaded}

                    
                    if self.posts:
                        self.blog.post_count = max(self.posts.keys())

                except Exception:
                    
                    self.posts = {}
                    self.blog.post_count = 0

    def search_post(self, key):
        """Return a post by its code, or None if it does not exist."""
        return self.posts.get(key)

    def create_post(self, title, text):
        """
        Create a new Post object, assign next post code,
        store it in dictionary, and save to file if autosave.
        """
        
        self.blog.post_count += 1

        code = self.blog.post_count

        post = Post(code,title,text)

        self.posts[code] = post
        self._save()
        return post

    def update_post(self,key, new_title, new_text):
        """
        Update the title and text of an existing post.
        Return False if the post does not exist.
        """
       
        post = self.posts.get(key)
        if not post:
            return False
        
        post.update(new_title, new_text)
        self._save()
        return True

    def delete_post(self, key):
        """
        Delete a post by code. Return False if the post does not exist.
        """
        if key not in self.posts:
            return False
        
        del self.posts[key]
        self._save()
        return True
    
    def retrieve_posts(self,search_string):
        """
        Retrieve all posts whose title or text contains the search string.
        """
        results = []

        for post in self.posts.values():
            if search_string in post.title or search_string in post.text:
                results.append(post)
        
        return results

    def list_posts(self):
        """
        Return all posts sorted by code in descending order:
        newest posts first.
        """

        all_posts = list(self.posts.values())

        all_posts.sort(key=lambda p: p.code, reverse=True)

        return all_posts

    def _save(self):
        """
        Save all posts to the blog's .dat file using pickle,
        if autosave is enabled.(helper func)
        """
        if not self.autosave:
            return

        # always save as dict {code: Post}
        with open(self.file_path, "wb") as f:
            pickle.dump(self.posts, f)

        