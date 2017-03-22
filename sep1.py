ins=[['add', '$r1', '$r2', '$r3'], ['add', '$r4', '$r1', '$r2'], ['lw', '$r5', '8($r4)'], ['add', '$r7', '$r6', '$r5'], ['add', '$r8', '$r7', '$r5'], ['lw', '$r9', '16($r4)'], ['add', '$r10', '$r6', '$r9'], ['add', '$r11', '$r10', '$r9']]
time=[]
t=5
for i in ins:
	if i[0]=='add' or i[0]=='mul' or i[0]=='sub' or i[0]=='addi' or i[0]=='move' or i[0]=='li':
		time.append(t)
		t+=1
	if i[0]=='lw' or i[0]=='sw':
		time.append(t)
		t+=2
print "intime",time
s=[[0], [1], [2, 5], [3, 6], [4, 7]]
t1=[]
for i in range(0,len(ins)):
	t1.append(0)
for i in s:
	if len(i)<=1:
		t1[i[0]]=time[i[0]]
	else:
		l=[]
		for k in i:
			l.append(time[k])
		v=min(l)
		for k in i:
			t1[k]=v
print t1
		
CPIinorder=float(max(time)-min(time)+1)/len(ins)
CPIOorder=float(max(t1)-min(t1)+1)/len(ins)

print CPIinorder,"IN"
print CPIOorder,"OUT"
