from datetime import date
#from resource_requirement import Resource_requirement
import pandas as pd
from employment_requirement import Employment_requirement
from job import Job
from cargo_requirement import Cargo_requirement

mission_read_data = pd.read_csv('./database/mission_2.csv')

class Mission:
    mission_id = 0
    mission_name= ''
    mission_description= ''
    country_of_origin= ''
    countries_allowed_list = ''
    coor_name = ''
    # a list stores Job object
    jobs = []
    # a list stores Employment_requirement object
    employment_requirement = {}
    # a list stores Cargo_requirement object
    cargo_require = []
    launch_date = ''
    destination_location = ''
    mission_duration = 0
    mission_status = ''
    has_shuttle = 0
    can_reject = True
    recruitent_status = False

    def __init__(self,mission_id, mission_name, mission_description, country_of_origin,
    countries_allowed_list, coor_name, jobs, employment_requirement, cargo_require, launch_date,
    destination_location, mission_duration , mission_status, has_shuttle, can_reject, recruitent_status
    ):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.mission_description = mission_description
        self.country_of_origin = country_of_origin
        self.countries_allowed_list = countries_allowed_list
        self.coor_name = coor_name
        self.jobs = jobs
        self.employment_requirement = employment_requirement
        self.cargo_require = cargo_require
        self.launch_date = launch_date
        self.destination_location = destination_location
        self.mission_duration = mission_duration
        self.mission_status = mission_status
        self.has_shuttle = has_shuttle
        self.can_reject = can_reject
        self.recruitent_status = recruitent_status

    def get_can_reject(self):
        return self.can_reject

    def get_has_shuttle(self):
        return self.has_shuttle

    def get_cargo_require(self):
        return self.cargo_require

    def get_employe_require(self):
        return self.employees_require

    def get_job_list(self):
        return self.jobs

    def get_coor_name(self):
        return self.coor_name

    def get_mission_id(self):
        return self.mission_id

    def get_mission_name(self):
        return self.mission_name

    def get_mission_description(self):
        return self.mission_description

    def get_country_of_origin(self):
        return self.country_of_origin

    def get_countries_allowed_list(self):
        return self.countries_allowed_list

    def get_launch_date(self):
        return self.launch_date

    def get_destination_location(self):
        return self.destination_location

    def get_mission_status(self):
        return self.mission_status

    def get_mission_duration(self):
        return self.mission_duration

    def set_mission_id(self, mission_id,id):
        mission_read_data.loc[id, 'mission_id'] = mission_id
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.mission_id = mission_id

    def set_mission_name(self,mission_name,id):
        mission_read_data.loc[id, 'mission_name'] = mission_name
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.mission_name = mission_name

    def set_mission_description(self,mission_description,id):
        mission_read_data.loc[id, 'mission_description'] = mission_description
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.mission_description = mission_description

    def set_country_of_origin(self,country_of_origin,id):
        mission_read_data.loc[id, 'country_of_origin'] = country_of_origin
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.country_of_origin = country_of_origin

    def set_countries_allowed_list(self,countries_allowed_list,id):
        mission_read_data.loc[id, 'countries_allowed_list'] = countries_allowed_list
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.countries_allowed_list = countries_allowed_list

    def set_launch_date(self,launch_date,id):
        mission_read_data.loc[id, 'launch_date'] = launch_date
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.launch_date = launch_date

    def set_destination_location(self,destination_location,id):
        mission_read_data.loc[id, 'destination_location'] = destination_location
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.destination_location = destination_location

    def set_mission_status(self,mission_status,id):
        mission_read_data.loc[id, 'mission_status'] = mission_status
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.mission_status = mission_status

    def set_coor_name(self,coor_name,id):
        mission_read_data.loc[id, 'coor_name'] = coor_name
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.coor_name = coor_name

    def set_jobs(self, jobs):
        self.jobs.append(jobs)

    def set_employees_require(self,employ):
        self.employees_require = employ

    def set_caggo_require(self, cargo):
        self.cargo_require = cargo

    def set_mission_duration(self, duration,id):
        mission_read_data.loc[id, 'mission_duration'] = duration
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.mission_duration = duration

    def set_has_shuttle(self, shuttle,id):
        mission_read_data.loc[id, 'has_shuttle'] = shuttle
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.has_shuttle = shuttle

    def set_can_reject(self, can_reject,id):
        mission_read_data.loc[id, 'can_reject'] = can_reject
        mission_read_data.to_csv('./database/mission_2.csv', index=False)
        self.can_reject = can_reject