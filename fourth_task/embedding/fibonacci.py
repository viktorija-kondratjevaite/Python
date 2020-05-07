def fibonacci (n):
	if n<1:
		print ("Please enter a number greater than zero.")
	else:
		a,b = 0,1
		for i in range(n):
			a,b = b,a+b
		return a