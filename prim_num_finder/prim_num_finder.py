import sys;


# Show help
def show_help():
	print "usage: python prim_num_finder.py [max_value]\tfind prime number between 1 to max_value";

prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];

def find_in_predefine_prime_number(max_value):

	if max_value > 100:
		return None;	
	elif max_value >=97:
		return prime;
	if max_value <= 1:
		return None;
	elif max_value <= 2:
		return [2];

	idx = len(prime)-1;

	while idx >= 0:
		if prime[idx] <= max_value:
			return prime[:idx];
		idx -= 1;	

	return None;

def find_prime_number(max_value):

	if max_value <= 1:
		return None;
	result = find_in_predefine_prime_number(max_value);
	if result is not None:
		return result;	
	
	result = prime;
	idx = 101;
	while idx <= max_value:
		is_prime = True;
		i = len(result) - 1;
		while i >= 0:
			if idx % result[i] == 0:
				is_prime = False;
				break;
			i -= 1;
		if is_prime == True:
			result.append(idx);
		idx += 2;
	return result;

if len(sys.argv) != 2:
	show_help();
else:
	try:
		result = find_prime_number(int(sys.argv[1]));
		if result is None:
			print "None result";
		else:
			for num in result:
				print num;
	except ValueError:
		print "Invalid parameters";
