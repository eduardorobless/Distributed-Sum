import socket 
import json 
import os 



def send_data_to_node(node_ip, node_port, numbers):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((node_ip, node_port))
    data = json.dumps(numbers) # create a json-formatted string
    client_socket.send(data.encode())  # send json-formatted string's bytes object 
    result = client_socket.recv(1024).decode()
    client_socket.close()
    return int(result)
    

# numbers to sum 

numbers = list(range(1, 101))
mid = len(numbers) // 2



# split data 
numbers_node1 = numbers[:mid]
numbers_node2 = numbers[mid:]



# send to nodes 
url_linux = '127.0.0.1'
port_linux = 5000
result1 = send_data_to_node(url_linux, port_linux, numbers_node1)

url_windows = os.getenv('URL_WINDOWS')
print(url_windows)
port_windows = 5000
result2 = send_data_to_node(url_windows, port_windows, numbers_node2)



# Combine results 
total_sum = result1 + result2 

print(f"Total sum: {total_sum}")
