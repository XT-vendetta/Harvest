from typing import Union


class Equity:
    def __init__(self, id: Union[str, int], name: str = None):
        self.id = id
        self.name = name
