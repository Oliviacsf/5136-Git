class Employment_requirement:
    emp_requirement_name = ''

    def __init__(self, emp_requirement_name):
        self.emp_requirement_name = emp_requirement_name

    def get_emp_requirement_name(self):
        return self.emp_requirement_name

    def set_emp_requirement(self, jobs_requirement):
        self.emp_requirement_name = jobs_requirement
