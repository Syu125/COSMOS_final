from LEDonly import Light 
from markovONLY import piece
import threading
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 3000)
sock.bind(server_address)
print('starting up on {} port {}'.format(*server_address))

# Listen for incoming connections
sock.listen(1)
print('listening')

light = Light()
print('lights initialized')

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            play = True
            data = connection.recv(16)
            data = data[:-2].split(b' ')
           # dat = data[1].split(b' ')
            command = data[0]
            if command == b'tempo':
                value = float(data[1])
                tempo = value
                print("got tempo")
                t = threading.Thread(target = light.run, args = (tempo,))
                t.start()
            elif command == b'startNotes':
                value = int(data[1])
                r = piece(value)
                for i in range (len(r)):
                    byteSent = connection.send(bytes(str(r[i])+';', 'utf8'))
                    #connection.send(bytes(str(r[i]), 'utf8'))
                    print ("final: " + str(r[i])+ str(byteSent))
            elif command == b'stopLights':
                light.stop()
            else:
                print("unknown command {}".format(command))
           
            
            
            
                
            
#           t = threading.Thread(target = piece, args = (20,))
#           t.start()

           

                    
    finally:
        # Clean up the connection
        connection.close()
            
        
