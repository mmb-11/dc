import random

servers = ["Server1", "Server2", "Server3"]

# Round Robin
class RoundRobin:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

# Random Selection
class RandomBalancer:
    def __init__(self, servers):
        self.servers = servers

    def get(self):
        return random.choice(self.servers)

# Simulate requests
def simulate(lb, count):
    for i in range(count):
        print(f"Request {i+1} → {lb.get()}")

# Run
print("Round Robin Load Balancing:")
simulate(RoundRobin(servers), 10)

print("\nRandom Load Balancing:")
simulate(RandomBalancer(servers), 10)
