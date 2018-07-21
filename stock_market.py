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
	def __init__(self, book_type):
		self.book_type = book_type
		self.bids = []
		self.priorities = ["price"] # Dictates how this Book will be sorted, defaults to price

	def __str__(self):  # allows us to call str(my_bid) and print(my_bid)
		return "\n".join(map(str, self.bids))

	# Sets new priorities for the book and sorts the book
	def set_priorities(self, *args):
		new_priorities = []
		for priority in args:
			new_priorities.append(priority)
		self.priorities = new_priorities

		if len(self.bids) > 1:
			self.sort_book()

	# Sorts book according to priorities
	def sort_book(self):
		# compare_bids_parameters = tuple(["bid."+x for x in self.priorities])
		# print(compare_bids_parameters)
		# # Comparator function for sorting
		# compare_bids = lambda bid: compare_bids_parameters

		if self.book_type == "bid":
			compare_bids = lambda bid: (bid.price, bid.visibility)
			self.bids.sort(key = compare_bids, reverse = True)
		else:
			compare_bids = lambda bid: (bid.price, -bid.visibility)
			self.bids.sort(key = compare_bids, reverse = False)

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

	# Offers
	gregori_offer = Bid(20.20, True, "Gregori")
	haley_offer = Bid(20.18, True, "Haley")
	inez_offer = Bid(20.18, False, "Inez")
	jing_offer = Bid(20.10, False, "Jing")
	kala_offer = Bid(20.15, True, "Kala")
	lou_offer = Bid(20.18, True, "Lou")

	# Bid book
	bid_book = Book("bid")
	# bid_book.set_priorities("price", "visibility")
	bid_book.submit_bid(amy_bid)
	bid_book.submit_bid(brian_bid)
	bid_book.submit_bid(chao_bid)
	bid_book.submit_bid(dmitri_bid)
	bid_book.submit_bid(esteban_bid)
	bid_book.submit_bid(florio_bid)

	# Offer book
	offer_book = Book("offer")
	# offer_book.set_priorities("price", "visibility")
	offer_book.submit_bid(gregori_offer)
	offer_book.submit_bid(haley_offer)
	offer_book.submit_bid(inez_offer)
	offer_book.submit_bid(jing_offer)
	offer_book.submit_bid(kala_offer)
	offer_book.submit_bid(lou_offer)

	# Testing
	print("Bid Book: \n" + str(bid_book) + "\n")
	print("Offer Book: \n" + str(offer_book))

if __name__ == '__main__':
	main()
