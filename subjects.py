from base_file import Base_class



class Subjects(Base_class):
    def __init__(self,sid,sname,is_pract):
        self.subid=sid
        self.subname=sname
        self.subpract=is_pract
        
