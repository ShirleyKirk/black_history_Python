if __name__:'__main__':
	import sys
	if len(sys.argv)==1:
		more(sys.stdin.read())
	else:
		more(open(sys.argv[1]).read())