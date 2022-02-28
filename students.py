from base_file import Base_class


class Students(Base_class):
    def __init__(self,stud_id,stud_name,stud_age,stud_marks):
        self.studid=stud_id
        self.studname=stud_name
        self.stud_age=stud_age
        self.stud_marks=stud_marks
        self.studsubjects = []

