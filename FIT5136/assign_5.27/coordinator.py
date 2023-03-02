'''
    this is the class of coordinator, it contains some information of coordinator
'''
from staff import  Staff
class Coordinator(Staff):
    __passwd = '123456'

    def __init__(self, name, contact_information):
        Staff.__init__(name, contact_information)




