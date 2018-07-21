import datetime

class Bid:
	def __init__(self, price, visibility, trader):
		self.price = price
		self.visibility = visibility # True = visible, False = Hidden
		self.time = None  # not yet submitted
		self.trader = trader

	def __str__(self):  # allows us to call str(my_bid) and print(my_bid)
		return "{}\t{}\t{}\t{}".format(self.price, self.visibility, self.time.strftime("%H:%M:%S:%f"), self.trader)

class Book:
	def __init__(self):
		self.bids = []

	def __str__(self):  # allows us to call str(my_bid) and print(my_bid)
		return "\n".join(map(str, self.bids))

	def sort_book(self):
		# Comparator function for sorting
		compare_bids = lambda bid: (bid.price, bid.visibility)
		self.bids.sort(key = compare_bids, reverse = True)

	def submit_bid(self, bid):
		bid.time = datetime.datetime.now()
		self.bids.append(bid)
		self.sort_book()  # sort book every time a bid is added


def main():
	# Bids
	amy_bid = Bid(20.05, False, "Amy")
	brian_bid = Bid(20.04, True, "Brian")
	chao_bid = Bid(20.04, True, "Chao")
	dmitri_bid = Bid(20.05, True, "Dmitri")
	esteban_bid = Bid(20.03, True, "Esteban")
	florio_bid = Bid(20.06, False, "Florio")

	# Bid book
	book = Book()
	book.submit_bid(amy_bid)
	book.submit_bid(brian_bid)
	book.submit_bid(chao_bid)
	book.submit_bid(dmitri_bid)
	book.submit_bid(esteban_bid)
	book.submit_bid(florio_bid)

	# Testing
	print(book)

if __name__ == '__main__':
	main()
