from blogging.post import Post

class Blog:
    def __init__(self,bid,name,url,email):
        self.id=bid
        self.name=name
        self.url=url
        self.email=email
        self.posts=[]
        self.post_count=0

    def __eq__(self, blog):
        if blog == None:
            return False
        return self.id==blog.id and self.name==blog.name and self.url==blog.url and self.email==blog.email
    
    def create_post(self,code,title,text):
        post = Post(code,title,text)
        self.posts.append(post)
        self.post_count+=1
        return post

    def search_post(self, code):
        for post in self.posts:
            if (post.code == code):
                return post
        return None

    def retrieve(self,text):
        post_list = []

        for post in self.posts:

            if (text in post.title) or (text in post.text):
                post_list.append(post)

        return post_list

    