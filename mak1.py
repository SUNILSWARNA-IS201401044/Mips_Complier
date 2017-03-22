import sys
f=open('out.asm','w+')
f1=open(sys.argv[1],'r+')
l=[]
str1=''
str2=''
str3=''
for i in f1:
	str1=i.split()
	l.append(str1)
g=[]
for i in l:
	if len(i)<=3:
		str4=i[0]
                if str4!="syscall":
			if str4[0]!='#' and str4[0]!='.':
				print str4[0]
				str2=i[0]+' '
				k=len(i)
                		for j in range(1,k):
                		        y=len(i[j])
                		        str3=i[j]
                		        if len(i[j])>=3 and str3[y-1]!=',':
                		                str2=str2+i[j]
                		                if(j<k-1 and i[j+1]==','):
                		                        str2=str2+i[j+1]
                		        if len(i[j])>=3 and str3[y-1]==',':
                				str2=str2+i[j]
				f.write(str2)
                                f.write("\n")
                                g.append(str2)


	if len(i)>3:
		
		str4=i[0]
		if str4!="syscall":
			if str4[0]!='#' and str4[0]!='.':
				print str4[0]
				str2=i[0]+' '
				k=len(i)
				for j in range(1,k):
					y=len(i[j])
					str3=i[j]
					if len(i[j])>=3 and str3[y-1]!=',':
						str2=str2+i[j]
						if(j<k-1 and i[j+1]==','):
							str2=str2+i[j+1]
					if len(i[j])>=3 and str3[y-1]==',':
						str2=str2+i[j]
				f.write(str2)
				f.write("\n")
				g.append(str2)

f.close()
f1.close()	
f=open('out.asm','r+')	
k=0
list1=[]
dict1={}
dict1.setdefault("RAW",[])
dict1.setdefault("WAW",[])
dict1.setdefault("WAR",[])
for i in f:
	list1.append(i.split('\n'))
	k+=1
p=''
s=[]
lis1=[]
for i in range(0,k):
	for j in list1[i]:
		s.append(j.split('\n'))	
for h in range(0,len(s)-1):
	try:
		lis1.append(s[2*h])	
	except:
		pass	
l=[]
lis2=[]
g=[]
for i in range(0,len(lis1)):
	if ['syscall'] in lis1:
		lis1.remove(['syscall'])
	elif ['.text'] in lis1:
		lis1.remove(['.text'])
	elif ['main:'] in lis1:
		lis1.remove(['main:'])
	elif ['.data'] in lis1:
		lis1.remove(['.data'])
	elif ['.globl main'] in lis1:
		lis1.remove(['.globl main'])	
f=[]
d=[]
c=''
lis3=[]
for l in lis1:
	for g in l:
		f=g.split(' ' or ',')
		c=','.join(f)
		lis3.append(c.split(','))
print lis3
flag=[[] for i in range(len(lis3))]
flag1=[[] for i in range(len(lis3))]

def chardel(k):
	s=''
	if k.endswith(')'):
		s=s+k[len(k)-4]+k[len(k)-3]+k[len(k)-2]
	else:
		s=k
	return s

