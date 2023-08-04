#import necessary libraries
import socket
import string
import random
  
# take the server name and port name
host = 'local host'
port = 5000
  
# create a socket at server side using TCP / IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
# bind the socket with server and port number
s.bind(('', port))
  
# allow maximum 1 connection to the socket
s.listen(1)
  
# wait till a client accept connection
c, addr = s.accept()
  
# display client address
print("CONNECTION FROM:", str(addr))

# send message to the client after encoding into binary string
#an array to store original messages on the server side
og = []

#for loop to generate 149 datapoints
for i in range(1000):

    #length of the generated string 
    N = 8

    #generate random message - combination of uppercase, lowercase, digits is generated
    message = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N)).encode('utf-8')

    #send byte-encoded message to client "c"
    c.send(message)

    #done for the purpose of running the program
    og.append(str(message))
    print("")

#print original message array for serverside
print(og)

# disconnect the server
c.close()