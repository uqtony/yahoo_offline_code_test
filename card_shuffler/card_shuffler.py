
import sys;
import random;

# show help
def show_help():
	print '[Usage]python card_shuffler.py [number_of_cards]\t Shuffle deck with size=number_of_cards';

def show_menu():
	print '1. Pick one';
	print '2. Shuffle';
	print '3. Exit';
	try:
		return int(input('Enter choice(1-3):'));
	except ValueError:
		return -1;

class CardShuffler:
	def __init__(self, number_of_cards):
		self.cards = [];
		self.pick_cards = [];
		self.prepare_cards(number_of_cards);

	def prepare_cards(self, number_of_cards):
		for idx in range(0, number_of_cards):
			self.cards.append(idx);

	def shuffle_cards(self):
		while len(self.pick_cards) > 0:
			self.cards.append(self.pick_cards.pop());

	def pick_card(self):
		if len(self.cards) <= 0:
			return -1;	
		idx = self.cards.pop(random.randint(0, len(self.cards)-1));
		self.pick_cards.append(idx);
		return idx;

if len(sys.argv) != 2:
	show_help();
	sys.exit();
number_of_cards = 0;
try:
	number_of_cards = int(sys.argv[1]);
except ValueError:
	print 'Invalid parameter';
	sys.exit();

cardShuffler = CardShuffler(number_of_cards);
user_input = show_menu();
while user_input != 3:
	if user_input == 1:
		idx = cardShuffler.pick_card();
		if idx != -1:
			print 'Pick:%d' %(idx);
		else:
			print 'No card';
	elif user_input == 2:
		cardShuffler.shuffle_cards();
		print 'Shuffle cards';
	else:
		print 'Invalid option';
	user_input = show_menu();
print 'Bye';
