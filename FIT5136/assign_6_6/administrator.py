'''
    this is class Administrator, it contains some information of administrator
'''
from staff import  Staff
class Administrator(Staff):
    __passwd = 'admin'
    __username = 'admin'
    def __init__(self, name='', contact_information=''):
        Staff.__init__(self,name='', contact_information='')

    def get_username(self):
        return self.__username
    def get_passwd(self):
        return self.__passwd

