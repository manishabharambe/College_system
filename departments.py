from base_file import Base_class


class Departments(Base_class):
    def __init__(self,did,dname,HOD,no_of_studs):
        self.deptid=did
        self.deptname=dname
        self.deptprinci=HOD
        self.deptstrength=no_of_studs
        self.stud_list = None
        self.studs=[]
        