def adddep(add1,add2,add3,k):
	j=0
	for i in lis3[k:]:
		r=lis3.index(i)
		sum1=0
		if i[0]=='add' or i[0]=='mul' or i[0]=='sub' or i[0]=='addi' or i[0]=='div':
			
			if add1==chardel(i[1]) :
				print lis3[k-1],"had a WAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAW"] :
					dict1["WAW"].append(lis3[k-1])
				if i not in dict1["WAW"]:					
					dict1["WAW"].append(i)
			if add2==chardel(i[1]) :
				print lis3[k-1],"had a WAR dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAR"]:
					dict1["WAR"].append(lis3[k-1])
				if i not in dict1["WAR"]:					
					dict1["WAR"].append(i)
			if add3==chardel(i[1]) :
				print lis3[k-1],"had a WAR dependency with",i
				flag1[r].append(lis3[k-1])
				flag[r].append(k-1)
				if lis3[k-1] not in dict1["WAR"]:
					dict1["WAR"].append(lis3[k-1])
				if i not in dict1["WAR"]:					
					dict1["WAR"].append(i)
			if add1==chardel(i[2]) :
				print lis3[k-1],"had a RAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["RAW"]:
					dict1["RAW"].append(lis3[k-1])
				if i not in dict1["RAW"]:					
					dict1["RAW"].append(i)
			if  add1==chardel(i[3]):	
				print lis3[k-1],"had a RAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["RAW"]:
					dict1["RAW"].append(lis3[k-1])
				if i not in dict1["RAW"]:					
					dict1["RAW"].append(i)
		if i[0]=='lw' or i[0]=='li' or i[0]=='lb':
			if add1==chardel(i[1]):
				print lis3[k-1],"has WAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAW"]:
					dict1["WAW"].append(lis3[k-1])
				if i not in dict1["WAW"]:					
					dict1["WAW"].append(i)
			if add1==chardel(i[2]):
				print lis3[k-1],"has RAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["RAW"]:
					dict1["RAW"].append(lis3[k-1])
				if i not in dict1["RAW"]:					
					dict1["RAW"].append(i)
			if add2==chardel(i[1]):
				print lis3[k-1],"has WAR dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAR"]:
					dict1["WAR"].append(lis3[k-1])
				if i not in dict1["WAR"]:					
					dict1["WAR"].append(i)
			if add3==chardel(i[1]):
				print lis3[k-1],"has WAR dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAR"]:
					dict1["WAR"].append(lis3[k-1])
				if i not in dict1["WAR"]:					
					dict1["WAR"].append(i)
		if  i[0]=='sw' or i[0]=='sb':
			if add1==chardel(i[2]):
				print lis3[k-1],"has WAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAW"]:
					dict1["WAW"].append(lis3[k-1])
				if i not in dict1["WAW"]:					
					dict1["WAW"].append(i)
			if add2==char(i[2]):
				print lis3[k-1],"has RAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["RAW"]:
					dict1["RAW"].append(lis3[k-1])
				if i not in dict1["RAW"]:					
					dict1["RAW"].append(i)
			if add3==chardel(i[2]):
				print lis3[k-1],"has RAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["RAW"]:
					dict1["RAW"].append(lis3[k-1])
				if i not in dict1["RAW"]:					
					dict1["RAW"].append(i)
			if add1==chardel(i[1]):
				print lis3[k-1],"has WAR dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAR"]:
					dict1["WAR"].append(lis3[k-1])
				if i not in dict1["WAR"]:
					dict1["WAR"].append(i)
		
def lwdeep(lw1,lw2,k):
	for i in lis3[k:]:
		r=lis3.index(i)
		if i[0]=='add' or i[0]=='mul' or i[0]=='sub' or i[0]=='addi' or i[0]=='div':
			if lw1==chardel(i[1]):
				print lis3[k-1],"has WAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAW"]:
					dict1["WAW"].append(lis3[k-1])
				if i not in dict1["WAW"]:					
					dict1["WAW"].append(i)
			if lw1==chardel(i[2]):
				print lis3[k-1],"has RAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["RAW"]:
					dict1["RAW"].append(lis3[k-1])
				if i not in dict1["RAW"]:					
					dict1["RAW"].append(i)
			if lw1==chardel(i[3]):
				print lis3[k-1],"has RAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["RAW"]:
					dict1["RAW"].append(lis3[k-1])
				if i not in dict1["RAW"]:					
					dict1["RAW"].append(i)
			if lw2==chardel(i[1]):
				print lis3[k-1],"has WAR dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAR"]:
					dict1["WAR"].append(lis3[k-1])
				if i not in dict1["WAR"]:					
					dict1["WAR"].append(i)
		if i[0]=='lw' or i[0]=='li' or i[0]=='lb':
			if lw1==chardel(i[1]):
				print lis3[k-1],"has WAW dependency with",i
				flag1[r].append(lis3[k-1])
				flag[r].append(k-1)
				if lis3[k-1] not in dict1["WAW"]:
					dict1["WAW"].append(lis3[k-1])
				if i not in dict1["WAW"]:					
					dict1["WAW"].append(i)
			if lw1==chardel(i[2]):
				print lis3[k-1],"has RAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["RAW"]:
					dict1["RAW"].append(lis3[k-1])
				if i not in dict1["RAW"]:					
					dict1["RAW"].append(i)
			if lw2==chardel(i[1]):
				print lis3[k-1],"has WAR dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAR"]:
					dict1["WAR"].append(lis3[k-1])
				if i not in dict1["WAR"]:					
					dict1["WAR"].append(i)
		if  i[0]=='sw' or i[0]=='sb':
			if lw1==chardel(i[2]):
				print lis3[k-1],"has WAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAW"]:
					dict1["WAW"].append(lis3[k-1])
				if i not in dict1["WAW"]:					
					dict1["WAW"].append(i)
			if lw1==chardel(i[1]):
				print lis3[k-1],"has RAW dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["RAW"]:
					dict1["RAW"].append(lis3[k-1])
				if i not in dict1["RAW"]:					
					dict1["RAW"].append(i)
			if lw2==chardel(i[2]):
				print lis3[k-1],"has WAR dependency with",i
				flag[r].append(k-1)
				flag1[r].append(lis3[k-1])
				if lis3[k-1] not in dict1["WAR"]:
					dict1["WAR"].append(lis3[k-1])
				if i not in dict1["WAR"]:
					dict1["WAR"].append(i)			
