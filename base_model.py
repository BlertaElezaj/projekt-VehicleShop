from enum import Enum
class Vehicle:
    def __init__(self, id, manufacturer, model, horsePower, price, color, mileage, productionYear, transmission, fuelType):
        self.__id = id
        self.__manufacturer = manufacturer
        self.__model = model
        self.__horsePower = horsePower
        self.__price = price
        self.__color = color
        self.__mileage = mileage
        self.__productionYear = productionYear
        self.__transmission = transmission
        self.__fuelType = fuelType

    # Getters
    def get_id(self):
        return self.__id
    
    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_model(self):
        return self.__model
    
    def get_horsePower(self):
        return self.__horsePower
    
    def get_price(self):
        return self.__price
    
    def get_color(self):
        return self.__color
    
    def get_mileage(self):
        return self.__mileage
    
    def get_productionYear(self):
        return self.__productionYear
    
    def get_transmission(self):
        return self.__transmission
    
    def get_fuelType(self):
        return self.__fuelType

    # Setters
    def set_id(self, id):
        self.__id = id
    
    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
    
    def set_model(self, model):
        self.__model = model
    
    def set_horsePower(self, horsePower):
        self.__horsePower = horsePower
    
    def set_price(self, price):
        self.__price = price
    
    def set_color(self, color):
        self.__color = color
    
    def set_mileage(self, mileage):
        self.__mileage = mileage
    
    def set_productionYear(self, productionYear):
        self.__productionYear = productionYear
    
    def set_transmission(self, transmission):
        self.__transmission = transmission
    
    def set_fuelType(self, fuelType):
        self.__fuelType = fuelType


class Car:
    def __init__(self, Manufacturer, Color, FuelType, Transmission):
        self.__Manufacturer = Manufacturer
        self.__Color = Color
        self.__FuelType = FuelType
        self.__Transmission = Transmission

    # Getters
    def get_Manufacturer(self):
        return self.__Manufacturer
    
    def get_Color(self):
        return self.__Color
    
    def get_FuelType(self):
        return self.__FuelType
    
    def get_Transmission(self):
        return self.__Transmission

    # Setters
    def set_Manufacturer(self, Manufacturer):
        self.__Manufacturer = Manufacturer
    
    def set_Color(self, Color):
        self.__Color = Color
    
    def set_FuelType(self, FuelType):
        self.__FuelType = FuelType
    
    def set_Transmission(self, Transmission):
        self.__Transmission = Transmission

