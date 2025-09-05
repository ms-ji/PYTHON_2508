class Walkable:
    def walk(self):
        print('걷는다.')
class Runnalble:
    def run(self):
        print('뛴다.')

class Human(Walkable,Runnalble):
    pass

h = Human()
h.walk()
h.run()
#걷는다.
#뛴다.
