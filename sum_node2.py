import socket 
import json 
import os
def sum_numbers(numbers):
    return sum(numbers)





# Prepare to receive data, socket TCP ipv4 , 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url_windows = os.getenv('MY_URL')
port_windows = 5000
server_socket.bind((url_windows, port_windows)) 
server_socket.listen(1), #backlog of zero 
print("Node 2 listening for connections...")




connection, client_address = server_socket.accept()  # accept incoming connection
# getting sequence of bytes that represent JSON data
# convert the bytes object to a Json string
data = connection.recv(1024).decode() 

# parsing json string to python object 
numbers = json.loads(data) 


result = sum_numbers(numbers)
connection.send(str(result).encode()) #encoding result to bytes object

connection.close()
server_socket.close()
