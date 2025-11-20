from blogging.blog import Blog
from blogging.post import Post
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException
import hashlib
import os

class Controller:
    def __init__(self):
        self.id = 0
        self.logged_in = False
        self.blogs = []
        self.current_blog = None
        self.users = {}
        path = os.path.join(os.path.dirname(__file__), "users.txt")
        with open(path, "r") as usersFile:
            for line in usersFile:
                [name, password] = line.split(',')
                self.users[name] = password.rstrip()


    # Log in
    def login(self, name, password):
        if self.logged_in:
            raise DuplicateLoginException
        for user in self.users:
            # hashed is the password tried, in sha 256
            hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if user == name and hashed ==self.users[user] :
                self.logged_in = True
                return True
        raise InvalidLoginException

    # Log out
    def logout(self):
        if self.logged_in:
            self.logged_in = False
            return True
        else:
            raise InvalidLogoutException

    #Create new blog
    def create_blog(self, bid, name,url,email):
        if self.search_blog(bid)!=None:
            return None
        if not self.logged_in:
            return None
        else:
            blog = Blog(bid,name,url,email)
            self.blogs.append(blog)
            return blog

    #Search blog
    def search_blog(self, id):
        if not self.logged_in:
            return None
        for blog in self.blogs:
            if (blog.id == id):
                return blog
        return None

    # Retrieve existing blogs
    def retrieve_blogs(self, name):
        if not self.logged_in:
            return None

        blog_list = []

        for blog in self.blogs:
            if name in blog.name:
                blog_list.append(blog)
        return blog_list

    #Delete existing blog
    def delete_blog(self,id):

        if not self.logged_in:
            return False

        blog_to_delete = self.search_blog(id)

        if blog_to_delete == self.current_blog:
            return False

        if blog_to_delete is None:
            return False
        else:
            self.blogs.remove(blog_to_delete)
            return True

    # Update existing blog
    def update_blog(self, bid, new_bid, name,url,email):
        if not self.logged_in:
            return False
        if not self.blogs:
            return False
        if self.search_blog(new_bid)!=None and bid!=new_bid:
            return False
        blog = self.search_blog(bid)
        if blog == self.current_blog:
            return False
        if blog!=None:
            blog.id = new_bid
            blog.name = name
            blog.url = url
            blog.email=email
            return True
        return False
        
    #List all blogs
    def list_blogs(self):

        if not self.logged_in:
            return None

        return self.blogs

    # Set current blog
    def set_current_blog(self, bid):
        if not self.logged_in:
            return None
        self.current_blog = self.search_blog(bid)

    # Choose current blog
    def get_current_blog(self):
        if not self.logged_in:
            return None
        return self.current_blog

    # Unset current blog
    def unset_current_blog(self):
        if not self.logged_in:
            return None
        self.current_blog=None

    #Create new post in the current blog
    def create_post(self, title, text):
        if not self.logged_in:
            return None
        if not self.current_blog:
            return None
        code = self.current_blog.post_count+1
        return self.current_blog.create_post(code,title,text)

    # Searches for post
    def search_post(self,code):
        if not self.logged_in:
            return None
        if not self.current_blog:
            return None
        post = self.current_blog.search_post(code)
        return post

    #Updates post
    def update_post(self, code,title,text):
        if not self.current_blog:
            return None
        return self.current_blog.update_post(code,title,text)

    #Retrieve existing posts from the current blog
    def retrieve_posts(self, text):

        if not self.logged_in:
          return None

        if self.current_blog is None:
            return None

        if not self.current_blog.posts:
            return []

        return self.current_blog.retrieve(text)


    #Delete existing post in the current blog
    def delete_post(self, code):

        if not self.logged_in:
            return False
        if self.current_blog is None:
            return False

        post_to_delete = self.search_post(code)

        if post_to_delete is None:
            return False
        else:
            self.current_blog.posts.remove(post_to_delete)
            return True

    #List all posts from the current blog
    def list_posts(self):
        if not self.logged_in:
            return None

        if self.current_blog is None:
            return None

        if not self.blogs:
            return None

        if not self.current_blog.posts:
            return []

        return list(reversed(self.current_blog.posts))

