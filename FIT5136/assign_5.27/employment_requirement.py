class Employment_requirement:
    required_jobs_list = []
    jobs_requirement = {}

    def __init__(self,required_jobs_list,jobs_requirement):
        self.required_jobs_list = required_jobs_list
        self.jobs_requirement = jobs_requirement

    def get_required_jobs_list(self):
        return self.required_jobs_list
    def get_jobs_requirement(self):
        return self.jobs_requirement
    def set_required_jobs_list(self, required_jobs_list):
        self.required_jobs_list = required_jobs_list
    def set_jobs_requirement(self, jobs_requirement):
        self.jobs_requirement = jobs_requirement