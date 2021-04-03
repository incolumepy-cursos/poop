__author__ = '@britodfbr'

import pathlib
from head_first_design_patterns.strategy.duck import Duck
from head_first_design_patterns.strategy.fly_behavior import FlyNoWay
from head_first_design_patterns.strategy.quack_behavior import MuteQuack


class DuckHOF(Duck):
    def __init__(self):
        # override the method with pre defined values
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def perform_fly(self):
        return self.fly_behavior.fly()

    def perform_quack(self):
        return self.quack_behavior.quack()

    def display(self):
        # print(dir(self))
        print(f"{self.__class__.__name__} (fly: {self.perform_fly()}; croak: {self.perform_quack()})")
