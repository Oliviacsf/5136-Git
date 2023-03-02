from datetime import date
from resource_requirement import Resource_requirement
from employment_requirement import Employment_requirement
class Mission:
    mission_id = ''
    mission_name= ''
    mission_description= ''
    country_of_origin= ''
    countries_allowed_list = []
    criteria_list= []
    launch_date: date
    destination_location= ''
    mission_duration= ''
    mission_status= ''
    recruitment_status = False
    selection = {}
    resource_requirement = Resource_requirement
    employment_requirement = Employment_requirement

    def __init__(self,mission_id, mission_name, mission_description, country_of_origin,
    countries_allowed_list,criteria_list, launch_date, destination_location,
    mission_duration,mission_status,recruitment_status,selection,resource_requirement,employment_requirement,
    ):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.mission_description = mission_description
        self.country_of_origin = country_of_origin
        self.countries_allowed_list = countries_allowed_list
        self.criteria_list = criteria_list
        self.launch_date = launch_date
        self.destination_location = destination_location
        self.mission_duration = mission_duration
        self.mission_status = mission_status
        self.recruitment_status = recruitment_status
        self.selection = selection
        self.resource_requirement = resource_requirement
        self.employment_requirement = employment_requirement

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
    def get_recruitment_status(self):
        return self.recruitment_status
    def get_selection(self):
        return self.selection
    def get_criteria_list(self):
        return self.criteria_list
    def get_employment_requirement(self):
        return self.employment_requirement
    def set_mission_id(self, mission_id):
        self.mission_id = mission_id
    def set_mission_name(self,mission_name):
        self.mission_name = mission_name
    def set_mission_description(self,mission_description):
        self.mission_description = mission_description
    def set_country_of_origin(self,country_of_origin):
        self.country_of_origin = country_of_origin
    def set_countries_allowed_list(self,countries_allowed_list):
        self.countries_allowed_list = countries_allowed_list
    def set_launch_date(self,launch_date):
        self.launch_date = launch_date
    def set_destination_location(self,destination_location):
        self.destination_location = destination_location
    def set_mission_status(self,mission_status):
        self.mission_status = mission_status
    def set_recruitment_status(self,recruitment_status):
        self.recruitment_status = recruitment_status
    def set_selection(self,selection):
        self.selection = selection
    def set_criteria_list(self,criteria_list):
        self.criteria_list = criteria_list
    def set_employment_requirement(self,employment_requirement):
        self.employment_requirement = employment_requirement