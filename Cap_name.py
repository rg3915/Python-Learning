names = input().split()

fullname = []

for name in names:
	name2 = len(name)
	if name2 > 3:
		name = name.capitalize()
	fullname.append(name)
	
final = " ".join(fullname)
print(final)