def fbnq(n):
	a,b=0,1
	while b<n:
		print(a,"  ")
#	print(a,end=' ')
		a,b=b,a+b
	print(a)
	print ("it's end!")


fbnq(1000)

