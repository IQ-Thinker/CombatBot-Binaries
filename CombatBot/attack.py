class PooCannon:
    def __init__(self, attack_strength, othersAgility):
        self.damage = attack_strength / 3 + 15
        self.dodge = (100 / (250 - othersAgility)) * 80

class DiarrheaHurricane:
    def __init__(self, attack_speed, othersSpeed):
        self.damage = attack_speed / 3
        self.dodge = (200 / (300 - othersSpeed)) * 40

class VomitCloud:
    def __init__(self, attack_strength, othersSpeed):
        self.damage = attack_strength / 3 - 10
        self.dodge = (200 / (300 - othersSpeed)) * 15