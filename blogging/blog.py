from blogging.post import Post
import datetime

class Blog:
    def __init__(self,bid,name,url,email):
        self.id=bid
        self.name=name
        self.url=url
        self.email=email
        self.posts=[]
        self.post_count=0

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
    def create_post(self,code,title,text):
        self.post_count+=1
        post = Post(self.post_count,title,text)
        self.posts.append(post)
        return post

    #Searches for a Post in this blog by its code
    def search_post(self, code):
        for post in self.posts:
            if (post.code == code):
                return post
        return None

    # Retrieves all posts from this blog that contain the given text
    def retrieve(self,text):
        post_list = []

        for post in self.posts:

            if (text in post.title) or (text in post.text):
                post_list.append(post)

        return post_list

    # Updates an existing post’s title and text, identified by its code
    def update_post(self, code, new_title, new_text):
        ''' update a post from the blog '''
        updated_post = None

        for post in self.posts:
            if post.code == code:
                updated_post = post
                break

        if not updated_post:
            return False

        updated_post.update(new_title, new_text)
        return True
    
    def delete_post(self, code):
        ''' delete a post from the blog '''
        post_to_delete_index = -1
        # first, search the post by code
        for i in range(len(self.posts)):
            if self.posts[i].code == code:
                post_to_delete_index = i
                break
        # post does not exist
        if post_to_delete_index == -1:
            return False
        # post exists, delete post
        self.posts.pop(post_to_delete_index)
        return True

    def list_posts(self):
        ''' list all posts from the blog from the 
            more recently added to the least recently added'''
        # list existing posts
        posts_list = []
        for i in range(-1, -len(self.posts)-1, -1):
            posts_list.append(self.posts[i])
        return posts_list

    def retrieve_posts(self, search_string):
        ''' retrieve posts in the blog that satisfy a search string '''
        # retrieve existing posts
        retrieved_posts = []
        for post in self.posts:
            if search_string in post.title or search_string in post.text:
                retrieved_posts.append(post)
        return retrieved_posts


    