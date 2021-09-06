# unlimited positional arguments
def add(*args):
    print(args[0])
    print(sum(args))


add(11, 5)


# unlimited key word arguments
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT_R")
print(my_car.model)
