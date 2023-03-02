class Cargo_requirement:
    cargo_type = ''
    cargo_require = ''
    def __init__(self,cargo_type, cargo_require):
        self.cargo_type = cargo_type
        self.cargo_require = cargo_require
    def get_cargo_type(self):
        return self.cargo_type
    def get_cargo_require(self):
        return self.cargo_require
    def set_cargo_type(self,cargo_type):
         self.cargo_type = cargo_type
    def set_cargo_require(self,cargo_require):
        self.cargo_require = cargo_require