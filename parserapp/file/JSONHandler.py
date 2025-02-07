import json

from ..type.JSON import JSON

class JSONHandler:
    def __init__(self) -> None:
        pass

    def createJSONFile(self, requested_filename:str, json_object:JSON)->None:

        json_dump:JSON = {}
        if(json_object is not None):
            json_dump = json_object

        filename:str

        if(len(requested_filename) < 1):
            filename = "empty.json"
        else:
            filename = requested_filename

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(json_dump, f, indent=4)
