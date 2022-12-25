#!/usr/bin/python3
"""No module imported"""


class Square:
    """Defines a class: Square with a private attribute: size and checks Error
      and returns the area of the square. Prints in stdout the square with the
      character '#' preceded by ' ' as specified"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return pow(self.__size, 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) == 2:
            i, j = value
            if isinstance(i, int) and isinstance(j, int):
                if i >= 0 and j >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()

            for i in range(pow(self.__size, 2)):
                if (i % self.__size == 0):
                    if i != 0:
                        print()
                    for i in range(self.__position[0]):
                        print(' ', end='')
                print('#', end='')
            print()
