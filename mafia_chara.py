class Townperson(object):
    """Create the base model of a townsperson"""
    def __init__(self, name, role, status):
        self.name=name
        self.role=role
        self.status="Alive"