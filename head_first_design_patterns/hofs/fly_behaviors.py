__author__ = '@britodfbr'

def fly_wings():
    def fly():
        m = "I'm flying"
        print(m)
        return m
    return fly()


def fly_not():
    def fly():
        m = "I can't fly"
        print(m)
        return m
    return fly()


def fly_rocket_powered():
    def fly():
        m = "I'm flying with a rocket"
        print(m)
        return m
    return fly()