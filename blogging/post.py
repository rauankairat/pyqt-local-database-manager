import datetime

class Post:
    def __init__(self,code,title,text,creation,update):
        self.code = code
        self.title = title
        self.text = text
        self.creation = datetime.datetime.now()
        self.updatee = datetime.datetime.now()
