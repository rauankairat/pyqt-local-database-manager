import os
import pickle
from typing import List, Optional

from blogging.configuration import Configuration
from blogging.post import Post
from blogging.dao.post_dao import PostDAO


class PostDAOPickle(PostDAO):
  

    def __init__(self):
              
        self.posts = []      


        if not os.path.exists(Configuration.records_path):
            os.makedirs(Configuration.records_path)


        self._load_from_file()



    def _file_path(self) -> str:
        return os.path.join(
            Configuration.records_path,
            f"{self.blog.id}{Configuration.records_extension}"
        )

    def _load_from_file(self) -> None:
        path = self._file_path()
        if not os.path.exists(path):
            self.posts = []
            if hasattr(self.blog, "post_count"):
                self.blog.post_count = 0
            return

        with open(path, "rb") as f:
            try:
                self.posts = pickle.load(f)
            except:
                self.posts = []

        # Sync blog.counter
        if hasattr(self.blog, "post_count"):
            if self.posts:
                self.blog.post_count = max(p.code for p in self.posts)
            else:
                self.blog.post_count = 0

    def _save_to_file(self) -> None:
        path = self._file_path()
        with open(path, "wb") as f:
            pickle.dump(self.posts, f)



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
