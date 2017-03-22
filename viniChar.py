f=open('out.asm','w')
f1=open('p2.asm','r+')
#for i in f:
#	print i,
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
	
		
print g
		
	
