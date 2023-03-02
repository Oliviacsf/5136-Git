'''
    this is class shuttle, it contains some information of Jobs
'''
from job import Job
class Jobs:
    jobs_list = []

    def __init__(self, jobs_list):
        self.jobs_list = jobs_list

    def get_job_list(self):
        return self.jobs_list
    def set_job_list(self, jobs_list):
        self.jobs_list = jobs_list