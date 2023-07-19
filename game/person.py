class Person(object):
    def __init__(self):
        self.lives = 3

    def get_damage(self):
        self.lives -= 1
        return self.lives

    def get_hill(self):
        self.lives += 1
        return self.lives


main_person = Person()