for i in range(len(lis3)):
	for j in range(len(lis3[i])):
		try:
			if lis3[i][j]=='lw' or lis3[i][j]=='move' or lis3[i][j]=='lb':
				lw1=lis3[i][j+1]
				lw2=lis3[i][j+2]
				k1=chardel(lw1)
				k2=chardel(lw2)
				fun2=lwdeep(k1,k2,i+1)
			if lis3[i][j]=='li':
				if lis3[i][j+1]=='$v0':
					continue
				else:
					lw1=chardel(lis3[i][j+1])
					lw2='#'
					fun2=lwdeep(lw1,lw2,i+1)
			elif lis3[i][j]=='sw' or lis3[i][j]=='sb':
				lw1=lis3[i][j+1]
				lw2=lis3[i][j+2]
				k1=chardel(lw1)
				k2=chardel(lw2)
				fun2=lwdeep(k2,k1,i+1)	
			elif lis3[i][j]=='add' or lis3[i][j]=='mul' or lis3[i][j]=='div' or lis3[i][j]=='sub' or lis3[i][j]=='addi':
				add1=lis3[i][j+1]
				add2=lis3[i][j+2]
				add3=lis3[i][j+3]
				k1=chardel(add1)
				k2=chardel(add2)
				k3=chardel(add3)
				fun1=adddep(k1,k2,k3,i+1)
		except:
			pass
#print dict1
#print lis3
print flag ,"Instruction Dependcies"  # Out of order excution sequence
#print flag1 #for out of order instructions list
flagult=[]
l1=[]
l1=list(flag)
l3=[]
for i in range(0,len(l1)):
        try:
                flagult.append(0)
        except:
                pass
def process(l1,flagult):
        k=[]
        for i in range(len(l1)):
                if l1[i]==[] and flagult[i]==0:
                        k.append(i)

        return k
for fun in l1:
                s1=process(l1,flagult)
      #          print s1,"Each Iteration OOO"
                l3.append(s1)
         #       print flagult,"Flagg"
                for s in s1:
                        position=s
                        flagult[position]=1
                        l1[position].append(-1)
        #                print l1
                        for k in l1:
                                p1=l1.index(k)
                                for j in range(len(k)):
                                        try:
                                                if k[j]==position and flagult[p1]==0:
                                                        if k.count(position)==1:
                                                                k.remove(k[j])
                                                        else:
                                                                for t in range(k.count(position)):
                                                                        k.remove(position)
                                        except:
                                                pass
