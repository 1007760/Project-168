class Bookshelf :
    def __init__(self, name, author, price, published) :
        self.bookshelf_name = name
        self.bookshelf_author = author
        self.bookshelf_price = price
        self.bookshelf_published = published
        
    def add_book(self) :
        print("Book Name : " + self.bookshelf_name)
        print("Book Author : " + self.bookshelf_author)
        print("Book Price : "  + self.bookshelf_price)
        print("Year the Book was Published : " +str(self.bookshelf_published))
        print("Book Added")
        
    def years_since_published(self) :
        years = 2022 - self.bookshelf_published
        print("This book was published " + str(years) + " years ago.")
        
book1 = Bookshelf("The Room with the Yellow Wallpaper", "Charlotte Perkins Gilman", "$4.99", 1892)
book1.add_book()
book1.years_since_published()
book2 = Bookshelf("Beowulf", "unknown", "$1,099", 1815)
book2.add_book()
book2.years_since_published()