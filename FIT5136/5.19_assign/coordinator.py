'''
    this is the class of coordinator, it contains some information of coordinator
'''
class Coordinator:
    coo_user_id = ''
    coo_name = ''
    contact_information = ''
    __coo_password = ''
    def __init__(self, user_id, name, contact_information):
        self.coo_user_id = user_id
        self.coo_name = name
        self.contact_information = contact_information
    def get_name(self):
        return self.coo_name
    def set_name(self, name):
        self.coo_name = name
    def get_user_id(self):
        return self.coo_user_id
    def set_user_id(self, user_id):
        self.coo_user_id = user_id
    def get_contact_info(self):
        return self.contact_information
    def set_contact_info(self):
        return self.contact_information