# programming-ca-1
Steps to run code:
1.Open the final_code.ipynb or final_code.py file and run the code
2.Call addStudentToList() method with data in dictionary format as follows
	addStudentToList({"name":"Saurabh","number":99999991,"subjCode":"ABCDEFG"})
3.For generating data of random students copy and paste below snippets to jupyter
	'''Logic for generating random student numbers and inserting it into the students list'''
	from random import randrange
	for i in range(10000):
		#print(i)
	   
		student={"name":"Saurabh","number": randrange(10000000, 99999999),"subjCode":"ABCDEFG"}
		addStudentToList(student)


	
4.For retriving call retriveStudentData() method
