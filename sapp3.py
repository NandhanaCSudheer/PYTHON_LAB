class Publisher:
    def __init__(self,name):
        self.name=name
        print(f"Publisher constructor called for {self.name}")
    
    def display(self):
        print(f"Publisher name:{self.name}")

class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
        print(f"Book constructor called for '{self.title}'by {self.author}")
    
    def display(self):
        print("Book details: ")
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Publisher:{self.name}")

b1=Book("Bloomsbury","Harry Potter","J.K Rowling")
b1.display()