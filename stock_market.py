class bid:
    def __init__(self, price, visibility, time, trader):
        self.price = price
        self.visibility = visibility
        self.time = time
        self.trader = trader

class bidBook:
    def __init__(self):
        self.bids = []

""" Build the buy side of the limit order bidBook """
# Step 1. Sort the bids by price
def sortByPrice(bidBook):
    bidBook.bids.sort(key = lambda x: x.price, reverse=True)
    return bidBook

def sortByVisibilityHelper(bids):
    if len(bids) > 1:
        for x,y in bids:
            print(x, y)

sortByVisibilityHelper([])

# Step 2. Sort orders at the same price by visibility
def sortByVisibility(bidBook):
    if len(bidBook) < 2:
        return bidBook


    pass

""" General Functions """
# Print the limit order book
def printLimitOrderBook(bidBook):
    print("Price\tVisibility\tTime\tTrader")
    for bid in bidBook.bids:
        print("{}\t{}\t\t{}\t{}".format(bid.price, bid.visibility, bid.time, bid.trader))

def main():
    # Initialize Variables
    # Bids
    florio_bid = bid(20.06, "Hidden", 9.35, "Florio")
    amy_bid = bid(20.05, "Hidden", 9.30, "Amy")
    dmitri_bid = bid(20.05, "", 9.33, "Dmitri")
    brian_bid = bid(20.04, "", 9.31, "Brian")
    chao_bid = bid(20.04, "", 9.32, "Chao")
    esteban_bid = bid(20.03, "", 9.34, "Esteban")

    # BidBook
    test_bidBook = bidBook()
    test_bidBook.bids.append(amy_bid)
    test_bidBook.bids.append(brian_bid)
    test_bidBook.bids.append(chao_bid)
    test_bidBook.bids.append(dmitri_bid)
    test_bidBook.bids.append(esteban_bid)
    test_bidBook.bids.append(florio_bid)

    # Testing
    print("Original Book")
    printLimitOrderBook(test_bidBook)
    print()
    test_bidBook = sortByPrice(test_bidBook)
    print("Book after sort")
    printLimitOrderBook(test_bidBook)

if __name__ == '__main__':
    main()
