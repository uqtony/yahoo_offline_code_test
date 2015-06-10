
import sys;
from math import log

# show help
def show_help():
	print '[Usage] python fibonacci_binet.py [N]\tShow Nth value on Fibonacci sequence';

phi = (1 + 5**0.5) / 2;

def fibonacci_binet(number):
	return int(round((phi**number - (1-phi)**number) / 5**0.5));

if len(sys.argv) != 2:
	show_help();
	sys.exit();

try:
	num = int(sys.argv[1]);
	print '%dth number=%d'%(num, fibonacci_binet(num));
	
except ValueError:
	print 'Invalid parameter';
