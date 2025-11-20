import datetime

class Post:
    def __init__(self,code,title,text):
        self.code = code
        self.title = title
        self.text = text
        self.creation_time = datetime.datetime.now()
        self.update_time = datetime.datetime.now()

    def update(self, title, text):
        self.title = title
        self.text = text
        self.update_time = datetime.datetime.now()	

    def __eq__(self, other):
        ''' checks whether this post is the same as other post '''
        return self.code == other.code and self.title == other.title and self.text == other.text

    def __str__(self):
        ''' converts the post object to a string representation '''
        return str(self.code) + "; " + str(self.creation_time) + "; " + str(self.update_time) + "\n" + str(self.title) + "\n\n" + self.text

    def __repr__(self):
        ''' converts the post object to a string representation for debugging '''
        return "Post(%r, %r, %r,\n%r,\n\n%r\n)" % (self.code, self.creation_time, self.update_time, self.title, self.text)
