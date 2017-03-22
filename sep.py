#ins=[['add', '$r1', '$r2', '$r3'], ['add', '$r4', '$r1', '$r2'], ['lw', '$r5', '$r4'], ['add', '$r7', '$r6', '$r5'], ['add', '$r8', '$r7', '$r5'], ['lw', '$r9', '$r4'], ['add', '$r10', '$r6', '$r9'], ['add', '$r11', '$r10', '$r9']]
#ins=[['lw', '$f2', '$r2'], ['lw', '$f4', '$r3'], ['mul', '$f6', '$f4', '$f2'], ['sub', '$f8', '$f2', '$f2'], ['div', '$f4', '$f2', '$f8'], ['add', '$f10', '$f6', '$f4']]
#ins=[['li', '$v0', '4'], ['li', '$t0', '1'], ['addi', '$t0', '$t0', '2'], ['addi', '$t1', '$t0', '1'], ['sub', '$t2', '$t1', '$t0'], ['li', '$v0', '1'], ['move', '$a0', '$t2'], ['add', '$t1', '$t3', '$t4'], ['add', '$t5', '$t6', '$t7'], ['add', '$t8', '$t5', '$t7'], ['li', '$v0', '10']]
ins=[['add', '$r1', '$r2', '$r3'], ['add', '$r4', '$r1', '$r2'], ['lw', '$r5', '$r4'], ['add', '$r7', '$r6', '$r5'], ['add', '$r8', '$r7', '$r5'], ['lw', '$r9', '$r4'], ['add', '$r10', '$r6', '$r9'], ['add', '$r11', '$r10', '$r9']]

time=[]
time1=5
print len(ins)
k=-1
for i in range(0,len(ins)):
	if ins[i][0]=='addi' or ins[i][0]=='add' or ins[i][0]=='mul' or ins[i][0]=='sub' or ins[i][0]=='div':
		print i,"add"
		try:
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				if ins[i][1]== ins[i+1][2] or ins[i+1][3]==ins[i][1] or ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][2] or ins[i+1][1]==ins[i][3]:
					time.append(time1)
					time1+=1
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			elif ins[i+1][0]=='lw':
				if ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][3] or ins[i+1][1]==ins[i][2]:
					time.append(time1)
					time1+=1
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			elif ins[i+1][0]=='move' or ins[i+1][0]=='li':
				if ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][3] or ins[i+1][1]==ins[i][2]:
					time.append(time1)
					time1+=1
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
	        	elif ins[i+1][0]=='sw':
				if ins[i][1]==ins[i+1][1] or ins [i][1]==ins[i+1][2] or ins[i+1][2]==ins[i][2] or ins[i+1][2]==ins[i][3]:
					time.append(time1)
					time1+=1
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			else:
				time.append(time1)
				time1=time1
				k=k+1
				print k,"Iter"
		except:
			pass
	if ins[i][0]=='lw':
		print i,"lw"
		try:
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][3] or ins[i][2]==ins[i+1][1]:
					time.append(time1)
					time1+=2
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			elif ins[i+1][1]=='lw':
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time.append(time1)
					time1+=2
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			elif ins[i+1][1]=='move' or ins[i+1]=='li':
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time.append(time1)
					time1+=2
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			elif ins[i+1][1]=='sw' :
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][2]:
					time.append(time1)
					time1+=2
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			else:
				time.append(time1)
				time1=time1
				k=k+1
				print k,"Iter"
		except:
			pass
	if ins[i][0]=='move' or ins[i][0]=='li':
		print i,"li"
		try:
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
                        	if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][3] or ins[i][2]==ins[i+1][1]:
                                	time.append(time1)
                               		time1+=1
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
                	elif ins[i+1][1]=='lw':
                        	if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
                                	time.append(time1)
                                	time1+=1
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
                	elif ins[i+1][1]=='move' or ins[i+1]=='li':
                        	if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
                                	time.append(time1)
                           		time1+=1
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
                
			elif ins[i+1][1]=='sw' :
                	        if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][2]:
                        	        time.append(time1)
                                	time1+=1
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			else:
				time.append(time1)
				time1=time1
				k=k+1
				print k,"Iter"
		except:
			pass
	if ins[i][0]=='sw':
		print i,"sw"
		try:
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				if ins[i][2]==ins[i+1][1] or ins[i][2]==ins[i+1][2] or ins[i][2]==ins[i+1][3] or ins[i][1]==ins[i+1][1] :
					time.append(time1)
					time1+=2
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			
			elif ins[i+1][0]=='sw':
				if ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1] or ins[i][2]==ins[i+1][2]:
					time.append(time1)
					time1+=2
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			elif ins[i+1][0]=='lw' or ins[i+1][0]=='move' or ins[i+1][0]=='li':
				if ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][2] or ins[i][2]==ins[i+1][2]:
					time.append(time1)
					time+=2
					k=k+1
					print k,"Iter"
				else:
					time.append(time1)
					time1=time1
					k=k+1
					print k,"Iter"
			else:
				time.append(time1)
				time1=time1
				k=k+1
				print k,"Iter"
		except:
			pass

time.append(time1)
print time
t1=[]
#s=[[0, 1], [2, 3], [4], [5]]
s=[[0], [1], [2, 5], [3, 6], [4, 7]]
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

