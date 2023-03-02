from datetime import date

"""
    this is class candidate, it contains some information of candidate
"""
class Candidate:
    candidate_id = ''
    can_name = ''
    date_of_birth = date
    address = ''
    nationality = ''
    identification_number = 0
    gender = ''
    allergies = []
    food_preferences = ''
    qualification = []
    work_experience = []
    occupation = []
    computer_skills = []
    languages_spoken = []
    criminal_records = False
    health_record = False
    def __init__(self, candidate_id, can_name, date_of_birth, address,nationality,identification_number,
                 gender, allergies, food_preferences, qualification, work_experience, occupation,
                 computer_skills, languages_spoken, criminal_records,health_record):
        self.candidate_id = candidate_id
        self.can_name = can_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.nationality = nationality
        self.identification_number = identification_number
        self.gender = gender
        self.allergies = allergies
        self.food_preferences = food_preferences
        self.qualification = qualification
        self.work_experience = work_experience
        self.occupation = occupation
        self.computer_skills = computer_skills
        self.languages_spoken = languages_spoken
        self.criminal_records = criminal_records
        self.health_record = health_record
    def get_candidate_id(self):
        return self.candidate_id

    def get_can_name(self):
        return self.can_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_address(self):
        return self.address
    def get_nationality(self):
        return self.nationality
    def get_identification_number(self):
        return self.identification_number
    def get_gender(self):
        return self.gender
    def get_allergies(self):
        return self.allergies
    def get_food_preferences(self):
        return self.food_preferences
    def get_qualification(self):
        return self.qualification
    def get_work_experience(self):
        return self.work_experience
    def get_occupation(self):
        return self.occupation
    def get_computer_skills(self):
        return self.computer_skills
    def get_languages_spoken(self):
        return self.languages_spoken
    def get_criminal_records(self):
        return self.criminal_records
    def get_health_record(self):
        return self.health_record

    def set_candidate_id(self, candidate_id):
        self.candidate_id = candidate_id
    def set_can_name(self, can_name):
        self.can_name = can_name
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth
    def set_address(self, address):
        self.address = address
    def set_nationality(self, nationality):
        self.nationality = nationality
    def set_identification_number(self, identification_number):
        self.identification_number = identification_number
    def set_gender(self, gender):
        self.gender = gender
    def set_allergies(self,allergies):
        self.allergies = allergies
    def set_food_preferences(self, food_preferences):
        self.food_preferences = food_preferences
    def set_qualification(self, qualification):
        self.qualification = qualification
    def set_work_experience(self, work_experience):
        self.work_experience = work_experience
    def set_occupation(self, occupation):
        self.occupation = occupation
    def set_computer_skills(self,computer_skills ):
        self.computer_skills = computer_skills
    def set_languages_spoken(self, languages_spoken):
        self.languages_spoken = languages_spoken