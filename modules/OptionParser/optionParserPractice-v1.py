from optparse import OptionParser

#print(f'...')

def test():
	print(f'[store_true] hi?')

def main():
	usage = "usage: %prog [options] arg"
	parser = OptionParser(usage)
	parser.add_option("-f", "--file", dest="filename",
		      help="read data from FILENAME")
	parser.add_option("-s", "--store_true",
		      action="store_true", dest="store_true")
	parser.add_option("-a", "--append",
		      action="append", dest="append")
	parser.add_option("-v", "--verbose",
		      action="store_true", dest="verbose")
	parser.add_option("-q", "--quiet",
		      action="store_false", dest="verbose")
	#print(f'...')
	(options, args) = parser.parse_args()
	print(f'[parser-return] options:{options} args:{args}')
	if len(args) != 1:
		parser.error("incorrect number of arguments")
	if options.verbose:
		print("reading %s..." % options.filename)
	#print(f'...')

if __name__ == "__main__":
	main()
