import sys;

def get_medium_number(numbers):
	len_of_numbers = len(numbers);
	if len_of_numbers <= 0:
		return None;
	sorted_list = [];
	for num in numbers:
		i = 0;
		while i < len(sorted_list):
			if sorted_list[i] <= num:
				break;
			i += 1;
		sorted_list.insert(i, num);
	if len_of_numbers % 2 == 0:
		return (sorted_list[len_of_numbers/2-1] + sorted_list[len_of_numbers/2])/2;
	else:
		return sorted_list[len_of_numbers/2];

user_input = raw_input('Input series of number, please separate with ",", (ex: 1,3,4): ');
text_list = user_input.split(',');
number_list = [];
for text in text_list:
	try:
		number_list.append(int(text));
	except ValueError:
		# Do Nothing
		print

medium_number = get_medium_number(number_list);
if medium_number is not None:
	print 'medium number=%d' %(medium_number);
else:
	print 'Medium number not found';

