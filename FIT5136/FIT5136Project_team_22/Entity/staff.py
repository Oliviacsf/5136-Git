'''this is the class of staff'''
class Staff:
    name = ''
    contact_information = ''

    def __init__(self,name,contact_information):
        self.name = name
        self.contact_information = contact_information

    def get_name(self):
        return self.name

    def get_contact_info(self):
        return self.contact_information

    def set_name(self, name):
        self.name = name

    def set_contact_info(self,contact_information ):
        self.contact_information = contact_information



