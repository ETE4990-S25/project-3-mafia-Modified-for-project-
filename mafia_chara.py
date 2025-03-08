import random

class Townperson(object):
    """Create the base model of a townsperson"""
    def __init__(self, name, role,status,charnumber):
        self.name=name
        self.role=role
        self.status=status
        self.charnumber=charnumber

class playDetective(Townperson):
    """Creates the player version of the player character"""
    def __init__(self, name, role,status,charnumber):
        super.__init__(self, name, role,status,charnumber)