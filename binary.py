"""studentsData=[{"name":"Saurabh","number":1,"grade":"56"},
         {"name":"Saurabh","number":2,"grade":"56"},
         {"name":"Saurabh","number":3,"grade":"56"},
         {"name":"Saurabh","number":4,"grade":"56"},
         {"name":"Saurabh","number":6,"grade":"56"}]"""

studentsData=[]
n=11111111
for i in range(10000000):
    #print(i)
    n=n+i
    student={"name":"Saurabh","number": i,"grade":"56"}
    studentsData.append(student)

def insertDataAtSpecificPostion(targetStudentNo,startIndex,lastIndex):
    print(startIndex,lastIndex)
    if(startIndex>lastIndex):
        studentsData.insert(startIndex,studentObj)
        #print(startIndex)
        return startIndex
    else:
        midpointIndex=startIndex+(lastIndex-startIndex)//2
        if(studentsData[midpointIndex]["number"]==targetStudentNo):
            print("number already exist")
            return midpointIndex
        else:
            if(targetStudentNo<studentsData[midpointIndex]["number"]):
                insertDataAtSpecificPostion(targetStudentNo,startIndex,midpointIndex-1)
            else:
                insertDataAtSpecificPostion(targetStudentNo,midpointIndex+1,lastIndex)
                

def addStudentToList(studentObj):
    insertDataAtSpecificPostion(studentObj['number'],0,len(studentsData))
    
    
    
        