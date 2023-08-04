#import necessary libraries
import socket
import random
import secrets
import string
import pandas as pd
  
# take the server name and port name
host = 'local host'
port = 5000
  
# create a socket at client side using TCP / IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
# connect it to server and port number on local computer.
s.connect(('127.0.0.1', port))

# create empty arrays for original, modified strings, class labels
original_strings = []
modified_strings = []
label = []

# define the probability of modifying each message
p = 0.35

message = s.recv(1024)
# receive messages from the server until there are no more
while message:

    # receive a message from the server    
    message = s.recv(1024)

    # if the message is empty, break out of the loop
    if not message:
        break

    #randomly modify the message with probability p
    if random.random() < p:

        #randomly select the index where the message is injected
        n = random.randint(2,len(message.decode()))

        #length of injected string
        N = 2

        #modify the message
        modified_string = (str(message.decode())[0:n-2] + ''.join(random.choices(string.ascii_uppercase +
                                                                                  string.digits + string.ascii_lowercase, k=N))
                                                                                    + str(message.decode())[n:len(message.decode())])

        # append the original and modified strings to their respective arrays
        original_strings.append(message.decode())
        modified_strings.append(modified_string)

        #class label = 1 for modified strings
        label.append(1)

    else:
        # append the original string to the original strings array without modifying it
        original_strings.append(message.decode())

        # append the original string to the modified strings array to indicate that it was not modified
        modified_strings.append(message.decode())

        #class label = 0 for original strings
        label.append(0)

# close the socket
s.close()

# print the original, modified strings, class labels for client side
print("Original strings:", original_strings)
print("Modified strings:", modified_strings)
print("Labels:",label)

#convert the arrays to a dataframe using pandas
df = pd.DataFrame(list(zip(original_strings, modified_strings,label)), columns = ['Original_strings','Modified_strings', 'Labels'])

#use pandas function to convert df to csv and export 
df.to_csv(r'C:\Users\{username}\Desktop\bigdata.csv')

#indicative of when the process has fully run
print("Done")




