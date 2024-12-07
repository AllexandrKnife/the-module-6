class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'yellow']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: \033[94m{self.__model}\033[0m" 

    def get_horsepower(self):
        return f"Мощность двигателя: \033[93m{self.__engine_power}\033[0m" 

    def get_color(self):
        color_map = {
            'blue': '\033[94m',
            'red': '\033[91m',
            'green': '\033[92m',
            'black': '\033[30m',
            'white': '\033[97m',
            'yellow': '\033[93m'
        }
        color_code = color_map.get(self.__color.lower(), '')
        return f"Цвет: {color_code}{self.__color}\033[0m"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: \033[92m{self.owner}\033[0m")  

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"\033[91mНельзя сменить цвет на {new_color}\033[0m") 


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Пример использования
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
