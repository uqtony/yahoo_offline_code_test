
import sys;

# show help
def show_help():
	print '[Usage] python fibonacci_recursive.py [N]\tShow Nth value on Fibonacci sequence';

def fibonacci_recursive(number):
	if number == 1 or number == 2:
		return 1;
	return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2);

if len(sys.argv) != 2:
	show_help();
	sys.exit();

try:
	num = int(sys.argv[1]);
	print '%dth number=%d'%(num, fibonacci_recursive(num));
	
except ValueError:
	print 'Invalid parameter';
