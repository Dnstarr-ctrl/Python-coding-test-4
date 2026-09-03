class Book:
    def __init__(self,title,author):
        self.title = title
        self.author=author
        self.__borrowed=False

    def borrow(self):
        self.__borrowed=True
        print(self.title ,"has been borrowed.")
    def return_book(self):
        self.__borrowed=False
        print(self.title ,"has been returned now.")

book1=Book("Sherlock Holmes","Arthur Conan Doyle")
book2=Book("Wings Of Fire","T.U.I T Sutherland")
book3=Book("When the mountain meets the moon", "Grace Lin")
book1.borrow()
book2.borrow()
book3.borrow()
book1.return_book()
book2.return_book()
book3.return_book()
        
        
    
