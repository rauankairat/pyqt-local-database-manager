import datetime

class Post:
    def __init__(self,code,title,text):
        self.code = code
        self.title = title
        self.text = text
        self.creation = datetime.datetime.now()
        self.update = datetime.datetime.now()

    #Check if two Post objects are equal based on their codes titles and text
    def __eq__(self,post):
        if post == None:
            return False
        return self.code==post.code and self.title==post.title and self.text==post.text
