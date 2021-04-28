
#!/usr/bin/python3

import sys

# Navigieren Sie zum Ablageort der Datei Blatt1. py und fuehren Sie das Programm ueber die Kommandozeile aus.

def hello_world():
    print("Hello Student!")

def hello_user():
    user_name = raw_input("Please enter your name. \n")
    print("Hello "+ user_name +"! Welcome to your first worksheet! You did great!")

def decode_message():
    user_message = raw_input("Please enter the secret Message: \n")
    correct_message = "V2VsbCBkb25lISBUaGlzIGlzIHlvdXIgcHJpemU6IGh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9ZFF3NHc5V2dYY1Eg"
    if user_message == correct_message:
        print("Decoded String: " + user_message.decode('base64','strict'))

if __name__ == "__main__":
    hello_world()
    hello_user()
    decode_message()