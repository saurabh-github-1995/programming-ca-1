'''In this code i have implemented sorting logic in two ways
1st is using bubble sort and recursion. But it is not efficeint at all because every time I append elemnt at the last
of list and then calls bubble sort function
In second logic i am doing more like a inserting sort. In this I find a correct index before inserting an element
so it is more efficient than bubble sort

'''
#initializing empty student list which will containe number of dictionaries of student data
studentsList=[{"name":"Saurabh","number":11111111,"grade":"56"}]

#function for sorting student list using bubble sort and recursion
def sortList():
    length=len(studentsList)
    for i in range(length-1):
        if(studentsList[i+1]["number"]<studentsList[i]["number"]):
           studentsList[i],studentsList[i+1]=studentsList[i+1],studentsList[i]
           sortList()

#function for registerenig stuentd one at a time
def registerStudenrs(student):
    
    studentsList.append(student)
    sortList()
    #sortList2(student)

#function for student with lowest number
def retrive():
    return studentsList[0]

#Second Logic for sorting i.e like insertion sort
def sortList2(student):
    if(len(studentsList)!=0 and student["number"]>studentsList[-1]["number"] ):
       
        studentsList.append(student)
    else:
        for i in range(len(studentsList)):
            if(student["number"]<studentsList[i]["number"]):
                studentsList.insert(i,student)
                break;
                
                
#code for adding number of studentrs to list               
n=11111111
for i in range(10):
    #print(i)
    n=n+i
    student={"name":"Saurabh","number": i,"grade":"56"}
    registerStudenrs(student) 

#code for adding one student at a time            
student={"name":"Saurabh","number":42882,"grade":"56"}
sortList2(student)    