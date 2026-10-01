'''26. Web Browser Cache
A web browser stores a limited number of recently accessed pages. When the storage becomes full, 
the page that has remained unused for the longest time should be removed to make space for a new page.
Design a solution that manages these page-access operations efficiently.
'''

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def access_page(self, page):
        if page in self.cache:
            self.cache.move_to_end(page)
            print("Page accessed:", page)
        else:
            if len(self.cache) >= self.capacity:
                removed = self.cache.popitem(last=False)
                print("Removed:", removed[0])

            self.cache[page] = True
            print("Page added:", page)

    def display(self):
        print("Cache:", list(self.cache.keys()))


cache = LRUCache(3)

cache.access_page("Google")
cache.access_page("YouTube")
cache.access_page("Facebook")
cache.access_page("Google")
cache.access_page("Amazon")

cache.display()