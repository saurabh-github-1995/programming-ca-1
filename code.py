#initializing empty student list which will containe number of dictionaries of student data
studentsList=[{"name":"Saurabh","number":11111111,"grade":"56"}]

#function for sorting student list using bubble sort and recursion
def sortList():
    length=len(studentsList)
    for i in range(length-1):
        if(studentsList[i+1]["number"]<studentsList[i]["number"]):
           studentsList[i],studentsList[i+1]=studentsList[i+1],studentsList[i]
           sortList()

#function for mregisterenig stuentd one at a time
def registerStudenrs(student):
    
    studentsList.append(student)
    sortList()
    #sortList2(student)

#function for student with lowest number
def retrive():
    return studentsList[0]

#Second Logic for sorting
def sortList2(student):
    if(len(studentsList)!=0 and student["number"]>studentsList[-1]["number"] ):
       
        studentsList.append(student)
    else:
        for i in range(len(studentsList)):
            if(student["number"]<studentsList[i]["number"]):
                studentsList.insert(i,student)
                break;
                
                
                
                
                
                
                
                
                
                
                
        ArrayList<Result>resultArrayList=new ArrayList<Result>();
        List<String>ansList=new ArrayList<String>(); 
        Map<Integer, String> map = new HashMap<>();
        for(int i=0;i<events1.size();i++){
            Result r=new Result();
            if(events1.get(i).contains("+")){
                
                String result=events1.get(i).replaceAll("[^0-9]+", " ").trim();
                
                String[] splited = result.split(" ");
                int resultInt=Integer.parseInt(splited[0]);
                /*for(int j=0;j<splited.length;j++){
                    resultInt=Integer.parseInt(splited[j])+resultInt;
                    
                }*/
                
                r.setEvent(events1.get(i));
                r.setTime(resultInt);
                r.setTeamName(team1);
                resultArrayList.add(r);
                
            }else if(events1.get(i).matches(".*\\d.*")){
                r.setEvent(events1.get(i));
                r.setTime(Integer.parseInt(events1.get(i).replaceAll("[^0-9]+", " ").trim()));
                r.setTeamName(team1);
                resultArrayList.add(r);
                
            }
        }
        for(int i=0;i<events2.size();i++){
            Result r=new Result();
            if(events2.get(i).contains("+")){
                
                String result=events2.get(i).replaceAll("[^0-9]+", " ").trim();
                

                String[] splited = result.split(" ");
                int resultInt=0;
                for(int j=0;j<splited.length;j++){
                    resultInt=Integer.parseInt(splited[j])+resultInt;
                    
                }
                r.setEvent(events2.get(i));
                r.setTime(resultInt);
                r.setTeamName(team2);
                resultArrayList.add(r);
            }else if(events2.get(i).matches(".*\\d.*")){
                r.setEvent(events2.get(i));
                r.setTime(Integer.parseInt(events2.get(i).replaceAll("[^0-9]+", " ").trim()));
                r.setTeamName(team2);
                resultArrayList.add(r);
               
            }
        }
    
    //System.out.println(Collections.sort(resultArrayList));

    
    List<String> finalResultList = new ArrayList<String>();
    ArrayList<Result>resultArrayList1=new ArrayList<Result>();
    //resultArrayList1.add(resultArrayList.get(0));
    //finalResultList.add(resultArrayList.get(0).getTeamName()+" "+resultArrayList.get(0).getEvent());
     
     for(int m=0;m<resultArrayList.size();m++){
         System.out.println(resultArrayList.size()); 
           
            
        if(m==0){
            
             resultArrayList1.add(resultArrayList.get(m)); 
        }else{
            for(int j=0;j<resultArrayList1.size();j++){
              if(resultArrayList.get(m).getTime()<resultArrayList1.get(j).getTime()){
                  resultArrayList1.add(j,resultArrayList.get(m));
              }else{
                  resultArrayList1.add(j+1,resultArrayList.get(m));
              }
          } 

        
        }
           
        
         
     }

    

     for(int k=0;k<resultArrayList1.size();k++){
            String str="";
            str=str+resultArrayList.get(k).getTeamName()+" "+resultArrayList.get(k).getEvent();
            finalResultList.add(str);
     }
    
    return finalResultList;

    }

}









    times = []
    for event in events1:
        times.append(re.findall(r'\d | \d+\d', event).strip())
    for event in events2:
        times.append(re.findall(r'\d | \d+\d', event).strip())

    for element in times:
        if type(element) == list:
            element = sum(int(i) for i in element)
    
    print(times)