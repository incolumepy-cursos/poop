__author__ = '@britodfbr'

def quack():
    def quack():
        m = "Quack!"
        print(m)
        return m
    return quack()


def squeak():
    def quack():
        m = "Squeak!"
        print(m)
        return m
    return quack()


def mute_quack():
    def quack():
        m = "<< silence >>"
        print(m)
        return m
    return quack()