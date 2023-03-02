'''
    this is class Warehouse, it contains some information of Warehouse
'''
class Warehouse:
    cargo_id = 0
    cargo_name = ''
    cargo_qty = 0
    def __init__(self,cargo_id,cargo_name,cargo_qty):
        self.cargo_id = cargo_id
        self.cargo_name = cargo_name
        self.cargo_qty = cargo_qty

    def get_cargo_id(self):
        return self.cargo_id
    def get_cargo_name(self):
        return self.cargo_name
    def get_cargo_qty(self):
        return self.cargo_qty

    def set_cargo_id(self, cargo_id):
        self.cargo_id = cargo_id
    def set_cargo_name(self, cargo_name):
        self.cargo_name = cargo_name
    def set_cargo_qty(self, cargo_qty):
        self.cargo_qty = cargo_qty