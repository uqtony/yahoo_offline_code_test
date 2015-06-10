
import sys;

# show help
def show_help():
	print '[Usage] python fibonacci_loop.py [N]\tShow Nth value on Fibonacci sequence';

def fibonacci_loop(number):
	if number == 1 or number == 2:
		return 1;
	fib1 = 1;
	fib2 = 1;
	result = 1;
	number -= 3;
	while number >= 0:
		result = fib1 + fib2;
		fib1 = fib2;
		fib2 = result;
		number -= 1;
	return result;

if len(sys.argv) != 2:
	show_help();
	sys.exit();

try:
	num = int(sys.argv[1]);
	print '%dth number=%d'%(num, fibonacci_loop(num));
	
except ValueError:
	print 'Invalid parameter';
