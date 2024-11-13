# File: blockchain.py

import hashlib
import time

class Block:
    """Represents a single block in the blockchain."""
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Calculates the hash of the block."""
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """Represents the blockchain."""
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        """Creates the first block in the blockchain."""
        return Block(0, time.time(), "Genesis Block", "0")
    
    def get_latest_block(self):
        """Returns the latest block in the chain."""
        return self.chain[-1]
    
    def add_block(self, data):
        """Adds a new block to the chain."""
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def display_chain(self):
        """Displays the blockchain."""
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}\n")

if __name__ == "__main__":
    my_blockchain = Blockchain()
    my_blockchain.add_block("Block 1 Data")
    my_blockchain.add_block("Block 2 Data")
    my_blockchain.display_chain()
