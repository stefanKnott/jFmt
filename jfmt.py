import sys, re, fileinput

if __name__ == "__main__":
	filename = sys.argv[1]
	indents = 0
	multiline = False 

	#stdout redirected to file
	for line in fileinput.input(filename, inplace=True):
		#check for comments...
		if re.search("/\*", line):
			multiline = True

		if re.search("\*/", line):
			multiline = False
			print indents * 4 * " " + line.strip()
			continue

		if multiline or re.search("//\s*\S*\{", line):
			print indents * 4 * " " + line.strip()
			continue

		#found close of scope
		if re.search("\s*\S*\}", line):
			indents -= 1

		print indents * 4 * " " + line.strip()

		#found opening of scope
		if re.search("\{\s*\S*\n", line):
			indents += 1
