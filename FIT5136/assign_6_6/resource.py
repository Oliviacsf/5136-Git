from shuttle import Shuttle
from mission import Mission
from warehouse import Warehouse
from pprint import pprint
import pandas as pd
'''
    this is class Resource, it contains all shuttle and warehouse
'''
can_name = pd.read_csv('./database/candidates.csv')


mission_data = pd.read_csv('./database/mission_2.csv')
mission_data_1 = mission_data.iloc[0].to_list()
mission_data_2 = mission_data.iloc[1].to_list()
mission_data_3 = mission_data.iloc[2].to_list()
mission_1 = Mission(mission_data_1[1],mission_data_1[2],mission_data_1[3],mission_data_1[4],mission_data_1[5],
                    mission_data_1[6],mission_data_1[7],mission_data_1[8],mission_data_1[9],mission_data_1[10],
                    mission_data_1[11],mission_data_1[12])
mission_2 = Mission(mission_data_2[1],mission_data_2[2],mission_data_2[3],mission_data_2[4],mission_data_2[5],
                    mission_data_2[6],mission_data_2[7],mission_data_2[8],mission_data_2[9],mission_data_2[10],
                    mission_data_2[11],mission_data_2[12])
mission_3 = Mission(mission_data_3[1],mission_data_3[2],mission_data_3[3],mission_data_3[4],mission_data_3[5],
                    mission_data_3[6],mission_data_3[7],mission_data_3[8],mission_data_3[9],mission_data_3[10],
                    mission_data_3[11],mission_data_2[12])


shuttle_1 = Shuttle(765	,'magna. Sed','10/04/2018',	'977899900',249	,502,31837,	'Russian Federation')
shuttle_2 = Shuttle(770	,'dapibus gravida.','04/17/2014','922124065',249,1203,34676,'United Kingdom')
shuttle_3 = Shuttle(775,'tristique neque','09/16/2012',	'604094652',277,1697,30552,	'Russian Federation')
shuttle_4 = Shuttle(780,'magna a','01/24/2010',	'3365269',260,779,30930,'India')
shuttle_5 = Shuttle(785,'accumsan convallis','06/16/2011','578248695',248,1054,34503,'Australia')

class Resource:
    shuttle_list_name= ['1. magna. Sed','2. dapibus gravida.','3. tristique neque','4. magna a','5. accumsan convallis']
    shuttle_list = [shuttle_1,shuttle_2,shuttle_3,shuttle_4,shuttle_5]
    mission_list_name = ['1:7003', '2:7006','3:7009']
    mission_list = [mission_1,mission_2,mission_3]
    warehouse_list = []
    candidate_name_list = {2176: 'jimmy',
                           2178:'Bianca Espinoza',
                           2180:'Anika Frost',
                           2182:'Kessie Barlow',
                           2184: 'Lawrence Campbell',
                           2186:'Allistair Gilbert',
                           2188: 'Jaden Curtis',
                           2190: 'Alika Reynolds',
                           2192:  'Dante Mcgowan'}



    # def __init__(self, shuttle_list = [], warehouse_list = []):
    #     self.shuttle_list = shuttle_list
    #     self.warehouse_list = warehouse_list
    def get_candidate_name_list(self):
        return self.candidate_name_list
    def get_mission_entity(self,index):
        return self.mission_list[index-1]
    def get_mission_list_name(self):
        return self.mission_list_name
    def get_shuttle_entity(self,index):
        return self.shuttle_list[index]
    def get_shuttle_list_name(self):
        return self.shuttle_list_name
    def get_warehouse_list(self):
        return self.warehouse_list
    def set_shuttle_list(self, shuttle_list):
        self.shuttle_list = shuttle_list
    def set_warehouse_list(self, warehouse_list):
        self.warehouse_list = warehouse_list

# s = Resource()
# pprint(s.candidate_name_list)