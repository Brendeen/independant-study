class Band:
    def __init__(self, name="unknown", members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Band instance. Name = {self.name}"

    def play_solos(self):
        return [member.play_solo() for member in self.members]


class Musician:
    def __init__(self, name="unknown"):
        self.name = name

    def __str__(self):
        return self.name


class Guitarist(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @classmethod
    def get_instrument(cls):
        return "guitar"

    @classmethod
    def play_solo(cls):
        return "face melting guitar solo"


class Bassist(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    @classmethod
    def get_instrument(cls):
        return "bass"

    @classmethod
    def play_solo(cls):
        return "bom bom buh bom"


class Drummer(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @classmethod
    def get_instrument(cls):
        return "drums"

    @classmethod
    def play_solo(cls):
        return "rattle boom crash"
