import datetime

class Post:
    def __init__(self,code,title,text):
        self.code = code
        self.title = title
        self.text = text
        self.creation = datetime.datetime.now()
        self.update = datetime.datetime.now()

    def __eq__(self,post):
        if post == None:
            return False
        return self.code==post.code and self.title==post.title and self.text==post.text
