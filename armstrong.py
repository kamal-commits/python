num=int(input("ENTER THE NUMBER : "))
sum = 0
t=num
while t!=0:
	temp=t%10
	temp=temp**3
	t=t/10

if sum==num:
	print("ARMSTRONG")

else:
	print("NOT")		