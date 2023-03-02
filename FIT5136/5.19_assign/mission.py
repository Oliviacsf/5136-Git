from datetime import date
class Mission:
    mission_id = ''
    mission_name = ''
    mission_description = ''
    country_of_origin = ''
    list_of_countries_allowed = []
    coordinator = []
    jobs_dictionary = {}
    employment_requirement = {}
    cargo_requirements = {}
    launch_date = date
    destination_location = ''
    mission_duration = ''
    mission_status = ''
    shuttle = []
    recruitment_status = False
    selection = {}
    criteria_dictionary = {}

    def __init__(self,mission_id, mission_name, mission_description, country_of_origin,
    list_of_countries_allowed,coordinator, jobs_dictionary, employment_requirement,
    cargo_requirements,launch_date,destination_location,mission_duration,mission_status,
    shuttle,recruitment_status,selection,criteria_dictionary ):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.mission_description = mission_description
        self.country_of_origin = country_of_origin
        self.list_of_countries_allowed = list_of_countries_allowed
        self.coordinator = coordinator
        self.jobs_dictionary = jobs_dictionary
        self.employment_requirement = employment_requirement
        self.cargo_requirements = cargo_requirements
        self.launch_date = launch_date
        self.destination_location = destination_location
        self.mission_duration = mission_duration
        self.mission_status = mission_status
        self.shuttle = shuttle
        self.recruitment_status = recruitment_status
        self.selection = selection
        self.criteria_dictionary = criteria_dictionary

    def get_mission_id(self):
        return self.get_mission_id()
    def set_mission_id(self,mission_id):
        self.mission_id = mission_id

    def get_mission_name(self):
        return self.mission_name
    def set_mission_name(self, mission_name):
        self.mission_name = mission_name

    def get_mission_description(self):
        return self.mission_description
    def set_mission_description(self,mission_description):
        self.mission_description = mission_description

    def get_country_of_origin(self):
        return self.country_of_origin
    def set_country_of_origin(self,country_of_origin ):
        self.country_of_origin = country_of_origin

    def get_list_of_countries_allowed(self):
        return self.list_of_countries_allowed
    def set_list_of_countries_allowed(self,list_of_countries_allowed):
        self.list_of_countries_allowed = list_of_countries_allowed
    def get_coordinator(self):
        return self.coordinator
    def set_coordinator(self, coordinator):
        self.coordinator = coordinator
    def get_jobs_dictionary(self):
        return self.jobs_dictionary
    def set_jobs_dictionary(self, jobs_dictionary):
        self.jobs_dictionary = jobs_dictionary
    def get_employment_requirement(self):
        return self.employment_requirement
    def set_employment_requirement(self,employment_requirement):
        self.employment_requirement = employment_requirement
    def get_cargo_requirements(self):
        return self.cargo_requirements
    def set_cargo_requirements(self, cargo_requirements):
        self.cargo_requirements = cargo_requirements
    def get_launch_date(self):
        return self.launch_date
    def set_launch_date(self, launch_date):
        self.launch_date = launch_date
    def get_destination_location(self):
        return self.destination_location
    def set_destination_location(self, destination_location):
        self.destination_location = destination_location
    def get_mission_duration(self):
        return self.mission_duration
    def set_mission_duration(self, mission_duration):
        self.mission_duration = mission_duration
    def get_mission_status(self):
        return self.mission_status
    def set_mission_status(self,mission_status ):
        self.mission_status = mission_status
    def get_shuttle(self):
        return self.shuttle
    def set_shuttle(self, shuttle):
        self.shuttle =  shuttle
    def get_recruitment_status(self):
        return self.recruitment_status
    def set_recruitment_status(self,recruitment_status ):
        self.recruitment_status = recruitment_status
    def get_selection(self):
        return self.selection
    def set_selection(self, selection):
        self.selection = selection
    def get_criteria_dictionary(self):
        return self.criteria_dictionary
    def set_criteria_dictionary(self, criteria_dictionary):
        self.criteria_dictionary = criteria_dictionary