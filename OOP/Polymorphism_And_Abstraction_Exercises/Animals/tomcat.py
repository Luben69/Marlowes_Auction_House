from Animals.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender='Male')

    @staticmethod
    def make_sound():
        return "Hiss"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age}" \
               f" year old {self.gender} {self.__class__.__name__}"