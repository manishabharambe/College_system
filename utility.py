import random


from students import Students
def generate_name():
    s = ""
    for i in range(random.randint(4,10)):
        n = chr((64 + random.randint(1,26)))
        s += n
    return s.title()
#     print(s)
# generate_name()

def generate_n_students(num,class_name):
    stud_list = []
    for i in range(1,num+1):
        s = class_name(stud_id=100+i,stud_name=generate_name(),stud_age=random.randint(17,22),stud_marks=random.randint(32,100))  
        stud_list.append(s) 
        # print(stud_list) 
    return stud_list
# print(generate_n_students(5,Students))

