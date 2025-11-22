from blogging.blog import Blog
from blogging.post import Post
from blogging.dao.blog_dao_json import BlogDAOJSON
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException
import hashlib
import os
from blogging.configuration import Configuration

class Controller:
    def __init__(self):

        self.id = 0
        self.logged_in = False
        self.blogs = BlogDAOJSON()
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
        if not self.logged_in:
            raise IllegalAccessException
        if self.search_blog(bid)!=None:
            raise IllegalOperationException
        else:
            return self.blogs.create_blog(Blog(bid,name,url,email))

    #Search blog
    def search_blog(self, id):
        if not self.logged_in:
            raise IllegalAccessException
        return self.blogs.search_blog(id)

    # Retrieve existing blogs
    def retrieve_blogs(self, name):
        if not self.logged_in:
            raise IllegalAccessException
        return self.blogs.retrieve_blogs(name)

    #Delete existing blog
    def delete_blog(self,id):
        if not self.logged_in:
            raise IllegalAccessException
        blog_to_delete = self.search_blog(id)
        if blog_to_delete == self.current_blog:
            raise IllegalOperationException
        if blog_to_delete is None:
            raise IllegalOperationException
        return self.blogs.delete_blog(id)

    # Update existing blog
    # Update existing blog
    def update_blog(self, bid, new_bid, name,url,email):
        if not self.logged_in:
            raise IllegalAccessException
        if self.current_blog!=None and self.current_blog.id == bid:
            raise IllegalOperationException
        if not self.search_blog(bid):
            raise IllegalOperationException

        self.blogs.update_blog(bid, Blog(new_bid, name, url, email))
        return True

        
    #List all blogs
    def list_blogs(self):
        if not self.logged_in:
            raise IllegalAccessException
        return self.blogs.list_blogs()

    # Set current blog
    def set_current_blog(self, bid):
        if not self.logged_in:
            raise IllegalAccessException
        src = self.blogs.search_blog(bid)
        if src == None:
            raise IllegalOperationException
        self.current_blog = src

    # Choose current blog
    def get_current_blog(self):
        if not self.logged_in:
            raise IllegalAccessException
        return self.current_blog

    # Unset current blog
    def unset_current_blog(self):
        if not self.logged_in:
            raise IllegalAccessException
        self.current_blog=None

    #Create new post in the current blog
    def create_post(self, title, text):
        if not self.logged_in:
            raise IllegalAccessException
        if not self.current_blog:
            raise NoCurrentBlogException
        return self.current_blog.create_post(title,text)

    # Searches for post
    def search_post(self,code):
        if not self.logged_in:
            raise IllegalAccessException
        if not self.current_blog:
            raise NoCurrentBlogException
        post = self.current_blog.search_post(code)
        return post

    #Updates post
    def update_post(self,code,title,text):
        if not self.logged_in:
            raise IllegalAccessException
        if not self.current_blog:
            raise NoCurrentBlogException
        return self.current_blog.update_post(code,title,text)

    #Retrieve existing posts from the current blog
    def retrieve_posts(self, text):

        if not self.logged_in:
          raise IllegalAccessException

        if self.current_blog is None:
            raise NoCurrentBlogException

        return self.current_blog.retrieve(text)


    #Delete existing post in the current blog
    def delete_post(self, code):

        if not self.logged_in:
          raise IllegalAccessException

        if self.current_blog is None:
            raise NoCurrentBlogException

        return self.current_blog.delete_post(code)

    #List all posts from the current blog
    def list_posts(self):
        if not self.logged_in:
            raise IllegalAccessException

        if self.current_blog is None:
            raise NoCurrentBlogException

        return self.current_blog.list_posts()

   
        

