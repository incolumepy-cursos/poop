from .duck import DecoyDuck, MallardDuck, ModelDuck, RubberDuck
from .fly_behavior import FlyRocketPowered

def run():
    # Instatiate ducks
    print("=======================")
    print("Mallard duck")
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    print("=======================")
    print("Rubber duck")
    rubber = RubberDuck()
    rubber.perform_quack()
    rubber.perform_fly()

    print("=======================")
    print("Decoy duck")
    decoy = DecoyDuck()
    decoy.perform_quack()
    decoy.perform_fly()

    print("=======================")
    print("Model duck")
    model = ModelDuck()
    model.perform_quack()
    model.perform_fly()
    # change fly behavior at runtime
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()

    # polymorphism
    # all ducks can swin and display yourself
    print("=======================")
    print("Display all ducks")
    for duck in (mallard, rubber, decoy, model):
        duck.display()
        duck.swin()


if __name__ == "__main__":
    run()
