import random

subjects=["CD","INS","MCWC","DMBI"]
#subjects=["CD","MI","OS","MCWC","DMBI","OOPJ"]
workload_sub={}
subject_faculty={}
#subject_faculty={"CD":["B","V"],"MI":["B","V"],"OS":["B","C"],"MCWC":["H","C"],"DMBI":["A"],"OOPJ":["A","S"]}
#workload={"CD":5,"MI":5,"OS":3,"MCWC":3,"DMBI":3,"OPPJ":5}
days=["Monday","Tuesday","Wednesday","Thrusday","Friday"]
workload_faculty={}
timetable={}
print("Enter the number of faculties you want")
no_faculty=raw_input()
for x in range(int(no_faculty)):
	print("Enter the faculty name:")
	faculty=raw_input()
	print("Enter the workload for "+faculty)
	faculty_load=raw_input()
	workload_faculty[faculty]=faculty_load
for sub in subjects:
	faculty_list=[]
	print("Enter the no faculties available for:"+sub)
	no=raw_input()
	for i in range(int(no)):
		print("Enter the faculty name:")
		faculty=raw_input()
		faculty_list.append(faculty)
	subject_faculty[sub]=faculty_list
for sub in subjects:
	print("Enter the subject load for "+sub+":")
	load=raw_input()
	workload_sub[sub]=load
	#sub=random.choice(subjects)
for d in days:
	sub_test={}
	fac_test={}
	flag=1
	for time_slot in range(4):
		while flag==1:
			sub=random.choice(subjects)
			sub_count=0
			for x in range(len(sub_test)):
				if sub in sub_test:
					sub_count+=1
			if sub_count<2:
				load=int(workload_sub[sub])
				load=load-1
				sub_test[sub]=time_slot
				flag=0
		flag=1
	timetable[d]=sub_test

for d in days:
	sub_dic=timetable[d]
	print(d)
	for l in sub_dic:
		print(l+":"+str(sub_dic[l]))
	print("\n")