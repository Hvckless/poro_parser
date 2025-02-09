from parserapp.type.Champion import Champion

class Main():
    def __init__(self)->None:

        _champion = Champion("Ahri", "https://poro.gg/legend/Ahri.png", "width:10px;")

        print(_champion.__dict__)

        pass


app = Main()