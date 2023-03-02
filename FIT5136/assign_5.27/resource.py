from shuttle import Shuttle
from warehouse import Warehouse
'''
    this is class Resource, it contains all shuttle and warehouse
'''
class Resource:
    shuttle_list= []
    warehouse_list = []

    def __init__(self, shuttle_list, warehouse_list):
        self.shuttle_list = shuttle_list
        self.warehouse_list = warehouse_list

    def get_shuttle_list(self):
        return self.shuttle_list
    def get_warehouse_list(self):
        return self.warehouse_list
    def set_shuttle_list(self, shuttle_list):
        self.shuttle_list = shuttle_list
    def set_warehouse_list(self, warehouse_list):
        self.warehouse_list = warehouse_list