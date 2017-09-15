print("Enter the no of subjects you want to enter:")
n=raw_input()
subjects=[]
sub_fac={}
for x in range(int(n)):
	print("Enter the subject:"+str((x+1)))	
	sub=raw_input()
	subjects.append(sub)
print("Enter the faculties:")
for sub in subjects:
	print("Entert the number of faculties for Subject:"+sub)
	n1=raw_input()
	fac=[]
	for x in range(int(n1)):
		print("Enter the faculty name")
		f=raw_input()
		fac.append(f)
	sub_fac[sub]=fac

##Faculty Printing######
# for sub in subjects:
# 	fac_list=sub_fac[sub]
# 	print("Faculties for subject:"+sub)
# 	for f in fac_list:
# 		print(f)
#######################
# for sub in subjects:
# 	print(sub)