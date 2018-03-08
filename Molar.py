Molar = dict()

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False


Molar["N"] = 14
Molar["O"] = 16

def MM(stof):
	M = 0
	print(stof)
	if(stof[-1] is not "1" ):
		stof = stof+"1"
	for i in range(len(stof[:-1])):
		print(i)
		print("Wup")
		if(stof[i] == stof[i].upper()):
			print("forste led")
			if(stof[i+1] == stof[i+1].upper()):
				if(is_number(stof[i+1]) == True):
					M += int(stof[i+1])*Molar[stof[i]]
					print("Her")
				else:
					M += Molar[stof[i]]
	return M
molekyle = input()
res = MM(molekyle)
print(molekyle,"har en molar masse på ",res,"g/mol")
			
