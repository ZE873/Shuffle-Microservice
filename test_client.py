import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5553")


def foe_input():
    user_input = input("input a test input: ")
    return user_input


while True:

    send = foe_input()

    if send == "Q":
        break

    socket.send_string(send)

    server_message = socket.recv()
    print(f'Server sent back:  {server_message.decode()}')
