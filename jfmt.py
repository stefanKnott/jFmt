import sys, re, fileinput

if __name__ == "__main__":
	filename = sys.argv[1]
	print filename

	#read file into memory
	jFile = open(filename, "r+")

	jfilem = []
	for line in jFile:
		jfilem.append(line)

	indents = 0

	#stdout redirected to file
	for line in fileinput.input(filename, inplace=True):
		leading_spc = len(line) - len(line.lstrip())
	
		#found close of scope
		if re.search("\s*\S*\}", line):
			indents -= 1

		if leading_spc != indents * 5:
			print indents * 4 * " " + line.strip()
		else:
			print line.strip()

		#found opening of scope
		if re.search("\{\s*\S*\n", line):
			indents += 1
