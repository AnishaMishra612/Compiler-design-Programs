def left_recursion(grammer):
	flag = 0
	pos = 0
	for key in grammer.copy():
		item = grammer[key]
		for prod in item:
			if key == prod[0:1]:
				print("left recursion found")
				flag = 1
				pos = pos +1
				subfix = prod[1:len(prod)]
		if flag == 1:
			grammer[key] = item[pos:len(item)][0]+key+"'"
			grammer.update({key+"'":["",subfix+key+"'"]})
			flag=pos=0
	return grammer
grammer = {}
le = int(input("length"))
for i in range(le):
	key = input("key")
	l = int(input("number of production"))
	lis = list()
	for i in range(0,l):
		lis.append(input())
	grammer.update({key:lis})
print(grammer)
print(left_recursion(grammer))
