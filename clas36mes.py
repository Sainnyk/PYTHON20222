class Mes:
    nombre = ""
    temperaturaMax = 0
    temperaturaMin = 0



    def media(self):
       
        return (self.temperaturaMax + self.temperaturaMin) / 2 

    def __str__(self):
        return (self.nombre + ", Maxima: " + str(self.temperaturaMax) + ", Minima: " + str(self.temperaturaMin) + ", Media: " + str(self.media()))