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
url1 = '127.0.0.1'
port1 = 5000
result1 = send_data_to_node(url1, port1, numbers_node1)

url2 = os.getenv('HOST11')
port2 = 5000
result2 = send_data_to_node(url2, port2, numbers_node2)



# Combine results 
total_sum = result1 + result2 

print(f"Total sum: {total_sum}")
