from shuttle import Shuttle
'''
    this is class Resource_requirement, it contains shuttle and cargo from mission
'''
class Resource_requirement:
    shuttle = Shuttle()
    cargo_requirements = {}
    cargo_purpose = ''
    def __init__(self, shuttle,cargo_requirements,cargo_purpose):
        self.shuttle = shuttle
        self.cargo_requirements = cargo_requirements
        self.cargo_purpose = cargo_purpose

    def get_shuttle(self):
        return self.shuttle
    def get_cargo_requirements(self):
        return self.cargo_requirements
    def get_cargo_purpose(self):
        return self.cargo_purpose
    def set_shutle(self, shuttle):
        self.shuttle = shuttle
    def set_cargo_requirements(self, cargo_requirements):
        self.cargo_requirements = cargo_requirements
    def set_cargo_purpose(self, cargo_purpose):
        self.cargo_purpose = cargo_purpose
