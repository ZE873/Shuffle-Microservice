HOW TO REQUEST DATA FROM THE MICROSERVICE:
- connect to zmq local host using REQ
    - I used localhost:5553, but you can change this, just make sure both your project and
        the microservice are using are on the same host
- send a string, should start with one of the three commands R, P, or F, commands must be capital
- rest of the string should contain 1s and 0s separated by commas,
    - 1 indicates the card is high priority
    - 0 indicates the card is low priority

Example:

create context
socket connect for request
connect to the local host
socket.send_string("R,1,0,0,0,1,1,1")

HOW TO RECEIVE DATA FROM THE MICROSERVICE:
- wait for a message back from the microservice
- if the format was invalid, it will send "invalid" back
- otherwise it will send back a string of shuffled indexes separated by commas

Example:

server_message = socket.recv()
printf(f'Server sent back: {server_message.decode()})

ex output:
"Server sent back: 6,3,5,0,1,2 "
