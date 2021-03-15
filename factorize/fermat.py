import gmpy2
c = 17830167351685057470426148820703481112309475954806278304600862043185650439097181747043204885329525211579732614665322698426329449125482709124139851522121862053345527979419420678255168453521857375994190985370640433256068675028575470040533677286141917358212661540266638008376296359267047685745805295747215450691069703625474047825597597912415099008745060616375313170031232301933185011013735135370715444443319033139774851324477224585336813629117088332254309481591751292335835747491446904471032096338134760865724230819823010046719914443703839473237372520085899409816981311851296947867647723573368447922606495085341947385255
n = 23135514747783882716888676812295359006102435689848260501709475114767217528965364658403027664227615593085036290166289063788272776788638764660757735264077730982726873368488789034079040049824603517615442321955626164064763328102556475952363475005967968681746619179641519183612638784244197749344305359692751832455587854243160406582696594311842565272623730709252650625846680194953309748453515876633303858147298846454105907265186127420148343526253775550105897136275826705375222242565865228645214598819541187583028360400160631947584202826991980657718853446368090891391744347723951620641492388205471242788631833531394634945663
e = 0x10001

def fermat(n):
	if(n<=0):
		return n
	if(n%2==0):
		return (n/2,2)
	
	x = gmpy2.isqrt(n)+1
	
	if(x*x==n):
		return (x,x)
	
	while(True):
		y_ = x* x -n
		if(y_>0):
			y = int(gmpy2.isqrt(y_))
			if(y*y==y_):
				return(x-y,x+y)
			else:
				x+=1
		else:
			print(y_)

p,q = fermat(n)
PHI=(p-1)*(q-1)
d= gmpy2.invert(e,PHI)
plain=pow(c,d,n)
print ("\nPlain=",hex(plain))
