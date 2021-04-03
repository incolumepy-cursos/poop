__author__ = '@britodfbr'

class DuckHOFDinamic:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def display(self):
        # print(dir(self))
        print(f"{self.__class__.__name__} (fly: {self.perform_fly()}; croak: {self.perform_quack()})")
