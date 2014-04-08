class FlavorBoard(object):
    def __init__(self, active_for_date, flavors):
        self.active_for = active_for_date
        
        self.flavors = flavors
        
        self.kinds = flavors.keys()
