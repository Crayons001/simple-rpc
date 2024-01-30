import xmlrpc.client

# Create a proxy that connects to your server (use the address to your server as the parameter)
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Test your rpc by calling server functions
num1 = 5
num2 = 2.5
myString = "karma"

result1 = proxy.increment(num1)
result2 = proxy.square_add(num2, num1)
result3 = proxy.reverse_string(myString)

print(f"{num1} has been incremented to {result1}")
print(f"({num2}^2) + {num1} = {result2}")
print(f"{myString} in reverse is {result3}")