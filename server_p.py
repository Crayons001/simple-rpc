from xmlrpc.server import SimpleXMLRPCServer

# Functions that the server can perform

def increment(num):
    return num + 1

def square_add(num1, num2):
    return (num1**2) + num2

def reverse_string(inputString):
    return inputString[::-1]

# Create an XMLRPC server object, with address and port as parameters (as a tuple)
server = SimpleXMLRPCServer(("localhost", 8000))

# Register the server functions to xmlrpc so they can be called remotely using rpc
server.register_function(increment)
server.register_function(square_add)
server.register_function(reverse_string)

# Start the server and set it to accept requests indefinitely as long as server is up
server.serve_forever()