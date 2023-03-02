'''
    this is class Administrator, it contains some information of administrator
'''
class Administrator:
    admin_user_id = ''
    admin_name = ''
    __admin_password = ''
    def __init__(self, user_id, name):
        self.admin_user_id = user_id
        self.admin_name = name

    def get_user_id(self):
        return self.admin_user_id
    def set_user_id(self, user_id):
        self.admin_user_id = user_id

    def get_name(self):
        return self.admin_name
    def set_name(self, name):
        self.admin_name = name
