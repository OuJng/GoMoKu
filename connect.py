from xmlrpc.server import SimpleXMLRPCServer
from game import *

if __name__ == "__main__":
    obj = game()
    server = SimpleXMLRPCServer(("0.0.0.0", 28088), allow_none=True)
    server.register_instance(obj)
    print("Listening")
    server.serve_forever()