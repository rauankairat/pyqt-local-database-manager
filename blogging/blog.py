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

    #Checks if two Blog objects are equal.
    def __eq__(self, blog):
        if blog == None:
            return False
        return self.id==blog.id and self.name==blog.name and self.url==blog.url and self.email==blog.email
    
    #Creates a new Post object and adds it to this blog's post list
    def create_post(self,code,title,text):
        post = Post(code,title,text)
        self.posts.append(post)
        self.post_count+=1
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

    