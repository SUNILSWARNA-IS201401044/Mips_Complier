ins=[['li', '$v0', '4'], ['li', '$t0', '1'], ['addi', '$t0', '$t0', '2'], ['addi', '$t1', '$t0', '1'], ['sub', '$t2', '$t1', '$t0'], ['li', '$v0', '1'], ['move', '$a0', '$t2'], ['add', '$t1', '$t3', '$t4'], ['add', '$t5', '$t6', '$t7'], ['add', '$t8', '$t5', '$t7'], ['li', '$v0', '10']]
l1=[[], [], [1, 1], [1, 2], [1, 2, 3], [], [], [3, 4], [], [8], []]
dic1={}
for i in range(len(ins)):
	dic1[i]=ins[i]
print dic1
l3=[]
flag=[]
time=len(ins)
print time,'****'
for i in range(0,len(l1)):
	try:
		flag.append(0)
	except:
		pass
def process(l1,flag):
	k=[]
	for i in range(len(l1)):
		if l1[i]==[] and flag[i]==0:
			k.append(i)
			
	return k
for fun in l1:
		s1=process(l1,flag)
		print s1,"Each Iteration OOO"
		l3.append(s1)
		print flag,"Flagg"
		for s in s1:
			position=s
			flag[position]=1
			
			
			l1[position].append(-1)
		
			print l1
			for k in l1:
				p1=l1.index(k)
				for j in range(len(k)):
					try:
						if k[j]==position and flag[p1]==0:
							if k.count(position)==1:
								k.remove(k[j])
							else:
								for t in range(k.count(position)):
									k.remove(position)
					except:
						pass
			print l1,"list"
print flag
print l3
k=0
for i in l3:
	k+=1
	for j in i:
		print k,dic1[j]
