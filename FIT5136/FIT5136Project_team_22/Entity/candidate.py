from datetime import date
import pandas as pd
"""
    this is class candidate, it contains some information of candidate
"""

can_data = pd.read_csv('./database/candidates.csv')

# can_data['name'][can_data['identification'] == 2176] = 'jack'

class Candidate:
    candidate_id_list = list(map(str, can_data['identification'].to_list()))
    candidate_id = 0
    __passwd = '12345'
    can_name = ''
    date_of_birth = ''
    address = ''
    nationality =''
    identification_type =''
    gender =''
    allergies = ''
    food_preferences = ''
    qualification = ''
    work_experience = ''
    occupation = ''
    computer_skills = ''
    languages_spoken = ''
    criminal_records = False
    health_record = False
    received_offer = ''
    def __init__(self, candidate_id=0, can_name='', date_of_birth='', address='',nationality='',identification_type='',
                 gender='', allergies='', food_preferences='', qualification='', work_experience='', occupation='',
                 computer_skills='', languages_spoken='', criminal_records=False,health_record=False,received_offer = ''):
        self.candidate_id = candidate_id
        self.can_name = can_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.nationality = nationality
        self.identification_number = identification_type
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
        self.received_offer = received_offer

    def get_received_offer(self):
        return can_data['received_offer'][can_data['identification'] == self.candidate_id].tolist()[0]

    def get_candidate_id(self):
        return self.candidate_id

    def get_passwd(self):
        return self.__passwd
    def get_can_name(self):
        return can_data['name'][can_data['identification'] == self.candidate_id].tolist()[0]

    def get_date_of_birth(self):
        return can_data['date of birth'][can_data['identification'] == self.candidate_id].tolist()[0]

    def get_address(self):
        return can_data['street'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_nationality(self):
        return can_data['country'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_identification_type(self):
        return can_data['identification type'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_gender(self):
        return can_data['gender'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_allergies(self):
        return can_data['allergies'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_food_preferences(self):
        return can_data['food preferences'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_qualification(self):
        return can_data['qualifications'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_work_experience(self):
        return can_data['years of work experience'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_occupation(self):
        return can_data['occupation'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_computer_skills(self):
        return can_data['computer skills'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_languages_spoken(self):
        return  can_data['languages known'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_criminal_records(self):
        return  can_data['criminal_records'][can_data['identification'] == self.candidate_id].tolist()[0]
    def get_health_record(self):
        return  can_data['health_record'][can_data['identification'] == self.candidate_id].tolist()[0]

    def set_candidate_id(self, candidate_id):
        self.candidate_id = int(candidate_id)
    def set_can_name(self, can_name):
        self.can_name = str(can_name)
        can_data['name'][can_data['identification'] == self.candidate_id] = can_name
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = str(date_of_birth)
        can_data['date of birth'][can_data['identification'] == self.candidate_id] = date_of_birth
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_address(self, address):
        self.address = str(address)
        can_data['street'][can_data['identification'] == self.candidate_id] = address
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_nationality(self, nationality):
        self.nationality = str(nationality)
        can_data['country'][can_data['identification'] == self.candidate_id] = nationality
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_identification_type(self, identification_type):
        self.identification_type = str(identification_type)
        can_data['identification type'][can_data['identification'] == self.candidate_id] = identification_type
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_gender(self, gender):
        self.gender = str(gender)
        can_data['gender'][can_data['identification'] == self.candidate_id] = gender
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_allergies(self,allergies):
        self.allergies = str(allergies)
        can_data['allergies'][can_data['identification'] == self.candidate_id] = allergies
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_food_preferences(self, food_preferences):
        self.food_preferences = str(food_preferences)
        can_data['food preferences'][can_data['identification'] == self.candidate_id] = food_preferences
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_qualification(self, qualification):
        self.qualification = str(qualification)
        can_data['qualifications'][can_data['identification'] == self.candidate_id] = qualification
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_work_experience(self, work_experience):
        self.work_experience = str(work_experience)
        can_data['years of work experience'][can_data['identification'] == self.candidate_id] = work_experience
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_occupation(self, occupation):
        self.occupation = str(occupation)
        can_data['occupation'][can_data['identification'] == self.candidate_id] = occupation
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_computer_skills(self,computer_skills ):
        self.computer_skills = str(computer_skills)
        can_data['computer skills'][can_data['identification'] == self.candidate_id] = computer_skills
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_languages_spoken(self, languages_spoken):
        self.languages_spoken = str(languages_spoken)
        can_data['languages known'][can_data['identification'] == self.candidate_id] = languages_spoken
        can_data.to_csv('./database/candidates.csv', index=False)
    def set_received_offer(self, received_offer):
        self.received_offer = str(received_offer)
        can_data['received_offer'][can_data['identification'] == self.candidate_id] += ',' + received_offer
        can_data.to_csv('./database/candidates.csv', index=False)
# c
