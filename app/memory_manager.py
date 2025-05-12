# memory_manager.py

class LongTermMemory:
    def __init__(self):
        self.memory_store = []

    def add_entry(self, context):
        self.memory_store.append(context)

    def retrieve_recent(self, n=3):
        return self.memory_store[-n:] if self.memory_store else []

# Example test
if __name__ == "__main__":
    mem = LongTermMemory()
    mem.add_entry("Test context 1")
    mem.add_entry("Test context 2")
    print(mem.retrieve_recent())
