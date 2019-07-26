
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 3000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

from gpiozero import LED
from time import sleep
import time
import random
pattern = random.randint(1,8)
song = False
count = 0
f = 60
T = 1/f
p = 0.9
red1 = LED(17)
orange1 = LED(18)
yellow1 = LED(27)
green1 = LED(22)
blue1 = LED(23)
white1 = LED(24)
red2 = LED(13)
orange2 = LED(19)
yellow2 = LED(26)
green2 = LED(16)
blue2 = LED(20)
white2 = LED(21)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print (data)
            (command, value) = data.split(b' ')
            value = float(value[:-2])
            print (command, value)
            tempo = value
            song = True
            
            while song == True:
#               #in order 2 (slow)
                while pattern == 1 and count <= 3:
                    beat = tempo/6000
                    red1.on()
                    time.sleep(beat)
                    red1.off()
                    
                    orange1.on()
                    time.sleep(beat)
                    orange1.off()
                    
                    yellow1.on()
                    time.sleep(beat)
                    yellow1.off()
                    
                    green1.on()
                    time.sleep(beat)
                    green1.off()
                    
                    blue1.on()
                    time.sleep(beat)
                    blue1.off()
                    
                    white1.on()
                    time.sleep(beat)
                    white1.off()
                    
                    red2.on()
                    time.sleep(beat)
                    red2.off()
                    
                    orange2.on()
                    time.sleep(beat)
                    orange2.off()
                    
                    yellow2.on()
                    time.sleep(beat)
                    yellow2.off()
                    
                    green2.on()
                    time.sleep(beat)
                    green2.off()
                    
                    blue2.on()
                    time.sleep(beat)
                    blue2.off()
                    
                    white2.on()
                    time.sleep(beat)
                    white2.off()
                    
                    count +=1
            
                
                #alternating
                while pattern == 2 and count <= 1:
                    beat = tempo/3000
                    
                    red1.on()
                    time.sleep(beat)
                    red1.off()
                
                    yellow1.on()
                    time.sleep(beat)
                    yellow1.off()
                
                    blue1.on()
                    time.sleep(beat)
                    blue1.off()
                
                    red2.on()
                    time.sleep(beat)
                    red2.off()
                
                    yellow2.on()
                    time.sleep(beat)
                    yellow2.off()
                
                    blue2.on()
                    time.sleep(beat)
                    blue2.off()
                
                    orange1.on()
                    time.sleep(beat)
                    orange1.off()
                
                    green1.on()
                    time.sleep(beat)
                    green1.off()
                
                    white1.on()
                    time.sleep(beat)
                    white1.off()
                
                    orange2.on()
                    time.sleep(beat)
                    orange2.off()
                
                    green2.on()
                    time.sleep(beat)
                    green2.off()
                
                    white2.on()
                    time.sleep(beat)
                    white2.off()
                    
                    count +=1
                    
                #in order (fast)    
                while pattern == 3 and count <=7:
                    beat = tempo/12000
                    red1.on()
                    time.sleep(beat)
                    red1.off()
                    
                    orange1.on()
                    time.sleep(beat)
                    orange1.off()
                    
                    yellow1.on()
                    time.sleep(beat)
                    yellow1.off()
                    
                    green1.on()
                    time.sleep(beat)
                    green1.off()
                    
                    blue1.on()
                    time.sleep(beat)
                    blue1.off()
                    
                    white1.on()
                    time.sleep(beat)
                    white1.off()
                    
                    red2.on()
                    time.sleep(beat)
                    red2.off()
                    
                    orange2.on()
                    time.sleep(beat)
                    orange2.off()
                    
                    yellow2.on()
                    time.sleep(beat)
                    yellow2.off()
                    
                    green2.on()
                    time.sleep(beat)
                    green2.off()
                    
                    blue2.on()
                    time.sleep(beat)
                    blue2.off()
                    
                    white2.on()
                    time.sleep(beat)
                    white2.off()
                    
                    count +=1
                    
                #spreading out    
                while pattern == 4 and count <= 7:
                    beat = tempo/10000
                    white1.on()
                    red2.on()
                    time.sleep(beat)
                    white1.off()
                    red2.off()

                    blue1.on()
                    orange2.on()
                    time.sleep(beat)
                    blue1.off()
                    orange2.off()
                    
                    green1.on()
                    yellow2.on()
                    time.sleep(beat)
                    green1.off()
                    yellow2.off()
                    
                    yellow1.on()
                    green2.on()
                    time.sleep(beat)
                    yellow1.off()
                    green2.off()
                    
                    orange1.on()
                    blue2.on()
                    time.sleep(beat)
                    orange1.off()
                    blue2.off()
                    
                    red1.on()
                    white2.on()
                    time.sleep(beat)
                    red1.off()
                    white2.off()

                    blue2.on()
                    orange1.on()
                    time.sleep(beat)
                    blue2.off()
                    orange1.off()
                    
                    green2.on()
                    yellow1.on()
                    time.sleep(beat)
                    green2.off()
                    yellow1.off()
                    
                    yellow2.on()
                    green1.on()
                    time.sleep(beat)
                    yellow2.off()
                    green1.off()
                    
                    orange2.on()
                    blue1.on()
                    time.sleep(beat)
                    orange2.off()
                    blue1.off()
                    
                    count +=1
                    
                #color-by-color    
                while pattern == 5 and count <= 7:
                    beat = tempo/6000
                    red1.on()
                    red2.on()
                    time.sleep(beat)
                    red1.off()
                    red2.off()
                    
                    orange1.on()
                    orange2.on()
                    time.sleep(beat)
                    orange1.off()
                    orange2.off()
                    
                    yellow1.on()
                    yellow2.on()
                    time.sleep(beat)
                    yellow1.off()
                    yellow2.off()
                    
                    green1.on()
                    green2.on()
                    time.sleep(beat)
                    green1.off()
                    green2.off()
                    
                    blue1.on()
                    blue2.on()
                    time.sleep(beat)
                    blue1.off()
                    blue2.off()
                    
                    white1.on()
                    white2.on()
                    time.sleep(beat)
                    white1.off()
                    white2.off()
                    
                    count +=1
                 
                #in order alternating
                while pattern == 6 and count <=3:
                    beat = tempo/5000
                    
                    red1.on()
                    yellow1.on()
                    time.sleep(beat)
                    red1.off()
                    yellow1.off()
                    
                    orange1.on()
                    green1.on()
                    time.sleep(beat)
                    orange1.off()
                    green1.off()
                    
                    yellow1.on()
                    blue1.on()
                    time.sleep(beat)
                    yellow1.off()
                    blue1.off()
                    
                    green1.on()
                    white1.on()
                    time.sleep(beat)
                    green1.off()
                    white1.off()
                    
                    blue1.on()
                    red2.on()
                    time.sleep(beat)
                    blue1.off()
                    red2.off()
                    
                    white1.on()
                    orange2.on()
                    time.sleep(beat)
                    white1.off()
                    orange2.off()
                    
                    red2.on()
                    yellow2.on()
                    time.sleep(beat)
                    red2.off()
                    yellow2.off()
                    
                    orange2.on()
                    green2.on()
                    time.sleep(beat)
                    orange2.off()
                    green2.off()
                    
                    yellow2.on()
                    blue2.on()
                    time.sleep(beat)
                    yellow2.off()
                    blue2.off()
                    
                    green2.on()
                    white2.on()
                    time.sleep(beat)
                    green2.off()
                    white2.off()
                    
                    count +=1
                    
                #two colors at a time in order
                while pattern == 7 and count <=3:
                    beat = tempo/10000
                    red1.on()
                    orange1.on()
                    time.sleep(beat)
                    red1.off()
                    
                    yellow1.on()
                    time.sleep(beat)
                    orange1.off()
                    
                    green1.on()
                    time.sleep(beat)
                    yellow1.off()
                    
                    blue1.on()
                    time.sleep(beat)
                    green1.off()
                    
                    white1.on()
                    time.sleep(beat)
                    blue1.off()
                    
                    red2.on()
                    time.sleep(beat)
                    white1.off()
                    
                    orange2.on()
                    time.sleep(beat)
                    red2.off()
                    
                    yellow2.on()
                    time.sleep(beat)
                    orange2.off()
                    
                    green2.on()
                    time.sleep(beat)
                    yellow2.off()
                    
                    blue2.on()
                    time.sleep(beat)
                    green2.off()
                    
                    white2.on()
                    time.sleep(beat)
                    blue2.off()
                    
                    blue2.on()
                    time.sleep(beat)
                    white2.off()
                    
                    green2.on()
                    time.sleep(beat)
                    blue2.off()
                    
                    yellow2.on()
                    time.sleep(beat)
                    green2.off()
                    
                    orange2.on()
                    time.sleep(beat)
                    yellow2.off()
                    
                    red2.on()
                    time.sleep(beat)
                    orange2.off()
                    
                    white1.on()
                    time.sleep(beat)
                    red2.off()
                    
                    blue1.on()
                    time.sleep(beat)
                    white1.off()
                    
                    green1.on()
                    time.sleep(beat)
                    blue1.off()
                    
                    yellow1.on()
                    time.sleep(beat)
                    green1.off()
                      
                    orange1.on()
                    time.sleep(beat)
                    yellow1.off()
                    
                    red1.on()
                    time.sleep(beat)
                    red1.off()
                    
                    count +=1
#                    
                else:
                    count = 0
                    red1.off()
                    orange1.off()
                    yellow1.off()
                    green1.off()
                    blue1.off()
                    white1.off()
                    red2.off()
                    orange2.off()
                    yellow2.off()
                    green2.off()
                    blue2.off()
                    white2.off()
                    pattern = random.randint(1,8)
                    
                    
    finally:
        # Clean up the connection
        connection.close()
            
        
