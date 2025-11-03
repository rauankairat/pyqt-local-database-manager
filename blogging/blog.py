class Blog:
    def __init__(self,bid,name,url,email):
        self.id=bid
        self.name=name
        self.url=url
        self.email=email

    def __eq__(self, blog):
        if blog == None:
            return False
        return self.id==blog.id and self.name==blog.name and self.url==blog.url and self.email==blog.email
    