#print flagult
#print l3 # Out of Order Sequence
time=[]
time1=5
ins=list(lis3)
print len(ins)
for i in range(0,len(ins)):
	if ins[i][0]=='addi' or ins[i][0]=='add' or ins[i][0]=='mul' or ins[i][0]=='sub' or ins[i][0]=='div':
		try:
			ins[i][1]=chardel(ins[i][1])			
			ins[i][2]=chardel(ins[i][2])
			ins[i][3]=chardel(ins[i][3])
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				ins[i+1][3]=chardel(ins[i+1][3])
				if ins[i][1]== ins[i+1][2] or ins[i+1][3]==ins[i][1] or ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][2] or ins[i+1][1]==ins[i][3]:
					time.append(time1)
					time1+=1
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][0]=='lw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][3] or ins[i+1][1]==ins[i][2]:
					time.append(time1)
					time1+=1
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][0]=='move' or ins[i+1][0]=='li':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][3] or ins[i+1][1]==ins[i][2]:
					time.append(time1)
					time1+=1
				else:
					time.append(time1)
					time1=time1
	        	elif ins[i+1][0]=='sw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins [i][1]==ins[i+1][2] or ins[i+1][2]==ins[i][2] or ins[i+1][2]==ins[i][3]:
					time.append(time1)
					time1+=1
				else:
					time.append(time1)
					time1=time1
			else:
				time.append(time1)
				time1=time1
		except:
			pass
	if ins[i][0]=='lw':
		try:
			ins[i][1]=chardel(ins[i][1])			
			ins[i][2]=chardel(ins[i][2])
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				ins[i+1][3]=chardel(ins[i+1][3])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][3] or ins[i][2]==ins[i+1][1]:
					time.append(time1)
					time1+=2
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][1]=='lw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time.append(time1)
					time1+=2
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][1]=='move' or ins[i+1]=='li':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time.append(time1)
					time1+=2
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][1]=='sw' :
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][2]:
					time.append(time1)
					time1+=2
				else:
					time.append(time1)
					time1=time1
			else:
				time.append(time1)
				time1=time1
		except:
			pass
	if ins[i][0]=='li' or ins[i][0]=='move':
		try:
			ins[i][1]=chardel(ins[i][1])			
			ins[i][2]=chardel(ins[i][2])
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				ins[i+1][3]=chardel(ins[i+1][3])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][3] or ins[i][2]==ins[i+1][1]:
					time.append(time1)
					time1+=1
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][1]=='lw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time.append(time1)
					time1+=1
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][1]=='move' or ins[i+1]=='li':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time.append(time1)
					time1+=1
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][1]=='sw' :
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][2]:
					time.append(time1)
					time1+=1
				else:
					time.append(time1)
					time1=time1
			else:
				time.append(time1)
				time1=time1
		except:
			pass
	if ins[i][0]=='sw':
		try:	
			ins[i][1]=chardel(ins[i][1])			
			ins[i][2]=chardel(ins[i][2])
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				ins[i+1][3]=chardel(ins[i+1][3])
				if ins[i][2]==ins[i+1][1] or ins[i][2]==ins[i+1][2] or ins[i][2]==ins[i+1][3] or ins[i][1]==ins[i+1][1] :
					time.append(time1)
					time1+=2
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][0]=='sw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1] or ins[i][2]==ins[i+1][2]:
					time.append(time1)
					time1+=2
				else:
					time.append(time1)
					time1=time1
			elif ins[i+1][0]=='lw' or ins[i+1][0]=='move' or ins[i+1][0]=='li':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][2] or ins[i][2]==ins[i+1][2]:
					time.append(time1)
					time+=2
				else:
					time.append(time1)
					time1=time1
			else:
				time.append(time1)
				time1=time1
		except:
			pass

print ins
time.append(time1)
print time,"TimeATr"
s=list(l3)

for i in s:
	if i==[]:
		s.remove(i)
if s[len(s)-1]==[]:
	s.remove([])
print s,"Out Of Order Sequence" # Out of Order Sequence
t1=[] # Out Of order Time

for i in range(0,len(ins)):
        t1.append(0)

