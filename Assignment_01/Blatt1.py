#!/usr/bin/env python
 #-*- coding: utf-8 -*-

import sys
import base64

# Navigieren Sie zum Ablageort der Datei Blatt1. py und fuehren Sie das Programm ueber die Kommandozeile aus.



def hello_world():
    print("Hello Student!")
    print("This is the secret message - Please copy it to find out your prize. ")
    print("aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==")
def hello_user():
    user_name = input("Please enter your name. \n")
    print("Hello "+ user_name +"! Welcome to your first worksheet! You did great!")

def decode_message():
    user_message = input("Please enter the secret Message: \n")
    correct_message = "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ=="
    if user_message == correct_message:
        print("Finally we got it! Enjoy some fun music :)" , base64.b64decode(user_message).decode('utf-8')  )
      

if __name__ == "__main__":
    hello_world()
    hello_user()
    decode_message()
    
   



