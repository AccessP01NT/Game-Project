class Player:
    """A sample Player class"""

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {} {}'.format(self.first, self.last,self.age)

    def __repr__(self):
        return "Player ('{}', '{}', {})".format(self.first, self.last, self.age)

