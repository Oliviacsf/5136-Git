'''
    this is the class of coordinator, it contains some information of coordinator
'''
from staff import  Staff
import pandas as pd
coor_data = pd.read_csv('./database/missionCoordinators.csv')

class Coordinator(Staff):
    __passwd = 'coor'
    __username = coor_data['employee name'].to_list()
    def __init__(self, name='', contact_information=''):
        Staff.__init__(self,name='', contact_information='')

    def get_username(self):
        return self.__username
    def get_passwd(self):
        return self.__passwd


