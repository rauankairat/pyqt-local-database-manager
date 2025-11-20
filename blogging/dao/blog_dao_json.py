from blogging.dao.blog_dao import BlogDAO
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class BlogDAOJSON(BlogDAO):
    def __init__(self):
        self.blogs = []

    def search_blog(self, key):
        for blog in self.blogs:
            if (blog.id == key):
                return blog
        return None

    def create_blog(self, blog):
        self.blogs.append(blog)
        return blog

    def retrieve_blogs(self, search_str):
        blog_list = []
        for blog in self.blogs:
            if search_str in blog.name:
                blog_list.append(blog)
        return blog_list

    def update_blog(self, bid, newBlog):
        blog = self.search_blog(bid)
        blog.id=newBlog.id
        blog.name=newBlog.name
        blog.url=newBlog.url
        blog.email=newBlog.email

    def delete_blog(self, key):
        blog_to_delete = self.search_blog(key)
        self.blogs.remove(blog_to_delete)
        return True

    def list_blogs(self):
        return self.blogs