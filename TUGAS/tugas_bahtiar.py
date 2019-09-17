#Determine Triangle
a = int(input ("a: "))
b = int(input ("b: "))
c = int(input ("c: "))

if (a <= 0 or b <= 0 or c <= 0):
	print ("tidak dapat dibangun")

elif (a >= b+c or b >= a+c or c >= a+b):
	print ("tidak dapat dibangun")

elif (a==b and b==c):
	print ("segitiga sama sisi")

elif (a==b or b==c or a==c):
	print ("segitiga sama kaki")

elif (a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
    print ("segitiga siku-siku")

else:
	print ("segitiga BEBASSS")
