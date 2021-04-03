__author__ = '@britodfbr'

from head_first_design_patterns.hofs_dinamics import duck
from head_first_design_patterns.hofs_dinamics import fly_behaviors
from head_first_design_patterns.hofs_dinamics import croak_behaviors

def run():
    # Instatiate ducks
    model = duck.DuckHOFDinamic(
        perform_quack=croak_behaviors.quack,
        perform_fly=fly_behaviors.fly_wings
    )
    print("\n====== True Duck ========")
    print('')
    print(model.display())
    print("\n====== Toy Duck =======")
    model.perform_quack=croak_behaviors.squeak
    model.perform_fly=fly_behaviors.fly_not
    print(model.display())
    print("\n====== Decoy Duck =======")
    model.perform_quack=croak_behaviors.mute_quack
    model.perform_fly=fly_behaviors.fly_not
    print(model.display())
    

