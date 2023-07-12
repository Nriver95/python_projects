
# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    origin = "Unknown"

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.origin,)
        return msg


#child class
class Hunter(Organism):
    name = 'rookie'
    species = 'wyverian'
    legs = 2
    arms = 2
    origin = 'Kokoto'
    rank = 'Master'

    def BladeMaster(self):
        msg = "\nWields a great sword that can fell any monster, or beast."
        return msg
    
    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nOrigin: {}\nHunter Rank: {}".format(self.name,self.species,self.legs,self.arms,self.origin,self.rank)
        return msg

#second child class
class Monster(Organism):
    name = "Rathalos"
    species = "wyvern"
    legs = 2
    arms = 0
    origin = "Forest and Hills"
    variant = "silver"

    def HellFire(self):
        msg = "\nFires a ball of hellfire which disintegrates anything it touches."
        return msg

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nOrigin: {}\nVariant: {}".format(self.name,self.species,self.legs,self.arms,self.origin,self.variant)
        return msg


#third child class
class Companion(Organism):
    name = "Palico"
    species = "felyne"
    legs = 2
    arms = 2
    origin = "Forest and Hills"
    ability = "Support"

    def ShockTrap(self):
        msg = "\nLays a trap that paralyzes monsters and beasts."
        return msg

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nOrigin: {}\nType: {}".format(self.name,self.species,self.legs,self.arms,self.origin,self.ability)
        return msg


if __name__ == "__main__":
    hunter = Hunter()
    print(hunter.information())
    print(hunter.BladeMaster())

    companion = Companion()
    print(companion.information())
    print(companion.ShockTrap())

    monster = Monster()
    print(monster.information())
    print(monster.HellFire())
    
