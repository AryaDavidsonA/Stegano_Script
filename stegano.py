import Decode
import Encode


def stego():
    
    Choice = int(input("Please choose your option!!! \n 1. Encrypt \n 2. Decrypt \n Enter your choice here : "))
    if Choice == 1:
        first = input("Enter the first image file : ")
        second = input("Enter the image file for hide : ")
        Encode.encode(first, second)
        print("Given image encoded successfully and saved as hidden.png!!!")

    elif Choice == 2:
        dec = input("Enter the image for decode : ")
        Decode.decode()
        print("Your image decoded successfully from ", dec," and saved as saved.png!!!")
    else:
        raise ValueError("Input valid data")


stego()

