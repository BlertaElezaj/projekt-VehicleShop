from enum import Enum

class Manufacturer(Enum):
    AUDI = 1
    BMW = 2
    VW = 3
    HONDA = 4
    SKODA = 5

class Color(Enum):
    BLACK = 1
    WHITE = 2
    RED = 3
    YELLOW = 4
    GRAY = 5
    BLUE = 6
    BROWN = 7

class FuelType(Enum):
    GASOLINE = 1
    DIESEL_FUEL = 2

class Transmission(Enum):
    AUTOMATIC = 1
    MANUAL = 2
