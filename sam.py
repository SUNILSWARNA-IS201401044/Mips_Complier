f=open('p3.asm','r+')
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
#print l3 # Out of Ordee Sequence
time=[] # Inorder Time
t=5
ins=list(lis3)
for i in ins:
        if i[0]=='add' or i[0]=='mul' or i[0]=='sub' or i[0]=='addi' or i[0]=='move' or i[0]=='li':
                time.append(t)
                t+=1
        if i[0]=='lw' or i[0]=='sw':
                time.append(t)
                t+=2

s=list(l3)
for i in s:
	if i==[]:
		s.remove(i)
if s[len(s)-1]==[]:
	s.remove([])
print s,"Out Of Order Sequence" # Out of Ordee Sequence
t1=[] # Out Of order Time
for i in range(0,len(ins)):
        t1.append(0)

for i in s:
	if i!=[]:
        	if len(i)<=1:
                	t1[i[0]]=time[i[0]]
        	else:
                	l=[]
               		for k in i:
                        	l.append(time[k])
                	v=min(l)
                	for k in i:
                        	t1[k]=v
CPIinorder=float(max(time)-min(time)+1)/len(ins)
CPIOorder=float(max(t1)-min(t1)+1)/len(ins)
print CPIinorder,"IN"
print CPIOorder,"OUT"


for i in s:
	for j in i:
		print lis3[j]
