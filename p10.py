# wapp to read two integers
# and find ans = n1 / n2

print("welcome")
try:
	n1 = int(input(" enter first integer "))
	n2 = int(input(" enter second integer "))
	if n2 == 0:
		raise Exception("2nd num should not be zero ")
	ans = n1 / n2
except Exception as e:
	print(" invalid input ", e)
else:
	print("ans = ", ans)
	
print("bye")

# try with single except
# raise for explicitely throwing an exception