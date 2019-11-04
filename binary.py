studentsData=[]
"""n=11111111
for i in range(1000):
    #print(i)
    n=n+i
    student={"name":"Saurabh","number": i,"grade":"56"}
    studentsData.append(student)"""
studentObjGlobal={}
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


def addStudentToList(studentObj):
    global studentObjGlobal 
    studentObjGlobal=studentObj
    insertDataAtSpecificPostion(studentObj['number'],0,len(studentsData))
    
    
def retriveStudentData():
    if(len(studentsData)!=0):
        loweststudent=studentsData[0]
        del studentsData[0]
        return loweststudent
    else:
        return "No data exists"

def removeStudentData():
    del studentsData[0]
        