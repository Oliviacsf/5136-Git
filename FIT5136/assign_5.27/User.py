class User:
    username = ''
    passwd = ''
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd

    def get_username(self):
        return self.username
    def get_psd(self):
        return self.passwd
    def set_username(self,username):
        self.username = username
    def set_psd(self, passwd):
        self.passwd = passwd