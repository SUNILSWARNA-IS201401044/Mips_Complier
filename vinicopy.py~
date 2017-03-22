f=open('out.asm','w')
f1=open('small-capital.asm','r+')
l=[]
str1=''
str2=''
str3=''
for i in f1:
	str1=i.split()
	l.append(str1)
g=[]
for i in l:
	if len(i)<=3 and len(i)!=0:
		
		str4=i[0]
                if str4!="syscall" and str4[len(str4)-1]!=':' and str4!='j' and str4!="la" :
			if str4[0]!='#' and str4[0]!='.':
				print str4[0]
				str2=i[0]+' '
				k=len(i)
				y11=0
                		for j in range(1,k):
                		        y=len(i[j])
                		        str3=i[j]
				        if i[j]=='#' or str3[0]=='#':
						break	
					if len(str3)>=2:
                                                if str3[1]=='#':
							y11=1
							print str,"2"
                                               		for z in range(0,1):
                                                        	str2=str2+str3[z]
                                        if len(str3)>=3:
							
                                                if str3[2]=='#':
							y11=1
							print str3,"3"
                                                        for z in range(0,2):
                                                        	str2=str2+str3[z]
                                        if len(str3)>=4:
							
                                                if str3[3]=='#':
							y11=1
							print str3,"4"
                                                        for z in range(0,3):
                                                        	str2=str2+str3[z]
                                        if len(str3)>=5:
                                                if str3[4]=='#':
							y11=1
							print str3,"4"
                                                        for z in range(0,3):
                                                        	str2=str2+str3[z]

	
	
	                	        if len(i[j])>=3 and str3[y-1]!=',' and y11!=1:
	                	                str2=str2+i[j]
	                		        if(j<k-1 and i[j+1]==','):
	                	                	str2=str2+i[j+1]
	                	        if len(i[j])>=3 and str3[y-1]==',' and y11!=1:
	                			str2=str2+i[j]
					if len(i[j])<=2 and str3[y-1]!=',' and y11!=1:
	                                               	str2=str2+i[j]
	                                               	if(j<k-1 and i[j+1]==','):
	                                                	str2=str2+i[j+1]
	                                if len(i[j])<=2 and str3[y-1]==',' and y11!=1:
	                                              	 str2=str2+i[j]

				f.write(str2)
               	                f.write("\n")
                                g.append(str2)
		
		

	if len(i)>3:
		
		str4=i[0]
		if str4!="syscall" and str4[len(str4)-1]!=':' and str4!='j' :
			if str4[0]!='#' and str4[0]!='.':
				print str4[0]
				str2=i[0]+' '
				k=len(i)
				y22=0
				for j in range(1,k):
					y=len(i[j])
					str3=i[j]
					if i[j]=='#' or str3[0]=='#':   
                                        	break
					if len(str3)>=2:
						if str3[1]=='#':
							y22=1
							print str3,"11"
							for z in range(0,1):
								str2=str2+str3[z]
					if len(str3)>=3:
						if str3[2]=='#':
							y22=1
							print str3,"33"
							for z in range(0,2):
								str2=str2+str3[z]
					if len(str3)>=4:
						if str3[3]=='#':
							y22=1
							print str3,"44"
							for z in range(0,3):
								str2=str2+str3[z]
					if len(str3)>=5:
                                                if str3[4]=='#':
							y22=1
							print str3,"55"
                                                        for z in range(0,3):
                                                               str2=str2+str3[z]

					if len(i[j])>=3 and str3[y-1]!=',' and y22!=1:
						
						str2=str2+i[j]
						if(j<k-1 and i[j+1]==','):
							str2=str2+i[j+1]
					if len(i[j])>=3 and str3[y-1]==',' and y22!=1:
						str2=str2+i[j]
					if len(i[j])<=2 and str3[y-1]!=',' and y22!=1:
                                                str2=str2+i[j]
                                                if(j<k-1 and i[j+1]==','):
                                                        str2=str2+i[j+1]
                                        if len(i[j])<=2 and str3[y-1]==',' and y22!=1:
                                                str2=str2+i[j]

				f.write(str2)
				f.write("\n")
				g.append(str2)
		
			
		
print g
		
	
