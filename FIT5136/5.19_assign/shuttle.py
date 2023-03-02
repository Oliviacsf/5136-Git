'''
    this is class shuttle, it contains some information of Shuttle
'''
class Shuttle:
    shuttle_name = ''
    shuttle_manufacturing_year = ''
    fuel_capacity = 0
    passenger_capacity = 0
    cargo_capacity = 0
    travel_speed = 0
    def __init__(self, name, manufacturing_year, fuel_capacity, payload_capacity,travel_speed):
        self.shuttle_name = name
        self.shuttle_manufacturing_year = manufacturing_year
        self.fuel_capacity = fuel_capacity
        self.payload_capacity = payload_capacity
        self.travel_speed = travel_speed
    def get_name(self):
        return self.shuttle_name
    def get_man_year(self):
        return self.shuttle_manufacturing_year
    def get_fuel_capacity(self):
        return self.fuel_capacity
    def get_passenger_capacity(self):
        return self.passenger_capacity
    def get_cargo_capacity(self):
        return self.cargo_capacity
    def get_travel_speed(self):
        return self.travel_speed


