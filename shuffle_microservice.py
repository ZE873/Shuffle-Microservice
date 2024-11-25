import zmq
import random


def shuffle_norm(norm_list): # shuffles all cards in the list
    norm_list.pop(0) # remove the command
    val = []

    for x in range(len(norm_list)): # add all indexes to a list
        val.append(x) #

    random.shuffle(val) # shuffle list
    print(val)
    return val


def shuffle_priority(all_cards): # shuffle only the high priority cards in the list
    all_cards.pop(0) # remove the command
    val = []
    val_index = 0

    for x in all_cards:
        if int(x) == 1: # add indexes of only priority cards
            val.append(val_index)
        val_index = val_index + 1 # track index

    random.shuffle(val) # shuffle the list of priority cards
    print(val)
    return val


def shuffle_front(full_list):
    full_list.pop(0) # remove command
    priority = []
    reg = []
    val_index = 0
    for x in full_list:
        if int(x) == 1: # add just priority
            priority.append(val_index)
        else:
            reg.append(val_index) # otherwise non priority
        val_index = val_index + 1

    # shuffle both independently
    random.shuffle(reg)
    random.shuffle(priority)

    all_shuffled = priority + reg # add priority before non priority

    print(all_shuffled)
    return all_shuffled


def create_list(cards): # decodes and reformat all string values sent by client
    c_list = cards.decode().split(",")
    return c_list


def string_output(list_output): # reformat the lists into strings as tokens separated by ","

    str_output = ""
    count = 0
    for x in list_output:
        if count != len(list_output) - 1: # if catches commas from being added to the end
            str_output = str_output + str(x) + ","
        else:
            str_output = str_output + str(x)
        count = count + 1
    return str_output


context = zmq.Context()

socket = context.socket(zmq.REP)

socket.bind("tcp://localhost:5553")

# VALID EXAMPLE STRING FROM CLIENT: R,1,1,1,0,0,1,1,0,1

while True:

    cards_to_shuffle = socket.recv()

    if len(cards_to_shuffle) > 0:
        card_list = create_list(cards_to_shuffle)
        output = ""

        if card_list[0] == 'R': # R command for shuffle normal
            output = shuffle_norm(card_list)

        if card_list[0] == 'P': # P command for shuffling all non priority
            output = shuffle_priority(card_list)

        if card_list[0] == 'F': # F command for shuffling both but front loading with priority
            output = shuffle_front(card_list)

        if input == "Q":
            break

        if output == "": # if input does not contain any commands
            output = "invalid"
        else:
            output = string_output(output)

        socket.send_string(output)
