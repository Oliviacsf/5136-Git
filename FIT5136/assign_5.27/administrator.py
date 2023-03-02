'''
    this is class Administrator, it contains some information of administrator
'''
from staff import  Staff
class Administrator(Staff):
    __passwd = 'admin'
    def __init__(self, name, contact_information):
        Staff.__init__(name, contact_information)
