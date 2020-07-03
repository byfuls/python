from optparse import OptionParser

def main():
	usage =	'''usage: %prog [options] arg
	-l, --list : shwo process list
	-u, --up [serial no.] : launch process
	-d, --down [serial no.] : kill process
	-w, --watch [serial no.] : watch gateway(=serial) '''	
	parser = OptionParser(usage)
	parser.add_option("-l", "--list", dest="list", action="store_true")
	parser.add_option("-u", "--up", dest="up", action="store_true")
	parser.add_option("-d", "--down", dest="down", action="store_true")
	parser.add_option("-w", "--watch", dest="watch", action="store_true")

	(options, args) = parser.parse_args()
	print(f'[parser-return] options:{options} args:{args}')
	print(f'[parser-return] options type:{type(options)}')

	if not (options.list or options.up or options.down or options.watch):
		parser.error('incorrect number of arguments')
		exit(0)

	if options.list:
		print(f'[options-sorting] list true')
	if options.up:
		if not len(args):
			parser.error('incorrect number of arguments')
			exit(0)
		t = args.pop(0)

		print(f'[options-sorting] up true')
	if options.down:
		t = args.pop(0)

		print(f'[options-sorting] down true')
	if options.watch:
		t = args.pop(0)

		print(f'[options-sorting] watch true')


if __name__ == "__main__":
	main()
