import sys
from blogging.configuration import Configuration
from blogging.controller import Controller
from .login import loginGui
from .blog_menu import blogMenu
from .blog_views.search_blog import searchBlog
from .blog_views.create_blog import createBlog
from .blog_views.retrieve_blog import retrieveBlog
from .blog_views.choose_blog import chooseBlog

from .post_menu import postMenu
from .post_views.create_post import createPost
from .post_views.delete_post import deletePost
from .post_views.list_posts import listPosts
from .post_views.update_post import updatePost
from .post_views.retrieve_posts import retrievePosts


from .blog_views.update_blog import updateBlog
from .blog_views.delete_blog import deleteBlog
from .blog_views.list_blog import listBlog



from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from PyQt6.QtGui import QIcon

class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        self.controller = Controller()
        self.setWindowIcon(QIcon("uvic.png"))

        # a dictionary to not use magic numbers for the stack
        self.view_map = {
            "login": 0,

            "blog_menu": 1,
            "search_blogs": 2,
            "create_blog": 3,
            "retrieve_blogs": 4,
            "update_blog": 5,
            "delete_blog": 6,
            "list_blogs": 7,
            "choose_blog": 8,

            "post_menu": 9,
            "create_post": 10,
            "retrieve_posts": 11,
            "update_post": 12,
            "delete_post": 13,
            "list_posts": 14
        }

        self.widget= QStackedWidget()
        
        # these need to be in order to match the dict above
        self.widget.addWidget(loginGui(self)) #0
        self.widget.addWidget(blogMenu(self)) #1
        self.widget.addWidget(searchBlog(self)) #2
        self.widget.addWidget(createBlog(self)) #3
        self.widget.addWidget(retrieveBlog(self)) #4
        self.widget.addWidget(updateBlog(self)) #5
        self.widget.addWidget(deleteBlog(self)) #6
        self.widget.addWidget(listBlog(self)) #7
        self.widget.addWidget(chooseBlog(self)) #8
        self.widget.addWidget(postMenu(self)) #9
        self.widget.addWidget(createPost(self)) #10
        self.widget.addWidget(retrievePosts(self)) #11
        self.widget.addWidget(updatePost(self)) #12
        self.widget.addWidget(deletePost(self)) #13
        self.widget.addWidget(listPosts(self)) #14
        
        self.setCentralWidget(self.widget)
        #login is the first view
        self.switchGui("login")
    
    def switchGui(self, index):
        self.widget.setCurrentIndex(self.view_map[index])


def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
