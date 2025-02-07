import os

class Initializer:
    def __init__(self):
        self.initial = 1

        if(os.path.isdir("./champion_data")):
            print("HELLO?")
        else:
            print("BYE")

        print("A")