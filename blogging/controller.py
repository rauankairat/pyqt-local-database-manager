
class Controller:
    def __init__(self):
        self.id = 0
        self.username = 'user'
        self.password = 'blogging2025'
        self.logged_in = False 
        self.blogs = []

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

        if blog_to_delete is None:
            return False
        else
            blogs.remove(blog_to_delete)
            return True
                
            
            


            





    
   


        
        
       

