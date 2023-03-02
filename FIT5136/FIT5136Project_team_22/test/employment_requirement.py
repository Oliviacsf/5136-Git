class Employment_requirement:
    emp_requirement = {}

    def __init__(self, emp_requirement_name, emp_requirement_number):
        self.emp_requirement[emp_requirement_name] = emp_requirement_number

    def get_jobs_requirement(self):
        return self.emp_requirement

    def set_jobs_requirement(self, jobs_requirement):
        self.emp_requirement = jobs_requirement
