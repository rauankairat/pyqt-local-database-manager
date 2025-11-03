from blogging.blog import Blog
from blogging.post import Post

class Controller:
    def __init__(self):
        self.id = 0
        self.username = 'user'
        self.password = 'blogging2025'
        self.logged_in = False 
        self.blogs = []
        self.current_blog = None

    def login(self, name, password):
        if self.username == name and self.password == password and not self.logged_in:
            self.logged_in = True
            return True
        return False

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            return True
        else:
            return False

    def create_blog(self, bid, name,url,email):
        if self.search_blog(bid)!=None:
            return None
        if not self.logged_in:
            return None
        else: 
            blog = Blog(bid,name,url,email)
            self.blogs.append(blog)
            return blog

    def search_blog(self, id):
        if not self.logged_in:
            return None
        for blog in self.blogs:
            if (blog.id == id):
                return blog
        return None

    def retrieve_blogs(self, name):
        if not self.logged_in:
            return None

        blog_list = []

        for blog in self.blogs:
            if name in blog.name:
                blog_list.append(blog)
        return blog_list
    
    def delete_blog(self,id):

        if not self.logged_in:
            return None
                
        blog_to_delete = self.search_blog(id)

        if blog_to_delete == self.current_blog:
            return False

        if blog_to_delete is None:
            return False
        else:
            self.blogs.remove(blog_to_delete)
            return True

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
    
    def list_blogs(self):

        if not self.logged_in:
            return None

        return self.blogs
    
    def retrieve_posts(self,text):

        if not self.logged_in:
            return None

        post_list = []

        for blog in self.blogs:

            if text in post.text:
                post_list.append(post)

            else if text in post.title:
                post_list.append(post)

        return post_list


    def set_current_blog(self, bid):
        if not self.logged_in:
            return None
        self.current_blog = self.search_blog(bid)

    def get_current_blog(self):
        if not self.logged_in:
            return None
        return self.current_blog
    
    def unset_current_blog(self):
        if not self.logged_in:
            return None
        self.current_blog=None

    def create_post(self, title, text):
        if not self.logged_in:
            return None
        if not self.current_blog:
            return None
        code = self.current_blog.post_count+1
        return self.current_blog.create_post(code,title,text)

    def search_post(self,code):
        if not self.logged_in:
            return None
        if not self.current_blog:
            return None
        post = self.current_blog.search_post(code)
        return post
            
            


            





    
   


        
        
       

