#initializing empty student list which will containe number of dictionaries of student data
studentsList=[{"name":"Saurabh","number":11111111,"grade":"56"}]


def sortList():
    length=len(studentsList)
    for i in range(length-1):
        if(studentsList[i+1]["number"]<studentsList[i]["number"]):
           studentsList[i]["number"],studentsList[i+1]["number"]=studentsList[i+1]["number"],studentsList[i]["number"]
           sortList()

#function for mregisterenig stuentd one at a time
def registerStudenrs(student):
    
    #studentsList.append(student)
    sortList2(student)
    
    
#function for student with lowest number
def retrive():
    return studentsList[0]    