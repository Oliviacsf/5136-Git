'''
    this is class shuttle, it contains some information of Shuttle
'''
class Shuttle:
    shuttle_id = 0
    shuttle_name = ''
    shuttle_manufacturing_year = ''
    fuel_capacity = ''
    passenger_capacity = 0
    cargo_capacity = 0
    travel_speed = 0
    origin = ''
    def __init__(self, shuttle_id,name, manufacturing_year, fuel_capacity, passenger_capacity,cargo_capacity,travel_speed, origin):
        self.shuttle_id = shuttle_id
        self.shuttle_name = name
        self.shuttle_manufacturing_year = manufacturing_year
        self.fuel_capacity = fuel_capacity
        self.passenger_capacity = passenger_capacity
        self.cargo_capacity = cargo_capacity
        self.travel_speed = travel_speed
        self.origin = origin
    def get_shuttle_id(self):
        return self.shuttle_id
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
    def get_origin(self):
        return self.origin


