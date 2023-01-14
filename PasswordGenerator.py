import random

alphanumeric = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", \
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", \
             "Y", "Z", \
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", \
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", \
             "y", "z", \
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

alphanumericPlus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", \
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", \
             "Y", "Z", \
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", \
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", \
             "y", "z", \
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", \
             "!", "@", "#", "$", "%", "^", "&", "*","+", "=", "?"]

while True:
    session = input ("Choose: /n 1. 2.:")
    if session == "1":
        print (random.choices(alphanumeric, k=10))
    if session == "2":
        print (random.choices(alphanumericPlus, k=10))
