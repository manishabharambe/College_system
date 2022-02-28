
from typing import NamedTuple


from base_file import Base_class

class College(Base_class):
    def __init__(self,cid,cname,princi,no_of_studs):
        self.clgid=cid
        self.clgname=cname
        self.clgprinci=princi
        self.clgstrength=no_of_studs
        self.Departments = []

if __name__ == "__main__":
    c1 = College(3144,"UMIT","Dr. Mathew",60)
    print(c1)