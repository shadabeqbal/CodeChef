#food = ['cookie','milk']
t=input()
for i in range(0,t):
	minutes=input()
	sz = minutes+1
	lst = ['None']*sz
	lst = raw_input()
	lst= lst.split(" ")
#for j in range(0,minutes):
	sz = len(lst)
	x=0
	while sz!=0:
		if(x>sz):
			break
		if(not "milk" in lst):
			flag=0
			break
		elif(lst[x-1] == "cookie" and lst[x] == "cookie"):
			flag=0
			break
		elif(lst[x-1] == "milk" and lst[x] == "milk"):
			flag=1
		elif(lst[len(lst)-1] == "cookie"):
			flag=0
			break
		else:
			flag=1
		x+=1
		sz=sz-1
	if (flag == 1):
		print "YES"
	else:
		print "NO"

			