for i in s:
	try:
		if i!=[]:
        		if len(i)<=1:
                		t1[i[0]]=time[i[0]]
        		else:
                		q=[]
               			for k in i:
                        		q.append(time[k])
                		v=min(q)
                		for k in i:
                        		t1[k]=v
	except:
		pass

CPIinorder=float(max(time)-min(time)+1)/len(ins)
CPIOorder=float(max(t1)-min(t1)+1)/len(ins)
print CPIinorder,"IN"
print CPIOorder,"OUT"
print s
#####----------GUI----------######

from Tkinter import *
import random
import sys
root=[]
root=random.sample(xrange(1000),100)
root[0]=Tk()
root[0].title('Assembler')
root[0].geometry('300x300')
top=Frame(root[0])
top.pack()
#def createTextBox(parent):
#	tBox = Entry(parent)
#	tBox.pack()
#createTextBox(root)
#root1=Tk()
#root2=Tk()
#root3=Tk()
#root4=Tk()
#root5=Tk()

#RAW Dep
def PrintD():
	root[1]=Tk()
	top1=Frame(root[1])
	top1.pack()
	text=Text(top1)
	text.insert(INSERT,"RAW dependencies\n")
	if dict1["RAW"]==[]:
		text.insert(END,"NONE")
		text.pack()
	else:
		for i in dict1["RAW"]:
			text.insert(INSERT,' '.join(i)+'\n')
		text.insert(END,"End of RAW dependencies")
		text.pack()
but1=Button(top,text="RAW Dependencies",command=PrintD)
but1.pack()

#WAR Dep
def PrintD2():
#	global root[2]
	root[2]=Tk()
	top2=Frame(root[2])
	top2.pack()
	text=Text(top2)
	text.insert(INSERT,"WAR dependencies\n")
	if dict1["WAR"]==[]:
		text.insert(END,"NONE")
		text.pack()
	else:
		for i in dict1["WAR"]:
			text.insert(INSERT,' '.join(i)+'\n')
		text.insert(END,"End of WAR dependencies")
		text.pack()
but2=Button(top,text="WAR Dependencies",command=PrintD2)
but2.pack()

#WAW Dep
def PrintD3():
#	global root[3]
	root[3]=Tk()
	top3=Frame(root[3])
	top3.pack()
	text=Text(top3)
	text.insert(INSERT,"WAW dependencies\n")
	if dict1["WAW"]==[]:
		text.insert(END,"NONE")
		text.pack()
	else:
		for i in dict1["WAW"]:
			text.insert(INSERT,' '.join(i)+'\n')
		text.insert(END,"End of WAW dependencies")
		text.pack()
but3=Button(top,text="WAW Dependencies",command=PrintD3)
but3.pack()

#Inorder seq
def Pinin():
#	global root[4]
	root[4]=Tk()
	top4=Frame(root[4])
	top4.pack()
	text=Text(top4)
	text.insert(INSERT,"Instruction"+'          '+"Time Taken"+'\n')	
	for i in range(len(lis3)):
		text.insert(INSERT,' '.join(lis3[i])+'     '+str(time[i])+'\n')
	text.insert(INSERT,'\n')
	text.insert(INSERT,"CPI of inorder seq\n")
	text.insert(END,CPIinorder)
	text.pack()
but4=Button(top,text="Inorder",command=Pinin)
but4.pack()

#Outorder seq
def PinO():
#	global root[5]
	root[5]=Tk()
	top5=Frame(root[5])
	top5.pack()
	text=Text(top5)
	text.insert(INSERT,"Instruction"+'          '+"Time Taken"+'\n')	
	for i in s:
		for j in i:
			text.insert(INSERT,' '.join(lis3[j])+'     '+str(t1[j])+'\n' )
	text.insert(INSERT,'\n')
	text.insert(INSERT,"CPI of Out of order seq\n")
	text.insert(END,CPIOorder)
	text.pack()
but5=Button(top,text="Out Of Order",command=PinO)
but5.pack()

for i in range(0,6):
	root[i].mainloop()
#root.mainloop()
#root1.mainloop()
#root2.mainloop()
#root3.mainloop()
#root4.mainloop()
#root5.mainloop()
