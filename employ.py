class person(object):
    def __init__(self, name, id_no):
        self.name= name
        self.id_no= id_no
    def display(self):
        print(self.name)
        print(self.id_no)
class employ(person):
    def __init__(self, name, id_no, salary, post):
        super().__init__(name, id_no)
        self.salary= salary
        self.post= post
    def info(self):
        print(self.salary, self.post)
a= employ("Mohan", 13, 30000, "intern")
a.display()
a.info()