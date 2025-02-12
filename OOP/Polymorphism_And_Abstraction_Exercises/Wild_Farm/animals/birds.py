from Wild_Farm.animals.animal import Bird
from Wild_Farm.food import Meat, Vegetable, Seed, Fruit


class Owl(Bird):
    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def allowed_food(self):
        return [Meat, Vegetable, Seed, Fruit]

    @property
    def weight_increment(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
