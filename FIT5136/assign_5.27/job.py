'''
    this is class shuttle, it contains some information of Job
'''
class Job:
    job_name = ''
    job_desc = ''
    def __init__(self, job_name,job_desc):
        self.job_name = job_name
        self.job_desc = job_desc

    def get_job_name(self):
        return self.job_name
    def get_job_desc(self):
        return self.job_desc
    def set_job_name(self,job_name):
        self.job_name = job_name
    def set_job_desc(self, job_desc):
        self.job_desc = job_desc