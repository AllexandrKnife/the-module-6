import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True

    @staticmethod
    def lay_eggs():
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self.move(0, 0, -dz / 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = PoisonousAnimal._DEGREE_OF_DANGER

    def speak(self):
        print(self.sound)

# Пример работы программы
db = Duckbill(10)

print(db.live)  # True
print(db.beak)  # True

db.speak()  # Click-click-click
db.attack()  # Be careful, i'm attacking you 0_0

db.move(1, 2, 3)
db.get_cords()  # X: 10 Y: 20 Z: 30
db.dive_in(6)
db.get_cords()  # X: 10 Y: 20 Z: 0.0

db.lay_eggs()  # Here are(is) <случайное число от 1 до 4> eggs for you
