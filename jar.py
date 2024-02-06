import emoji

class Jar:
    def __init__(self, capacity=12):
        if (capacity < 0):
            raise ValueError("wrong cap")

        self._capacity = capacity
        self._size= 0

    def __str__(self):
        output = emoji.emojize(":cookie:")
        if (emoji.is_emoji(output)):
            return f'{output * self.size}'

    def deposit(self, n):
        if ((self.size + n) <= self.capacity ) :
            self._size = self.size + n
        else:
            raise ValueError ("Is full")

    def withdraw(self, n):
        if self.size > n :
            self._size = self.size - n
        else:
            raise ValueError("not that many cookies left")

    @property
    def capacity(self):
        return self._capacity
    """
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
    """
    @property
    def size(self):
        return self._size
    """
    @size.setter
    def size(self, size):
        self._size = self.size
    """
