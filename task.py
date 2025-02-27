class Counter:
    def __init__(self, start=0, stop=None):
        self.value = start
        self.stop = stop

    def increment(self):
        if self.stop is not None and self.value >= self.stop:
            print("Maximal value is reached.")
        else:
            self.value += 1

    def get(self):
        return self.value

    # Example Usage:


c = Counter(start=42)
c.increment()
print(c.get())  # Output: 43

c = Counter()
c.increment()
print(c.get())  # Output: 1
c.increment()
print(c.get())  # Output: 2

c = Counter(start=42, stop=43)
c.increment()
print(c.get())  # Output: 43
c.increment()  # Output: Maximal value is reached.
print(c.get())  # Output: 43

