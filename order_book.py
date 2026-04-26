from sortedcontainers import SortedDict
import itertools

class OrderBook:

    def __init__(self):
        self.bids   = SortedDict(lambda x: -x)  # descending: best bid first
        self.asks   = SortedDict()               # ascending: best ask first
        self.orders = {}                         # order_id -> (side, price, qty)
        self._id    = itertools.count(1)         # generates 1, 2, 3...

    def add_order(self, side, price, qty):
        oid  = next(self._id)
        self.orders[oid] = (side, price, qty)
        book = self.bids if side == 'buy' else self.asks
        if price not in book:
            book[price] = {}
        book[price][oid] = qty
        return oid

    def cancel_order(self, oid):
        if oid not in self.orders:
            return False
        side, price, _ = self.orders.pop(oid)
        book = self.bids if side == 'buy' else self.asks
        del book[price][oid]
        if not book[price]:
            del book[price]
        return True

    def best_bid(self):
        if not self.bids:
            return None
        price = self.bids.keys()[0]
        qty   = sum(self.bids[price].values())
        return price, qty

    def best_ask(self):
        if not self.asks:
            return None
        price = self.asks.keys()[0]
        qty   = sum(self.asks[price].values())
        return price, qty

# Verification
book = OrderBook()
book.add_order('buy',  0.52, 100)
book.add_order('buy',  0.50, 200)
book.add_order('sell', 0.55, 150)
book.add_order('sell', 0.58, 100)

print("Best bid:", book.best_bid())   # (0.52, 100)
print("Best ask:", book.best_ask())   # (0.55, 150)

oid = book.add_order('buy', 0.53, 75)
print("Best bid:", book.best_bid())   # (0.53, 75)

book.cancel_order(oid)
print("Best bid:", book.best_bid())   # (0.52, 100)
