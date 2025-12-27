class media:
    def __init__(self, mcode, title, price ):
        self.mcode=mcode
        self.title=title
        self.price=price

    def showmedia(self):
        print(f"Media Code: {self.mcode}")                     
        print(f"Title: {self.title}")
        print(f"Price: {self.price:}₹")

class dvd(media):
    def __init__(self, mcode, title, price, capacity ):
        super().__init__(mcode,title,price)
        self.capacity=capacity

    def showmedia(self):
        super().showmedia()
        print(f'capacity:- {self.capacity} MB ')

class Book(media):
    def __init__(self, mcode: int, title: str, price: float, pages: int):
        super().__init__(mcode, title, price)
        self.pages = pages

    def showmedia(self):
        super().showmedia()
        print(f"Pages: {self.pages}")


dvd1=dvd(1001,'thunderstrom in akola', 99, 123)
book1=Book(108,'deshonati', 5, 10)

print('DVD info :-')
dvd1.showmedia()

print('\nBOOK info :-')
book1.showmedia()