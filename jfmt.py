import sys, re, fileinput

if __name__ == "__main__":
	filename = sys.argv[1]
	indents = 0
	comment = False #flag for indicating within a comment

	#stdout redirected to file
	for line in fileinput.input(filename, inplace=True):
		leading_spc = len(line) - len(line.lstrip())
	
		#check for comments...
		if re.search("/\*", line):
			comment = True

		if re.search("\*/", line):
			comment = False
			print indents * 4 * " " + line.strip()
			continue

		if comment:
			print indents * 4 * " " + line.strip()
			continue

		#found close of scope
		if re.search("\s*\S*\}", line):
			indents -= 1

		print indents * 4 * " " + line.strip()

		#found opening of scope
		if re.search("\{\s*\S*\n", line):
			indents += 1
