class cat:
    def __init__(self, color="black", breed="house"):
        self.color=color
        self.breed=breed

    def __str__(self):
        str_repr= ("Cat object with {} color and {} breed".format(self.color, self.breed))     
        return str_repr

        