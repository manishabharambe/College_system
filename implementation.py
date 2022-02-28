# from os import terminal_size
from base_file import Base_class
from college import College
from departments import Departments
from students import Students
from subjects import Subjects
from utility import generate_n_students
import random


c1 = College(cid=3144,cname="UMIT",princi="Dr. Mathew",no_of_studs= 60)

d1 = Departments(did=31441,dname="IT",HOD = "V Patil",no_of_studs=10)
d2 = Departments(did=31442,dname="COMP",HOD = "samita",no_of_studs=10)
d3 = Departments(did=31443,dname="MECH",HOD = "manshree",no_of_studs=10)
d4 = Departments(did=31444,dname="ETC",HOD = "Vrushali",no_of_studs=10)
d = [d1,d2,d3,d4]

c1.Departments.extend([d1,d2,d3,d4])
# print(c1)
studs = generate_n_students(40,Students)
# print("------------------")
# print(studs)


d1.studs.extend(studs[0:10])
d2.studs.extend(studs[0:10])
d3.studs.extend(studs[0:10])
d4.studs.extend(studs[0:10])

for i in d:
    i.stud_list = len(i.studs)

#  subject add remaining
sub = ["MATHS","PHYSICS","CHEMISTRY","BEE","CPP"]
sub1 =Subjects(sid=1120,sname="MATHS",is_pract=False)
sub2 =Subjects(sid=1121,sname="PHYSICS",is_pract=True)
sub3 =Subjects(sid=1122,sname="CHEMISTRY",is_pract=True)
sub4 =Subjects(sid=1123,sname="BEE",is_pract=False)
sub5 =Subjects(sid=1124,sname="CPP",is_pract=True)

list_subj = [sub1,sub2,sub3,sub4,sub5]
for i in studs:
    random_studs = list_subj[0:random.randint(1,5)]
    # print(random_studs)
    i.studsubjects.extend(random_studs)
# print("All students:---",studs)
   
print("----------------------------TASK 1 ----------------------------")
def Task1():
    """To search all students staring with given"""
    letter = input("enetr the starting alphabet of student").upper()
    x = list(filter(lambda x:x.studname.startswith(letter),studs))
    print("Task 1---:",x)
Task1()

print("----------------------------TASK 2 ----------------------------")
subj_ch = input("subject name:").upper()
def Task2(choice):
    """ To Display subject details using sub name"""
    x=list(filter(lambda x:x.subname==subj_ch,list_subj))
    print(x)
Task2(subj_ch)

print("----------------------------TASK 3 ----------------------------")
print("To collect all students with same subject and calculate average")
def Task3(subject):
    """To collect all students with same subject and calculate average"""
    sub = []
    marks = []
    for dpt in c1.Departments:
        for stud in dpt.studs:
            l = list(map(lambda x: x.subname, stud.studsubjects))  
            if subject in l:
                sub.append({"Department":dpt.deptname ,"Student Name": stud.studname})
                marks.append(stud.stud_marks)

    print(sub, len(sub))
    print(marks,len(marks))
    print("average of marks is:-",sum(marks)/len(marks))

Task3(subj_ch)
 
print("----------------------------TASK 4 ----------------------------")
print("if students marks is >50, return student list")
def Task4():
    """if students marks is >50, return student list"""
    marks_stud = []
    for dpt in c1.Departments:
        for stud in dpt.studs:
            l = list(map(lambda x:x.stud_marks,studs))
            # print("l is:",l,len(l))
            if stud.stud_marks>50:
                marks_stud.append({"Department":dpt.deptname ,"Student Name": stud.studname})
    print(marks_stud, len(marks_stud))

Task4()

print("----------------------------TASK 5 ----------------------------")
print("list out Students having 4 subjects count")
def Task5():
    """list out Students having 4 subjects count"""
    sub_stud =[]
    for dpt in c1.Departments:
        for stud in dpt.studs:
            l = list(map(lambda x: x.subname, stud.studsubjects))  
            if len(l)== 4:
              sub_stud.append({"student id":stud.studid,"Student Name": stud.studname})
    print("students having 4 subjects are:\n",sub_stud)
Task5()

print("----------------------------TASK 6----------------------------")
print("Enter the id of students to delete details")
id_ch = int(input("Enter the id of students to delete details:"))
def Task6(id_input):
    """To delete student entry"""
    # print("before",studs)
    for dpt in c1.Departments:
        for i in studs:
            if i.studid == id_input:
                x = studs.index(i)
                # print("X",x)
                del studs[x]
    print("after deleting student with id",id_ch,studs)

Task6(id_ch)
