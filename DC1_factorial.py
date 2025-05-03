# client

import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

number = int(input("Enter an integer to compute factorial for: "))

result = server.compute_factorial(number)

print(f"The factorial of {number} is {result}")


# server

from xmlrpc.server import SimpleXMLRPCServer

def compute_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * compute_factorial(n - 1)


server = SimpleXMLRPCServer(("localhost", 8000))
print("Server listening on port 8000...")
server.register_function(compute_factorial, "compute_factorial")
server.serve_forever()
