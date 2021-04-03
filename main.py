__author__ = '@britodfbr'

from head_first_design_patterns.strategy import mini_duck_simulator
from head_first_design_patterns.hofs import duck_dispenser
from head_first_design_patterns.hofs_dinamics import duck_dispenser as dinamic_duck_dispenser


def strategy():
    mini_duck_simulator.run()


def hof():
    duck_dispenser.run()

def hof_dinamic():
    dinamic_duck_dispenser.run()

def run():
    print("\n\n======= Pattern HOF Dinamic===========")
    hof_dinamic()

    print("\n\n======= Pattern HOF ===========")
    hof()

    print("\n\n======= Pattern Strategy ===========")
    strategy()


if __name__ == "__main__":
    run()
