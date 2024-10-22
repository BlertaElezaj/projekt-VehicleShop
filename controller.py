from base_enums import Color, FuelType, Manufacturer, Transmission
from base_model import Vehicle
from typing import List
import csv

class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def import_vehicles_from_file(self):
        vehicles = []
        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                vehicles.append(self._parse_vehicle_from_row(row))
        return vehicles

    def _parse_vehicle_from_row(self, row):
        id = int(row[0])
        manufacturer = Manufacturer[row[1]]
        model = row[2]
        horsePower = int(row[3])
        price = float(row[4])
        color = Color[row[5]]
        mileage = int(row[6])
        productionYear = int(row[7])
        transmission = Transmission[row[8]]
        fuelType = FuelType[row[9]]
        return Vehicle(id, manufacturer, model, horsePower, price, color, mileage, productionYear, transmission, fuelType)

    def write_vehicles_to_file(self, vehicle_list):
        with open(self.file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for vehicle in vehicle_list:
                csv_writer.writerow([vehicle.get_id(), vehicle.get_manufacturer().name, vehicle.get_model(), vehicle.get_horsePower(), vehicle.get_price(), vehicle.get_color().name, vehicle.get_mileage(), vehicle.get_productionYear(), vehicle.get_transmission().name, vehicle.get_fuelType().name])

class VehicleShopPrinter:
    def print_available_vehicles(self, vehicle_list):
        print("Available Vehicles:")
        for vehicle in vehicle_list:
            print(f"ID: {vehicle.get_id()}, Manufacturer: {vehicle.get_manufacturer().name}")

    def print_vehicle_sold_message(self, vehicle_chosen_id):
        print("\nVehicle with ID", vehicle_chosen_id, "was sold.")
    
    def print_vehicle_id_to_sell_message(self):
        print("\n\n Please enter the number (ID) of the vehicle you want to sell: ")

class VehicleShopProcessor:
    def sell_vehicle(self, vehicle_list, selected_vehicle_id):
        for vehicle in vehicle_list:
            if vehicle.get_id() == selected_vehicle_id:
                vehicle_list.remove(vehicle)
                return
        print("Vehicle with ID", selected_vehicle_id, "not found in the list.")

class VehicleTransformer:
    def transform_data_as_string_array_to_vehicle_objects(self, vehicles_as_string_array: List[str]) -> List[Vehicle]:
        vehicle_list = []
        for vehicle_as_string_array in vehicles_as_string_array:
            vehicle = self.transform_to_vehicle_object(vehicle_as_string_array)
            vehicle_list.append(vehicle)
        return vehicle_list

    def transform_to_vehicle_object(self, vehicle_as_string_array: List[str]) -> Vehicle: 
        vehicle_id = int(vehicle_as_string_array[0])
        manufacturer = self.get_manufacturer_from_string(vehicle_as_string_array[1])
        return Vehicle(vehicle_id, manufacturer)

    def get_manufacturer_from_string(self, manufacturer_as_string):
        for manufacturer in Manufacturer:
            if manufacturer.name == manufacturer_as_string:
                return manufacturer
        raise ValueError("Manufacturer not supported: " + manufacturer_as_string)
