class Horse:            # класс описывающий лошадь.
    x_distance = 0      # пройденный путь.
    _sound = 'Frrr'     # звук, который издаёт лошадь.

    def run(self, dx):  # dx - изменение дистанции, увеличивает x_distance на dx
        self.x_distance += dx

class Eagle:            # класс описывающий орла
    y_distance = 0      # высота полёта
    sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл (отсылка)

    def fly(self, dy):  # где dy - изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):   #- где dx и dy изменения дистанции.
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):
        print(self.sound)

pegasus1 = Pegasus()
#print(Pegasus.mro())
print(pegasus1.get_pos())
pegasus1.move(12, 6)
print(pegasus1.get_pos())
pegasus1.move(-3, 6)
print(pegasus1.get_pos())
pegasus1.voice()