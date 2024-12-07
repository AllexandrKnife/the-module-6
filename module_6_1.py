# Базовые классы
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


# Наследуемые классы для животных
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# Наследуемые классы для растений
class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


# Создаем объекты
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выводим начальные значения
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Взаимодействие животных с растениями
a1.eat(p1)
a2.eat(p2)

# Выводим результаты
print(a1.alive)
print(a2.fed)
