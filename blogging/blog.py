from blogging.post import Post
from blogging.dao.post_dao_pickle import PostDAOPickle
import datetime

class Blog:
    def __init__(self,bid,name,url,email):
        self.id=bid
        self.name=name
        self.url=url
        self.email=email
        self.post_count=0
        self.posts= PostDAOPickle(self)
      

    def __str__(self):
        ''' converts the blog object to a string representation '''
        return str(self.id) + "; " + self.name + "; " + self.url + "; " + self.email

    #Checks if two Blog objects are equal.
    def __eq__(self, blog):
        if blog == None:
            return False
        return self.id==blog.id and self.name==blog.name and self.url==blog.url and self.email==blog.email
    
    def __repr__(self):
        ''' converts the blog object to a string representation for debugging '''
        return "Blog(%r, %r, %r, %r)" % (self.id, self.name, self.url, self.email)


    #Creates a new Post object and adds it to this blog's post list
    def create_post(self,title,text):
        return self.posts.create_post(title, text)

    #Searches for a Post in this blog by its code
    def search_post(self, code):
        return self.posts.search_post(code)

    # Retrieves all posts from this blog that contain the given text
    def retrieve(self,text):
    
        return self.posts.retrieve_posts(text)

    # Updates an existing post’s title and text, identified by its code
    def update_post(self, code, title, text):
        ''' update a post from the blog '''
    
        return self.posts.update_post(code, title, text)

    
    def delete_post(self, code):
        ''' delete a post from the blog '''
        
        return self.posts.delete_post(code)

    def list_posts(self):
        ''' list all posts from the blog from the 
            more recently added to the least recently added'''
        # list existing posts
      
        return self.posts.list_posts()



    def retrieve_posts(self, search_string):
        ''' retrieve posts in the blog that satisfy a search string '''
        # retrieve existing posts
        
        return self.posts.retrieve_posts(search_string)


    