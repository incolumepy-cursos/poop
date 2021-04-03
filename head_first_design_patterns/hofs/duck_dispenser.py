__author__ = '@britodfbr'

from head_first_design_patterns.hofs import duck
from head_first_design_patterns.hofs import fly_behaviors
from head_first_design_patterns.hofs import quack_behaviors


def run():
    # Instatiate ducks
    print("==== Model duck ====")
    model = duck.DuckHOF()
    model.perform_quack()
    model.perform_fly()
    model.display()

    print("==== True duck ====")
    model.perform_fly = fly_behaviors.fly_wings
    model.perform_quack = quack_behaviors.quack
    model.display()

    print("==== Toy duck ====")
    model.perform_fly = fly_behaviors.fly_rocket_powered
    model.perform_quack = quack_behaviors.squeak
    model.display()