import pygal
from random import randint

# Take user input to determine how many dice to roll, and what kind of 
# dice to roll. Make sure the user input is an integer.

qty_1 = input("How many dice are you rolling?: ") 
qty_2 = input("What type of dice are you rolling?: ") 
qty_1 = int(qty_1)
qty_2 = int(qty_2)

# Define a class for "dice" and write a function to return a random 
# number that can be rolled on it.
	
class Die():
	def __init__(self, num_dice, faces):
		self.num_dice = num_dice
		self.faces = faces
	
	def roll(self):
		running_total = []
		for num in range(self.num_dice):
			running_total.append(randint(1, int(self.faces)))
		running_total = sum(running_total)
		return running_total

dice = Die(qty_1, qty_2)

all_results = []

# Repeat the process 5000 times and store every result to a list.

for num in range(5000):
	x = dice.roll()
	all_results.append(x)

frequencies = []

# Count how many times each possible result was returned.

for value in range(qty_1, qty_2 * qty_1 + 1):
	frequency = all_results.count(value)
	frequencies.append(frequency)

# Output the results as a bar graph to visualize the probability of
# each possible result and save the graph as an SVG image file.

hist = pygal.Bar()

hist.title = "Results of rolling %sd%s 5000 times" % (qty_1, qty_2)
hist.x_labels = []
for i in range(qty_1, qty_2 * qty_1):
	hist.x_labels.append(str(i))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('d%s' % (qty_2), frequencies)
hist.render_to_file('die_visual.svg')
