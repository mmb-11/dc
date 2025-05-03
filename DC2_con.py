#Server
import Pyro4

class StringConcatenator:
    @Pyro4.expose
    def concatenate(self, str1, str2):
        return f"{str1} {str2}"
        
def start_server():
    concatenator = StringConcatenator()
    daemon = Pyro4.Daemon()
    uri = daemon.register(concatenator)
    print("Server URI:", uri)
    print("Server is ready. Waiting for requests...")
    daemon.requestLoop()
    
if __name__ == "__main__":
    start_server()

#Client
import Pyro4

def main():
    uri = input("Enter the server's URI: ")
    concatenator = Pyro4.Proxy(uri)
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    result = concatenator.concatenate(str1, str2)
    print("Concatenated string:", result)

if __name__ == "__main__":
    main()
