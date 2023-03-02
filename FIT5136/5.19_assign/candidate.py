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
    allergies = ''
    food_preferences = ''
    qualification = []
    work_experience = []
    occupation = []
    computer_skills = []
    languages_spoken = []
    criminal_health_records = ''
    def __init__(self, candidate_id, can_name, date_of_birth, address,nationality,identification_number,
                 gender, allergies, food_preferences, qualification, work_experience, occupation,
                 computer_skills, languages_spoken, criminal_health_records):
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
        self.criminal_health_records = criminal_health_records

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
    def get_criminal_health_records(self):
        return self.criminal_health_records