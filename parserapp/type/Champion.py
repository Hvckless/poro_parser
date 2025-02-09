from dataclasses import dataclass, asdict

from parserapp.type.JSON import JSON

@dataclass
class Champion(JSON):
    name:str
    source_url:str
    css_style_code:str

    def __init__(self, name:str, source_url:str, css_style_code:str) -> None:
        self.name = name
        self.source_url = source_url
        self.css_style_code = css_style_code
        pass



    def setName(self, name:str)->None:
        self.name = name
    def setSourceURL(self, source_url:str)->None:
        self.source_url = source_url
    def setCSSStyleCode(self, css_style_code:str)->None:
        self.css_style_code = css_style_code

    def getName(self)->str:
        return self.name
    def getSourceURL(self)->str:
        return self.source_url
    def getCSSStyleCode(self)->str:
        return self.css_style_code