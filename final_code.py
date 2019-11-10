#GITHUB REPO : https://github.com/saurabh-github-1995/programming-ca-1
'''
In this logic I am making use of Binary search which makes it much more efficient than my
other logics where i have used recursion.
For inserting element even at 10M-1th index it takes much much less time beacuse it directly breaks list into two halves
based on the value of current student number.
It works at a time coplexity of O(Log n)
'''

#Array for storing students data in a dictionary format i.e list of dictionaries
studentsData=[]

#Dictionary for storing data
studentObjGlobal={}

#Method for finding the index in existing list at which new student will be added
def insertDataAtSpecificPostion(targetStudentNo,startIndex,lastIndex):
    if(len(studentsData)==0):
        studentsData.append(studentObjGlobal)
    else:
        if(targetStudentNo>studentsData[-1]["number"]):
            studentsData.append(studentObjGlobal)
        else:

            if(startIndex>lastIndex):#end-start+1 <= 0:
                studentsData.insert(startIndex,studentObjGlobal)
                #print(startIndex)
                return startIndex
            else:
                midpointIndex=startIndex+(lastIndex-startIndex)//2
                if(studentsData[midpointIndex]["number"]==targetStudentNo):
                    print("Student record with number already exist")
                    return midpointIndex
                else:
                    if(targetStudentNo<studentsData[midpointIndex]["number"]):
                        insertDataAtSpecificPostion(targetStudentNo,startIndex,midpointIndex-1)
                    else:
                        insertDataAtSpecificPostion(targetStudentNo,midpointIndex+1,lastIndex)

#this method recieves the dictionary of student and pass it to the above method for inserting in list
def addStudentToList(studentObj):
    global studentObjGlobal 
    studentObjGlobal=studentObj
    if len(studentObj['subjCode'])==7:
        insertDataAtSpecificPostion(studentObj['number'],0,len(studentsData))
    else:
        return "Plase enter a subject code exactly of 7 characters"

        
#this function returns the first element from list deleting that element
#it always returns the 0th index because list is sorted always
def retriveStudentData():
    if(len(studentsData)!=0):
        loweststudent=studentsData[0]
        del studentsData[0]
        return loweststudent
    else:
        return "No Records exists"
        
        
        
'''Logic for generating random student numbers and inserting it into the students list
from random import randrange
for i in range(10):
    #print(i)
   
    student={"name":"Saurabh","number": randrange(10000000, 99999999),"subjCode":"ABCDEFGH"}
    addStudentToList(student)

#Calling function for adding students     
addStudentToList({"name":"Saurabh","number":99999991,"subjCode":"ABCDEFGH"})




#Calling function for retriving students
retriveStudentData()'''