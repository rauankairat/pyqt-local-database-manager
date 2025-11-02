class Blog:
    def __init__(self,bid,name,url,email)
        self.id=bid
        self.name=name
        self.url=url
        self.email=email

    def __eq__(self, blog):
        return self.id==blog.id
    