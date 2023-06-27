class Order(object):
    def __init__(self,code,title,author,price,number,total):
        self._code = code
        self._title = title
        self._author = author
        self._price = price
        self._number = number
        self._total = total

    def __str__(self):
        return f'Book Title: {self._title}\nAuthor: {self._author}\nPrice of a book: ${self._price:.2f}\nNumber of books: {self._number}\nTotal order cost: ${self._total:.2f}'
