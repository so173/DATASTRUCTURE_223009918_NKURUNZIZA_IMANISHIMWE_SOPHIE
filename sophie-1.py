from collections import deque


class UndoStack:
    def __init__(self):
        self.stack = []

    def push(self, bid):
        self.stack.append(bid)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


class AuctionQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, request):
        self.queue.append(request)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0


class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        for item in self.items:
            if item['id'] == item_id:
                self.items.remove(item)
                return item
        return None

    def display_items(self):
        return self.items

class AuctionSystem:
    def __init__(self):
        self.items = ItemList()
        self.bids = {}
        self.undo_stack = UndoStack()
        self.auction_queue = AuctionQueue()

    def add_item(self, item):
        self.items.add_item(item)

    def place_bid(self, item_id, bidder, amount):
        if not any(item['id'] == item_id for item in self.items.items):
            print(f"Item with ID {item_id} not found!")
            return
        
        self.bids[item_id] = (bidder, amount)
        self.undo_stack.push((item_id, bidder, amount))
        print(f"Bid placed by {bidder} for {item_id} with amount {amount}")

    def undo_last_bid(self):
        last_bid = self.undo_stack.pop()
        if last_bid:
            item_id, bidder, amount = last_bid
            del self.bids[item_id]
            print(f"Bid from {bidder} for item {item_id} undone.")
        else:
            print("No bid to undo.")

    def request_auction(self, request):
        self.auction_queue.enqueue(request)

    def process_auction_request(self):
        request = self.auction_queue.dequeue()
        if request:
            print(f"Processing auction request: {request}")
        else:
            print("No auction requests to process.")

    def display_items(self):
        return self.items.display_items()

auction_system = AuctionSystem()

auction_system.add_item({'id': 1, 'name': 'Antique Vase', 'starting_price': 100})
auction_system.add_item({'id': 2, 'name': 'Vintage Watch', 'starting_price': 200})

print("Available items:", auction_system.display_items())

auction_system.place_bid(1, 'Bidder1', 150)
auction_system.place_bid(2, 'Bidder2', 250)

auction_system.undo_last_bid()


auction_system.request_auction("Auction Request 1")
auction_system.request_auction("Auction Request 2")

auction_system.process_auction_request()
auction_system.process_auction_request()

auction_system.process_auction_request()
